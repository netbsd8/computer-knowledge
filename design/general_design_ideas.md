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

