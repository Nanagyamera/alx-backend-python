Python Async Comprehension Examples

This repository provides examples of using async comprehensions in Python. It covers the following tasks:

1. `async_generator`: A coroutine that loops 10 times, asynchronously waits for 1 second, and yields a random number between 0 and 10 using the `async_generator` function.

2. `async_comprehension`: A coroutine that collects 10 random numbers using an async comprehension over the `async_generator` coroutine.

3. `measure_runtime`: A coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather()` and measures the total runtime.

Prerequisite

- Python 3.6 or higher

Usage

Clone the repository:

   git clone https://github.com/Nanagyamera/alx-backend-python.git

Change to the project directory:

cd 0x02-python_async_comprehension

Run the files and the output will display the results of the async comprehensions and the total runtime.

Contributions

Contributions to this repository are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request.

LICENSE

This repository is licensed under the MIT License.


