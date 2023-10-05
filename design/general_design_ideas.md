# Back of the envelope estimation
- requests/sec or queries/sec
  - MAU -> DAU -> activities/user
  - peak usage vs average usage
  - examples by using twitter
    - QPS
      - 300M MAU ->  50% -> 150M DAU -> 25% DAU make tweets and each make 2 tweets -> 150M * 0.5 = 75M/day
      - 75M tweets/day -> 75M/100K = average 750 tweets/sec
      - peak tweets: 750 * 2 = 1500 tweets/sec
    - Capacity
      - pictures: 150M tweets/day x 0.1 with pictures x 100KB x 400 days/year x 5 years x 3 copies = 9 X 10^15 = 9 PB
      - videos: 150M x 0.01 x 100MB x 400 x 5 x 3 = 900 PB
# Data
## meta data vs real data
## Schema
## DB
### meta data DB and blob/block/file system
- sql vs No sql
- hdfs / s3
### time-series
- additional indexes
### Column-oriented
- one column in a single file
## Storage
# Interface
## APIs
# Components
# processing
## streaming process -- real time
## batch process
- spark
## message broker
### types
- in-memory
  - it may need write-ahead log to support reliability (data not lost) 
- log-based
  - sequentially write into disk
  - every message is guaranteed to be delivered at least once

# Connection
## long polling
## web socket
# Query
## streaming - streaming join

# functional requirements
# capacity estimates
- 1 billion message per day
- 100 bytes on average per log/metric
- 100Gb of data per day
- read/write ratio
# throughput estimates

# API Endpoints
- sendMetric(source, payload, timestamp)
- fetchDataset(seriesId, timeRange)
# DB Schema
- user table
- 
# non-functional features
## metrics
## reliability
## efficiency

# Typical Questions
## TinyURL/PasteBin
- read >> write
  - read service and write service
- key(tinyUrl) -> value (realUrl)
  - NoSQL
- hash collapsing
  - key generation first
- caching
- load balancing
  - consistent hash
    - key: tinyUrl
## Twitter
- Functional requirements
  - make posts with text, image or video
  - follow other users
  - news feeds
- Capacity estimation
  - active users: 200M / day
  - 200 follows / user
  - 0.5 post / user -> 100M tweets / day
  - 300 bytes per tweet -> 30G tweet storage / day
  - 55TB of disk over 5 years
- Throughput
-  
- APIs
  - createPost(userId, content)
  - getPosts()
  - follow()/unfollow()

- DB schema
  - Posts table
    - userId: int
    - content: string
    - metadata: json
  - Users table
    - userId: int
    - email: string
    - password_hash: string
  - UserFollows table
    - userId1: int
    - userId2: int
- Design idea
  - push: update followers' reading cache (timeline) during writing (fanout)
  - pull: from hot spot
  - pre-generated timeline: application-level cache
  - shard: based on user id but not post id
  - post created time (epoch time) be part of the post ID: for searching the most recent timeline
## Dropbox
- requirements
  - upload/download
  - share
  - auto sync crossing devices (offline editing)
  - read and write heavy
- idea
  - chunk-based
    - update only changed chunks
    - retried only failed chunks
    - de-duplication
    - upload diffs but not whole chunk
- client
  - monitor changes and sync with remote
  - push vs pull
- server
  - metadata database
    - versioning
    - file/chunk, user, workspace
    - no-sql not support ACID
  - synchronization service
    - pub-sub message queue 
      - buffer burst of client requests -- handling heaving write
      - client also subscribe update from sync service
      - offline clients re-sync
## Job Scheduler
- functional requirements
  - running binary on dedicated compute cluster
  - instant and repeated scheduling
  - job must be run at least once
- capacity estimation
  - a few MB / job * 1k jobs / day
- APIs
  - scheduleJob(binary, timeSchedule) -> jobId
  - jobStatus(jobId)
- DB Schema
  - JobStatusTable
    - [jobid, binaryUrl, status, retryTimestamp]
- Architecture
  - HTTP/RPC call for requests
  - files to S3
  - message queue is not good to update the status
    - use DB to save the job status
  - index the timestamp to query, and run jobs whose timestamps are before the current time 
  - producer pull status from DB and insert into message queue
  - consumer pll jobs and run it,
  - distributed lock to avoid two consumers to run the same job
  - idempotent method such as request id is still needed in case a job is run by more than one consumers
  - for repeated jobs, it needs to add a record after the current run
  - a job claim service to update the DB in case worker is down
# Distributed Locking
- if the node holding the locker is down
  - TTL for the lock
  - heartbeat to the locking service
  - fencing token (increasing version number) to prevent old token is still used
- raft for consensus
  - leader election
  - comment phase for confirming the majority of followers 
  - queue fo locking request to prevent herding problem
# top K leaderboard
- requirements
  - top k events of any type
  - be able to get result for time window
- Capacity estimates
  - k < 1000
- APIs
  - fetchLeaderboard(k, start_time, end_time)
- DB schema
  - event table
- Architectural design
  - a ton of data, not calculate them in the flight.
  - pre-computing
  - message queue
    - customers (streaming processors) pull and counter by self and then merge
      - actually batch process for whole time window
    - for time window:
      - time series DB
      - approximately correct: 
        - pull every 10 mins from streaming processors results
        - count min sketch -- fast
# Chat
- Need to combine notification via device token
  - GCM / APNS for android and Apple
  - web socket for HTTP clients
- Group chat
  - pub-sub: message queue
- DB Schema
  - principle for sharding
    - based on the query
  - thread table
    - inbox: a list of threads:
      - SQL:
        - index by thread_id / participant_hash_code
      - NoSQL:
        - row key: 
          - thread_table: thread_id
          - participantHashCode: participant_hash_code
      - join operation
        - thread table: [id, last_message, created_at, avatar]
        - userThread table: [id, user_id, thread_id, is_muted, unread_count, joined_at, updated_at]
          - user_id + thread_id as primary key and for sharding
      - no join operation
        - userThread table: [user_id, thread_id, participant_users_id, is_muted, unread_count, last_message, avatar, created_at, updated_at]
          - user_id + thread_id as primary key
    - thread: a list of messages
  - message table: [message_id, thread_id, user_id, content, created_at]
    - noSql: no need to modify
    - sharding (row) key: thread_id
# notification
- store for offline users
- APIs
  - subscribeUser(userId, topicId)
  - publishNotification(topicId, message)
  - fetchNotification(userId)
- DB Schema
  - users(id, email, phone, webSocketConnect)
  - Topics(id, name, userList)
  - UnseenMessages(userId, message, timestamp)
- Architecture
  - duplicated messages: 
    - idempotent (key) vs two-phase comments
# web crawler
- BFS
- components
  - HTTP Fetcher: producer
  - URL frontier: data structure to store all URLs that remain to be downloaded. --> message queue
  - Extractor
  - Duplicate Eliminator
  - Datastore
# long polling vs websocket
- Long Polling (Poll Mode): Long polling operates in a "poll" or "request-response" mode. In this approach, the client sends periodic HTTP requests (polls) to the server, asking if there are any updates or new data. The server holds the request open until it has new information to send back to the client. This is more of a "pull" mechanism where the client actively requests updates from the server.
- WebSocket (Push Mode): WebSocket operates in a "push" mode. It establishes a persistent, full-duplex connection between the client and server. Once the connection is established, either party (client or server) can send data to the other at any time without waiting for a request. This allows for real-time "push" updates from the server to the client without the need for repeated requests.
# bloom filter
- It's designed to quickly determine whether an element is a member of a set, with a trade-off between memory usage and false positives. 
- use cases
  - membership testing
  - data deduplication
  - cache lookup
  - filter out packets or requests that don't match specific criteria
  - web crawl duplicates
  - spell checkers
# Consistent hash
- hash ring:
  - both node and data hash map to a ring point
    - data put on next first node with clockwise order
    - even distribution: real node -> virtual nodes
  - key mod (2^64)
  - a table to maintain the node -> hash range
    - coordinator to maintain
    - customer self maintain
- sharding key
  - how to shard data based on how to query data
    - user table: user_id
  - if search on multiple columns, it may need to build multiple tables with different sharding keys (columns name)
# Replica
- My SQL - master + slave
  - using Write Ahead Log to sync slave
    - WAL work on transaction as well: Data A at time B was changed from C to D
- Cassandra - 3 virtual nodes on hash ring
  - column-based NoSQL
  - row_key: partition key / hash key
    - user_id, no able to do range query
  - column_key
    - support range query (pre-defined index): 
      - query(row_key, col_start, col_end)
      - vs redis/memcached key-value pair


