# Caching
## strategies
- read cache-aside: web service will retrieve the missing data and then update the cache
- read cache-through: cache service will retrieve the missing data. It needs to warm the cache.
- write-through:  the data is written to both the cache and the backing store. This ensures that the data is always consistent between the two but can result in slower write performance
- write-around: write operations bypass the cache and are written directly to the backing store. 
- write-back: write operations are written to the cache and marked as “dirty.” The data is eventually written back to the backing store, but this can be done at a later time and may be done in a batch with other dirty cache entries.
## invalidation / eviction
- TTL: Each cached item is assigned a timestamp and a TTL value. Once the TTL expires, the corresponding item is automatically removed from the cache.
- FIFO vs LRU vs LFU vs RR
## metrics
- Hit Ratio
- Latency vs Throughput
## examples
- Memcached
- Redis
# Batching requests
- facts: mitigate network latency and request processing overhead when dealing with small data requests, and it involves combining multiple requests into a single batch for processing on the server side.
- solution:
  - Combine multiple requests into a single batch, which is processed by cluster nodes just like individual requests, and then respond with a batch of responses.
  - Requests are enqueued and tracked with unique request numbers, and a separate task continuously monitors queued requests.
- example:
  - Kafka supports producer request batching for improved performance: Batching allows multiple messages to be sent in a single request to the Kafka broker rather than sending each message individually. 
  - Batching is used in systems like Bookkeeper for flushing logs to disk.
  - Nagel's Algorithm in TCP batches smaller packets to enhance network throughput.
# Request pipeline
- facts:
  - Communicating between servers in a cluster using a Single Socket Channel can lead to performance issues when requests have to wait for previous responses.
  - To optimize throughput and latency, servers should keep their request queues filled to utilize server capacity efficiently.
  - For example, a Singular Update Queue can accept more requests while processing one, reducing wasted server capacity when sending only one request at a time.
- solution:
  - Nodes send requests without waiting for responses by using two separate threads for sending and receiving over a network channel.
  - The sender node sends requests over the socket channel without waiting.
  - A separate thread reads responses from the network channel.
  - Responses can be processed immediately or submitted to a Singular Update Queue.
- 🛠️ Request Pipeline Management:
  - To prevent overwhelming the receiving node, there's an upper limit on the number of inflight requests.
  - A blocking queue is used to track inflight requests, initialized with the maximum allowed.
  - Once a response is received, the corresponding request is removed from the queue to make room for more.
# Read-heavy vs Write-heavy