# Coordination
## Zookeeper
- It addresses coordination problems in distributed systems, including configuration management, leader election, distributed locks, and managing cluster membership.
- 📊 ZooKeeper Data Model: ZooKeeper features a hierarchical namespace, and each node (znode) can hold data and children.
  - uses a tree-like file system structure called znodes and provides primitive operations to manipulate them.
    - Persistent Znodes are permanently stored, while ephemeral Znodes are automatically deleted when the client disconnects.
    - 🌟 Ephemeral Nodes: These nodes exist as long as the session that created them is active. ephemeral Znodes are automatically deleted when the client disconnects.
    - 🔢 Sequence Nodes: Znodes can have monotonically increasing counters appended to their names. Ephemeral sequential Znodes have sequential numbers as suffixes and are useful for leader election.
- 🔍 Watches: Clients can set watches on znodes to receive notifications of changes.
- 📂 Data Access: Data stored in znodes can be read and written atomically.
- 🕰️ Time in ZooKeeper: ZooKeeper uses zxids and version numbers to track changes, not real-time.
- 📊 ZooKeeper Stat Structure: Contains metadata about a znode, including creation time and version information.
- 🔌 ZooKeeper Sessions: Clients establish sessions with ZooKeeper servers and manage state transitions.
- 🚀 Consistency Guarantees: ZooKeeper provides guarantees about data consistency.
### Examples:
[good example](https://bikas-katwal.medium.com/zookeeper-introduction-designing-a-distributed-system-using-zookeeper-and-java-7f1b108e236e)
#### Leader election:
- 🦋 In the leader election process:
  - Servers add a watch to the /election znode.
  - Servers create an ephemeral znode /leader under /election with their hostname as data.
  - Only one server succeeds in creating /leader, becoming the leader.
  - Servers call getChildren("/election") to find the leader's hostname.
  - 🦁 If the leader server goes down:
    - Zookeeper terminates its session after a timeout.
    - Deletes the /leader node, which is ephemeral.
    - Notifies all servers watching /election znode.
  - 🐏 When servers receive the leader's deletion notification:
    - They retry creating /leader, and one becomes the new leader.
    - Zookeeper notifies all servers again.
- 🐘 In Approach 2 for leader election:
  - Servers create ephemeral sequential znodes under /election.
  - The one with the least sequence number becomes the leader.
  - No extra write requests upon leader failure, reducing network traffic.
- 🐬 Approach 3 for leader election:
  - Servers set watches on child znodes with one less sequence.
  - If a leader goes down, only the next candidate is notified.
  - Reduces the herd effect.
#### Distributed locks
- The algorithm for managing distributed locks is the same as the leader election with a slight change.
  - Instead of the /election parent node, we will use /lock as the parent node.
  - The rest of the steps will remain the same as in the leader election algorithm. Any server which is considered a leader is analogous to the server acquiring the lock.
  - The only difference is, once the server acquires the lock, the server will perform its task and then call the delete operation on the child znode it has created so that the next server can acquire lock upon delete notification from zookeeper and perform the task.
#### Group membership/managing cluster state
- use a persistent znode to keep track of all the servers that join the cluster and the zookeeper’s ability to delete ephemeral znodes upon client session termination will come in handy in maintaining the list of active/live servers.
  - Create a parent znode /all_nodes, this znode will be used to store any server that connects to the cluster.
  - Create a parent znode /live_nodes, this znode will be used to store only the live nodes in the cluster and will store ephemeral child znodes. If any server crashes or goes down, the respective child ephemeral znode will be deleted.
  - Any server connecting to the cluster will create a new persistent znode under /all_nodes say /node1.domain.com. Let’s say another two-node joins the cluster. Then the znode structure will look like this:
    - /all_nodes/node1.domain.com
    - /all_nodes/node2.domain.com
    - /all_nodes/node3.domain.com
  - You can store any information specific to the node in znode’s data.
  - Any server connecting to the cluster will create a new ephemeral znode under /live_nodes say /node1.domain.com. Let’s say another two-node joins the cluster. Then the znode structure will look like this:
    - /live_nodes/node1.domain.com
    - /live_nodes/node2.domain.com
    - /live_nodes/node3.domain.com
  - Add a watch for any change in children of /all_nodes. If any server is added or deleted to/from the cluster, all server in the cluster needs to be notified.
  - Add a watch for any change in children of /live_nodes. This way all servers will be notified if any server in the cluster goes down or comes alive.
![structure](zookeeper_structure.webp)
# Message Queue
## Kafka
- the Kafka consumer follows a similar pattern to the Kafka producer. Kafka provides client libraries for various programming languages, and consumers are typically developed as custom applications using these libraries. 
  - Producer:
    - Buffering Messages: When a producer sends messages to Kafka, it doesn't immediately send each message as a separate request. Instead, it buffers messages in memory and groups them into batches. The producer specifies a maximum batch size or a maximum time interval for how long it will wait before sending a batch.
    - Compression: Kafka producers often apply message compression to reduce the size of messages before adding them to a batch. This is especially useful when sending large volumes of data. Kafka supports various compression algorithms, such as gzip, snappy, and lz4.
    - Topic-Partition Assignment: Messages within a batch are typically destined for the same topic and partition. Kafka ensures that messages intended for a specific topic-partition combination are grouped together.
    - Acknowledgment: Producers can configure acknowledgment settings to determine when a batch is considered "sent." For example, a producer can choose to wait for acknowledgment from the broker after all messages in a batch are successfully written, or it can configure acknowledgment for each message individually.
    - Background Sending: The Kafka producer operates in the background, continuously monitoring the buffered messages. When a batch size or time interval threshold is reached, the producer initiates a send operation to transmit the batch to the Kafka broker.
    - Retries: If a batch cannot be successfully sent to the broker due to network issues or broker unavailability, the producer can be configured to retry sending the batch after a certain number of retries or a specified retry delay.
    - Configurability: Kafka provides producers with various configuration options to fine-tune the batching behavior, including batch size, linger time (maximum wait time for accumulating messages in a batch), and compression settings.
  - Consumer:
    - Consumer Application: Customers can build their own consumer applications using the Kafka client libraries. These applications are responsible for subscribing to Kafka topics, fetching and processing messages, and handling various aspects of message consumption.
    - Customization: Consumer applications can be customized to define how messages are processed, including deserialization, data transformation, business logic, and error handling.
    - Configuration: Kafka consumers can be configured with various settings, such as the Kafka broker endpoints, consumer group ID, topic subscriptions, message offset management, and more.
    - Integration: Consumer applications can be integrated into a broader data processing pipeline, application architecture, or microservices environment to consume messages from Kafka topics and take appropriate actions based on the message content.
    - Scaling: Kafka consumers can be scaled horizontally to handle increased message throughput and provide fault tolerance. This can be achieved by deploying multiple consumer instances within a consumer group.