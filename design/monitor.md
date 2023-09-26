# Alerting
- Alertmanager can group alerts it detects to be related; for example, a major network outage might result in hundreds of individual alerts, but Alertmanager can group all of these into a single message, so that responders aren’t overwhelmed with pages.
- ![Alert Manager](Prometus_Alerting.png)
# Service Discovery
# Coordination
## Zookeeper
- 📊 ZooKeeper Data Model: ZooKeeper features a hierarchical namespace, and each node (znode) can hold data and children.
- 🔍 Watches: Clients can set watches on znodes to receive notifications of changes.
- 📂 Data Access: Data stored in znodes can be read and written atomically.
- 🌟 Ephemeral Nodes: These nodes exist as long as the session that created them is active.
- 🔢 Sequence Nodes: Znodes can have monotonically increasing counters appended to their names.
- 🕰️ Time in ZooKeeper: ZooKeeper uses zxids and version numbers to track changes, not real-time.
- 📊 ZooKeeper Stat Structure: Contains metadata about a znode, including creation time and version information.
- 🔌 ZooKeeper Sessions: Clients establish sessions with ZooKeeper servers and manage state transitions.
- 🚀 Consistency Guarantees: ZooKeeper provides guarantees about data consistency.