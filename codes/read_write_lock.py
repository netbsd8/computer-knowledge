import threading

class ReadWriteLock:
    def __init__(self):
        self.lock = threading.Lock()
        self.readers_cv = threading.Condition(self.lock)
        self.writers_cv = threading.Condition(self.lock)
        self.readers_count = 0
        self.writers_count = 0

    def acquire_read(self):
        with self.lock:
            while self.writers_count > 0:
                self.readers_cv.wait()
            self.readers_count += 1

    def release_read(self):
        with self.lock:
            self.readers_count -= 1
            if self.readers_count == 0:
                self.writers_cv.notify()

    def acquire_write(self):
        with self.lock:
            while self.readers_count > 0 or self.writers_count > 0:
                self.writers_cv.wait()
            self.writers_count += 1

    def release_write(self):
        with self.lock:
            self.writers_count -= 1
            if self.writers_count == 0:
                self.readers_cv.notify_all()

# Example usage:
rw_lock = ReadWriteLock()

def reader_thread():
    rw_lock.acquire_read()
    # Read from the shared resource
    rw_lock.release_read()

def writer_thread():
    rw_lock.acquire_write()
    # Write to the shared resource
    rw_lock.release_write()
