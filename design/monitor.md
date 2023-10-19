# System
- ![system components](monitoring_system_example.png)
# Metrics
## average
## distribution
# Logs
## Analytics DB - Scuba
# Alerting
- Alertmanager can group alerts it detects to be related; for example, a major network outage might result in hundreds of individual alerts, but Alertmanager can group all of these into a single message, so that responders aren’t overwhelmed with pages.
- ![Alert Manager](Prometus_Alerting.png)
# Service Discovery
# Data Storage
## time series DBs
- tags (index for multiple dimensions)
- down sampling (second -> minute)
# Tracing - UUID 
- When a new request enters your application and there is no incoming trace_id, it often means that this request is the entry point of a new trace.
- In distributed tracing systems like Zipkin or Jaeger, the trace_id is typically generated at the entry point of a request (e.g., at the edge of your system, such as a web server).
- The trace_id is propagated through the system as the request flows through various services. Each service generates its own span_id within the same trace, allowing you to trace the entire journey of a request.
- The span_id represents an individual operation or unit of work within a service. Each service creates and manages its own span_id, and these span_ids are related to the same trace_id.
- If a trace_id doesn't exist in the incoming request headers, your application should generate a new span_id locally for the current service, and this new span_id should be associated with a new trace_id, effectively starting a new trace for this request.
- The trace_id should ideally be generated using a unique identifier or a random value to ensure it is globally unique across your distributed system.
- The generated trace_id and span_id should then be included in the outgoing request headers when making requests to downstream services, allowing the trace to continue across services.
- In practice, many distributed tracing libraries and frameworks provide functionality to generate new trace_id values and handle trace context propagation automatically.

