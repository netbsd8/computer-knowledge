# thread pool
"""
Initialization: You create an instance of ThreadPoolExecutor and specify the maximum number of worker threads that can be active simultaneously.

Submitting Tasks: You submit tasks (functions and their arguments) to the thread pool using the submit method. This returns a Future object that represents the computation of the function.

Working: The thread pool maintains an internal queue of tasks. Worker threads pick tasks from this queue and execute them. The results (or exceptions, if any occurred) are stored in the corresponding Future object.

Retrieving Results: You can query the Future object for the result using its result method. This method blocks until the result becomes available. Alternatively, you can use the as_completed function of the concurrent.futures module to iterate over Future instances as they complete.

Shutdown: When done, it's essential to call the shutdown method of the ThreadPoolExecutor to allow it to clean up resources.
"""

import concurrent.futures

# A sample function to be executed in a thread
def compute(n):
    return n * n

# Using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks
    future_to_num = {executor.submit(compute, num): num for num in range(10)}
    
    # Retrieve results as they become available
    for future in concurrent.futures.as_completed(future_to_num):
        num = future_to_num[future]
        try:
            result = future.result()
            print(f"{num} squared is {result}")
        except Exception as exc:
            print(f"{num} generated an exception: {exc}")


# Promise and future
import concurrent.futures
import time

def slow_function(seconds):
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit a slow function for execution
    future = executor.submit(slow_function, 2)
    
    # Add a done callback
    future.add_done_callback(lambda f: print("Task completed!"))
    
    # Or Periodically check if the task has completed
    while True:
        if future.done():
            print("Task has completed!")
            break
        else:
            print("Task is still running...")
            time.sleep(1)

    # Wait and retrieve the result
    print(future.result())
 

# Async IO 
"""
async def: Declares an asynchronous function. These functions don't run immediately when called but instead return a coroutine object. You need to either await them or schedule them in an event loop to run.

await: Pauses the execution of the asynchronous function until the awaited function completes. During this pause, other tasks can run.

asyncio.gather: A function that takes multiple coroutines (or futures) and runs them concurrently.

asyncio.run: A utility function provided in Python 3.7+ to execute an async function and run the event loop until completion.
"""

import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['https://www.example.com', 'https://www.example.org', 'https://www.example.net']

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for url, response_text in zip(urls, responses):
            print(f"URL: {url}, Content Length: {len(response_text)}")

if __name__ == "__main__":
    asyncio.run(main())
