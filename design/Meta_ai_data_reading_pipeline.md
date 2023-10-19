# Main idea
#  
# Reliability
## Failure handling - failover
- recoverable failures: 
  - read from data warehouse / write to upstream  
  - retry
- non-recoverable failures: 
  - input parameters error
  - system crash
## Snapshot
# Efficiency
## Locality
- schedule job with the same data location
- reading data from local region
# Monitoring
## Failure detection
### metrics
- failure rate
## Reasoning - Analysis
### logging
- root cause analysis
### alerting
## efficiency regression detection
### metrics
- throughput: QPS
- latency

# Order handling
- no needed