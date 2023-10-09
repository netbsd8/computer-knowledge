# GIL: Remember the Global Interpreter Lock in CPython. 
# This can be a limitation for CPU-bound tasks. 
# If you're looking to parallelize CPU-bound tasks, 
# consider using multiprocessing or a different Python implementation like PyPy or Jython.

import threading
import time
import random


def square(number, results, index):
    results[index] = number * number

numbers = [1, 2, 3, 4]
results = [None] * len(numbers)
threads = []

for i, number in enumerate(numbers):
    thread = threading.Thread(target=square, args=(number, results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(results)  # Outputs: [1, 4, 9, 16]

# Synchronization
# mutex - Lock()

# This is our shared resource.
counter = 0

# This is the function that each thread will execute.
def increment_counter(lock):
    global counter
    for _ in range(100000):
        # Acquiring the lock before updating the counter.
        with lock:
            counter += 1

# Create a lock object.
lock = threading.Lock()

# Create two threads that will run the increment_counter function.
t1 = threading.Thread(target=increment_counter, args=(lock,))
t2 = threading.Thread(target=increment_counter, args=(lock,))

# Start both threads.
t1.start()
t2.start()

# Wait for both threads to finish.
t1.join()
t2.join()

print(counter)  # Expected output: 200000 

# Condition variable
# Shared resource
buffer = []
BUFFER_SIZE = 5

# Condition variable
condition = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1, 100)
            with condition:
                while len(buffer) == BUFFER_SIZE:
                    print("Buffer full, producer is waiting")
                    condition.wait()
                buffer.append(item)
                print(f"Produced {item}. Buffer: {buffer}")
                condition.notify()
            time.sleep(random.uniform(0.1, 0.7))

class Consumer(threading.Thread):
    def run(self):
        global buffer
        while True:
            with condition:
                while not buffer:
                    print("Buffer empty, consumer is waiting")
                    condition.wait()
                item = buffer.pop(0)
                print(f"Consumed {item}. Buffer: {buffer}")
                condition.notify()
            time.sleep(random.uniform(0.2, 0.8))

# Start one producer and one consumer
Producer().start()
Consumer().start()

"""
In C++, when you use condition variables (from the <condition_variable> header), you often pair them with a mutex. The typical pattern involves:

Locking the mutex.
Checking a condition. If the condition isn't met, you wait on the condition variable.
Once the condition is met (often signaled by another thread), you continue execution.
Finally, you unlock the mutex.
In Python, the Condition class from the threading module simplifies this process by integrating a lock (similar to a mutex). When you use a Condition object inside a with statement, it automatically:

Acquires the associated lock when entering the with block.
Releases the associated lock when exiting the with block.

The key difference is in the syntactic sugar that Python provides with the with statement and the Condition class, which makes the code more concise and less error-prone.

# for C++
std::unique_lock<std::mutex> lock(my_mutex);
while (!condition_met) {
    cond_var.wait(lock);
}

# for python
with condition:
    while not condition_met:
        condition.wait()
"""

# Semaphore
import threading
import time

# Create a semaphore with a maximum count of 3
semaphore = threading.Semaphore(3)

def access_resource(thread_id):
    print(f"[{thread_id}] Acquiring semaphore")
    with semaphore:
        print(f"[{thread_id}] Semaphore acquired")
        time.sleep(2)
    print(f"[{thread_id}] Semaphore released")

# Start 5 threads that want to access a resource controlled by the semaphore
for i in range(5):
    threading.Thread(target=access_resource, args=(i,)).start()

# Or implemented via condition variable
class Semaphore:
    def __init__(self, initial):
        self._count = initial
        self._cond = threading.Condition()

    def acquire(self):
        with self._cond:
            while self._count <= 0:
                self._cond.wait()
            self._count -= 1

    def release(self):
        with self._cond:
            self._count += 1
            self._cond.notify()