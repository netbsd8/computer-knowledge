import mmap
import os
import time

# Open the file for reading
f = open('example.txt', 'r')

# Map the file to memory
mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

# Advise the kernel about the expected usage pattern
madvise_flags = mmap.MADV_SEQUENTIAL | mmap.MADV_WILLNEED
mmap.madvise(mm, 0, 0, madvise_flags)

# Warm up the page cache by reading the entire file
start = time.time()
mm.seek(0)
while mm.read(1024*1024):
    pass
end = time.time()
print(f"Read the entire file in {end - start} seconds")

# Check which pages are resident in memory
page_size = os.sysconf('SC_PAGE_SIZE')
page_count = (mm.size() + page_size - 1) // page_size
page_in_mem = bytearray(page_count)
mincore_flags = mmap.MAP_SHARED | mmap.MAP_POPULATE
mmap.mincore(mm, mm.size(), page_in_mem, mincore_flags)

# Print the number of resident pages
print(f"{sum(page_in_mem)} out of {page_count} pages are resident in memory")

# Close the file and release the memory mapping
mm.close()
f.close()
