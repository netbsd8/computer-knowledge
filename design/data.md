# Collection
## Push vs Pull
- Prometheus: pull
	- multiple instances can pull metrics data;
	- better detection if service is up and running;
	- needs a service discovery to discover the targets
	- prometheus.yml:
		- which targets
		- at what interval
    - hard to scale
- ODS push: 
	- agent needed on each node, but it can do more things like aggregation/temp persistent
	- high networking traffic
	- easy to send data to a centralized monitoring server
	- easy to scale (just on server side)
# Storage
## Replication
## Sharding
- sharding key / partition key
  - user id
- resharding data / moving data around
  - consistent hash
- celebrity problem
  - allocate a shard for each celebrity or further partition
- join and de-normalization

# Query
# Use Cases
## Time Series DBs
- Challenge and opportunity
     - scale of data
     - a****append-only data(or insert-only)****
     - always timestamped and ordered by timestamp
 - Use cases
     - Time-series data is primarily used for running analytics and deducing conclusions.
     - A time series database usually has two main functions -- ingest a lot of data in chronological order, and provide flexible queries on ranges of that data.
 - When to NOT use it
     - if your data is not timestamped
     - if your data is not huge, then a SQL database can handle it as well
 - The design of these systems with time as a key index is distinctly different from [relational databases](https://en.wikipedia.org/wiki/Relational_database) which reduce discrete relationships through referential models.
 - The unique properties of time series datasets mean that time series databases can provide significant improvements in storage space and performance over general purpose databases.
     - For instance, due to the uniformity of time series data, specialized compression algorithms can provide improvements over regular compression algorithms designed to work on less uniform data.
 - Time series databases can also be configured to regularly delete old data, unlike regular databases which are designed to store data indefinitely
     - ****downsampling****
     - TimescaleDB allows you to reduce the granularity of your data by aggregating data into coarser periods of time and dropping the finer-grained real-time data while maintaining data accuracy.
 - Special [database indices](https://en.wikipedia.org/wiki/Database_index) can also provide boosts in query performance.
     - *TimescaleDB showed 200% to 5400% faster queries than MongoDB during our benchmark evaluation.*

 - Functional Requirements:
     - Windowing functions
     - Sharding capabilities
     - TTL support
     - Aggregate pipelines.
 - Design philosophy
     - Leverage the aforementioned characteristics
         - insert only
         - timestamped
         - older data is less queried
     - Main ideas
         - Sharding
         - Right data structure
         - Other smaller tools/components
 - A few design methodologies(there are multiple different ideas)
     - [Log-structured merge (LSM) trees](http://www.cs.umb.edu/~poneil/lsmtree.pdf), like Influx DB
         - shards will be created for each 7 day block of time
     - Build on top of SQL database with chunks, like timescale DB
     - others
 - Some other considerations
   - compaction
   - retention
   - indexing
  - Examples
    - Prometheus
    - InfluxDB