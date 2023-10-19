# feature
## transparent huge pages 
- Transparent Huge Pages (THP) is a feature of the Linux kernel that improves memory management performance by grouping pages into larger units called "huge pages". A page is a fixed-size block of memory that is used by the operating system to store data and code. By default, pages in Linux have a size of 4 kilobytes. THP allows these pages to be grouped into larger blocks of memory, such as 2 megabytes or 1 gigabyte.

- The main benefit of THP is that it reduces the overhead associated with managing large amounts of memory. When a process needs to allocate or free memory, the operating system must update data structures that track the state of each page. With THP, the number of pages that need to be updated is reduced, since each huge page contains many smaller pages. This can result in significant performance improvements, especially for applications that use large amounts of memory.

- However, THP can also have negative impacts on performance in some cases. One issue is that the larger page size can cause memory fragmentation, which can lead to inefficient memory usage and reduce the effectiveness of the kernel's memory management algorithms. THP can also cause increased memory usage, since it reserves a larger amount of memory for each allocation, even if the full amount is not needed. This can result in increased swapping and decreased overall system performance.
## vm.zone_reclaim_mode
- a kernel parameter in Linux that controls how the kernel manages memory allocation and reclamation. Specifically, vm.zone_reclaim_mode controls the behavior of the kernel when there is memory pressure in a particular memory zone. 
- Memory zones are logical partitions of physical memory, which are used to separate different types of memory usage, such as kernel memory and user memory. When there is memory pressure in a particular memory zone, the kernel may need to reclaim memory from other zones to satisfy the demand.
  - 0 (default): Zone reclaim is disabled.

  - 1: Zone reclaim is enabled, but pages are only reclaimed from the same memory zone.

  - 2: Zone reclaim is enabled, and the kernel can reclaim pages from other zones if necessary.

  - 4: Zone reclaim is enabled, and the kernel will attempt to avoid reclaiming pages from zones that are distant from the current memory node.

  - 8: Zone reclaim is enabled, and the kernel will attempt to avoid reclaiming pages from zones that have a different NUMA node ID.
- Zone
  - DMA zone: This memory zone is used for memory that can be accessed by devices using DMA (Direct Memory Access) operations. This zone is typically used for low-memory devices, such as sound cards and network adapters.

  - DMA32 zone: This memory zone is used for memory that can be accessed by devices using 32-bit DMA operations. This zone is typically used for devices with larger memory requirements, such as graphics cards.

  - Normal zone: This memory zone is used for general-purpose memory usage, such as user space and kernel memory.

  - HighMem zone: This memory zone is used for memory that cannot be directly accessed by the kernel due to its high address space. This zone is typically used for systems with large amounts of memory (more than 4 GB).

  - Movable zone: This memory zone is used for memory that can be moved around in physical memory by the kernel. This zone is typically used for memory that is not frequently accessed, such as cache or buffer memory.
## madvise
- madvise is a system call in Linux that can be used to provide hints to the kernel about how an application intends to use its memory. One of the hints that can be provided by madvise is related to Transparent Huge Pages (THP) and can be used to control how the kernel manages huge pages for a particular memory region.
- MADV_NORMAL: This is the default setting and indicates that the application has no specific requirements or hints for how the kernel should manage its memory.

- MADV_RANDOM: This hint indicates that the application is accessing memory randomly, and that the kernel should avoid caching the memory for sequential access.

- MADV_SEQUENTIAL: This hint indicates that the application is accessing memory sequentially, and that the kernel should optimize caching and prefetching for sequential access.

- MADV_WILLNEED: This hint indicates that the application is likely to access the memory region in the near future, and that the kernel should prefetch the data into memory to avoid performance penalties when the data is actually accessed.

- MADV_DONTNEED: This hint indicates that the application no longer needs the memory region, and that the kernel can reclaim the memory and free up system resources.

- MADV_HUGEPAGE: This hint indicates that the application is likely to benefit from Transparent Huge Pages (THP), and that the kernel should attempt to use THP for the memory region.

- MADV_NOHUGEPAGE: This hint indicates that the application does not benefit from THP, and that the kernel should avoid using THP for the memory region.