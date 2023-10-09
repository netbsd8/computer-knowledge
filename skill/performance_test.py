import time

def count_lines_readlines(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return len(f.readlines())

def count_lines_iter(filepath):
    count = 0
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for _ in f:
            count += 1
    return count

def measure_time(func, filepath, runs=10):
    total_time = 0
    for _ in range(runs):
        start_time = time.time()
        result = func(filepath)
        end_time = time.time()
        total_time += (end_time - start_time)
    return result, total_time / runs

# create a file with 1 million lines
with open("large_file.txt", "w") as f:
    for _ in range(10**6):
        f.write("This is a test line.\n")


filepath = "large_file.txt"
runs = 10
lines_readlines, avg_time_readlines = measure_time(count_lines_readlines, filepath, runs)
lines_iter, avg_time_iter = measure_time(count_lines_iter, filepath, runs)

print(f"Using readlines() over {runs} runs: {lines_readlines} lines in {avg_time_readlines:.4f} seconds on average.")
print(f"Using line-by-line over {runs} runs: {lines_iter} lines in {avg_time_iter:.4f} seconds on average.")
