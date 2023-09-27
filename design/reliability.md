# Failures
### process crash
### network delay
### not synchronized clock
### data consistency
-- Two Phase Commit: Often uses Versioned Value based storage to achieve better throughput without conflicting locks.
# Failure Detection
## heartbeat
# Fault Tolerance - redundancy
## data replication on multiple servers
# Consistency
## Quorum
- General idea
  - ⚙️ A cluster confirms an update when a majority (quorum) of its nodes acknowledge it (n/2 + 1 nodes for n nodes).
  - 🔄 Quorum indicates the number of tolerated failures (cluster size minus quorum) for fault tolerance (2f + 1 for 'f' failures).
  - ⚖️ Cluster size choice is based on write operation throughput and tolerated failures; practical sizes are three or five servers.
    - 📈 Doubling servers reduces throughput by half, and merely adding one server may not increase fault tolerance.
- 📊 Examples
  -  Updating data in clusters and leader election, ensuring data visibility and leader selection based on majority votes.
  -  📚 Consensus implementations like Zab, Raft, Paxos are quorum-based.
  -  📡 In systems not using consensus, quorum ensures the latest update is available to at least one server during failures or network partitions, as seen in databases like Cassandra.
- Quorum-based approaches are insufficient for strong consistency.
  - ⚙️ Inconsistencies occur when consecutive reads show the latest values disappearing during server failures.
  - 🔄 No guarantee is provided by the storage cluster to ensure consistent values for subsequent reads.
- Quorum-based consensus algorithms degrade throughput as cluster size increases.
  - Solution (Zookeeper: leader-follower)
    - Implement a smaller, 3 to 5 node cluster for linearizability and fault tolerance.
    - Use this cluster to manage metadata and cluster-wide decisions for larger data clusters.
    - 🖥️ Handling Client Interactions:
      - Finding the leader: Clients need to connect to the leader server.
      - Handling duplicate requests: Idempotent Receiver pattern used for duplicate detection.
      - State Watch: Used for notifications of metadata changes or time-bound leases.
    - Examples:
      - Google uses Chubby for coordination and metadata management.
      - Kafka uses Zookeeper for metadata and leader election.
      - Bookkeeper uses Zookeeper for cluster metadata.
      - Kubernetes uses etcd for coordination and group membership.
      - Big data systems like HDFS, Spark, and Flink use Zookeeper for high availability and coordination.
## Leader-Follower
### Concept
- 🙋‍♂️ Select one server as the leader among a cluster to make decisions for the entire cluster.
- 🔄 Leader propagates decisions to all other servers.
- 🚀 Servers initiate a leader election process at startup.
- 🗳️ Only the leader handles client requests; followers forward requests to the leader.
- Zookeeper is used as external leader election service
### Follower Reads
- Read-only requests can be directed to the nearest follower, reducing the load on the leader, but this may result in slightly older data being read.
- Cluster nodes maintain metadata about their location, allowing clients to select the nearest replica.
- Latency information is used to choose the follower with the least network latency.
- Slow or disconnected followers can be identified and excluded from serving requests.
- Clients can experience issues when reading immediately after writing, as the read request might go to a follower with outdated data.
  - To ensure consistency, servers store version stamps with each write, and clients include these stamps in read requests, ensuring they read the correct data.
- A timeout value is set for follower updates, and if not met, an error response is returned, allowing clients to retry with other followers.
- 💡 Linearizable reads may be required when replication lag cannot be tolerated, and such requests are redirected to the leader.
- 💼 Examples from various databases, including Neo4j, MongoDB, CockroachDB, and Kafka, showcase implementations of causal consistency and handling of read requests from followers.
# Client requests
## Idempotent receiver -- deal with duplicate message
- fact: 📡 Clients face uncertainty about request status, as responses may be lost or servers might crash.So, duplicated requests
- idempotent: describes a property of a server operation or request handler, indicating that the operation can be safely retried without causing unintended side effects.
- Client requests:
  - Idempotent Requests:
    - An idempotent request is one that can be safely repeated or retried multiple times without changing the result beyond the initial request.
    - When you make the same idempotent request multiple times, the outcome should be the same as if you had made it only once.
    - These requests do not have unintended side effects on the server or the system's state when repeated.
    - Common HTTP methods that are typically idempotent include GET, HEAD, PUT, and DELETE.
    - For example, a GET request for retrieving information or a DELETE request for deleting a resource can be considered idempotent.
- Non-Idempotent Requests:
  - A non-idempotent request is one where making the same request multiple times can result in different outcomes or unintended side effects.
  - Repeating non-idempotent requests may lead to changes in the system's state or data, or it may perform actions that are not safe to repeat.
  - The most common non-idempotent HTTP method is POST, which often creates a new resource or initiates a unique action with each request.
  - Other methods, such as PATCH or POST requests that trigger non-idempotent operations, may also be considered non-idempotent.
  - For example, submitting an order for a product (via a POST request) would typically create a new order, and repeating the request would result in multiple orders.
- solution: 
  - 💡 Assigning unique client IDs during registration helps ensure requests are processed correctly.
  - 🔄 Servers create sessions to store client responses, discarding inactive ones.
  - 📚 Servers store responses for non-idempotent requests and return them upon re-request.
  - 📆 Sessions on servers have a maximum time to live and can be removed if no HeartBeats are received.
  - ⏲️ Scheduled tasks periodically check and remove expired client sessions.
# Automatic Failover
# Examples
## message queue
- handle situation (saving data) if either consumer or producer failed