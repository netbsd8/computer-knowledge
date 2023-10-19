# kernel networking bypass
## DPDK
- a userland NIC driver or SR-IOV
- great for packet generator
- downside: lost that nic an sockets, iptables, netfilter
- poll with high cpu usage
## XDP
# networking path
[networking ingress/egress](../pictures/linux_networking_path_03.png)
## DNAT vs SNAT
- DNAT (Destination NAT): DNAT allows incoming traffic to be redirected to a different destination IP address and/or port. This is often used to forward traffic to a different internal server or to redirect incoming traffic to a specific service, such as a web server. DNAT can be used to implement port forwarding, load balancing, or to redirect traffic for security reasons.
  - iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:80

- SNAT (Source NAT): SNAT allows outgoing traffic to appear as if it is originating from a different IP address than the one used by the source device. This is often used to hide the identity of internal devices from external networks or to allow multiple devices on a network to share a single public IP address. SNAT can also be used to implement load balancing or to reduce the number of public IP addresses required by an organization.
  - iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
## components
### intermediate cache (proxy server/CDN)
- The caching policy for an intermediate cache, such as a proxy server or a CDN, will be based on both its own configuration and the cache headers provided by either the client or the server.

- When an intermediate cache receives a request from a client, it will first check its own caching configuration to determine if it has a cached copy of the requested resource and whether that copy is still fresh. If the cache does not have a valid copy of the resource, it will forward the request to the origin server and cache the response based on the cache headers returned by the server.

- Similarly, when an intermediate cache receives a request from an origin server, it will check the cache headers provided by the server to determine whether it can cache the response and for how long. If the cache headers prohibit caching or if the response is already stale, the cache will not cache the response and will instead forward the request to the client.
- The caching duration is specified using various cache control headers, including the max-age and s-maxage directives. The max-age directive specifies the maximum time that a client or an intermediate cache can keep a cached response, while the s-maxage directive applies only to intermediate caches and specifies the maximum time that an intermediate cache can keep a cached response
- Cache invalidation can be triggered by several methods, including explicit invalidation requests from the server, updates to the cached data, or the expiration of the caching duration. Some cache control headers, such as no-cache and must-revalidate, require that the cache validate the cached response with the origin server before serving it to the client.
- When an intermediate cache receives a request for a resource that it does not have in its cache, it can handle the cache miss in several ways. It can forward the request to the origin server, cache the response for a specified period, or serve a stale cached response if one is available and valid according to the cache control headers.
### netfilter
- conntrack
  - conntrack (connection tracking) is a mechanism used to track the state of network connections and the packets associated with them as they traverse through the network stack. Conntrack is implemented in the kernel and is used by various netfilter components, such as iptables, to provide advanced network functionality, such as stateful packet inspection and NAT (Network Address Translation).
  - The connection tracking table is a data structure used by the conntrack module to keep track of active connections, their states, and associated packet information. The table is used by netfilter components to perform advanced network functions, such as stateful packet inspection, where incoming packets are inspected based on the state of the connection they belong to.
  - When iptables evaluates each packet individually, it performs a full set of rule checks on each packet, which can be resource-intensive and slow down processing. By contrast, per-connection tracking evaluation only needs to perform the full set of rule checks on the first packet of a connection, and subsequent packets for the same connection can be processed more quickly based on the connection state.

## Queueing Disciplines
- Queueing Disciplines in Linux are a set of techniques used to manage network traffic and improve the performance and fairness of the networking stack. Queueing Disciplines are implemented in the Linux kernel's network subsystem and are used to control how packets are buffered, scheduled, and transmitted over the network.

  - First-In-First-Out (FIFO): This is the simplest Queueing Discipline, where packets are transmitted in the order they arrive. This can lead to poor performance and fairness in congested networks, as some flows may dominate the queue and starve other flows.

  - Stochastic Fairness Queueing (SFQ): This is a Queueing Discipline that attempts to provide fairness among flows by dividing packets into multiple queues and scheduling them in a randomized manner. This can help to avoid the problem of queue starvation and provide better performance and fairness in congested networks.

  - Hierarchical Token Bucket (HTB): This is a more advanced Queueing Discipline that allows traffic to be classified into different classes based on certain criteria, such as IP addresses or protocols. Each class can then be given a different amount of bandwidth and latency guarantees, which can help to provide better quality of service (QoS) for different types of traffic.

  - Network Emulation (NETEM): This is a Queueing Discipline that is used for testing and emulation purposes, and allows administrators to introduce various types of network delays, packet losses, and other types of network impairments.
- Ingress: When a packet arrives at a network interface, it is processed by the ingress Queueing Disciplines to determine how it should be buffered and scheduled for processing by the kernel's networking stack. This can include actions such as classification, policing, shaping, and scheduling of the packets based on their type, source, or destination.

- Egress: Once the packet has been processed by the networking stack, it is then transmitted over the network through the egress Queueing Disciplines. These disciplines can be used to apply various policies and mechanisms to control the transmission of packets, such as traffic shaping, congestion control, and bandwidth allocation.
## ip tunneling
- IP tunneling is a technique used to encapsulate IP packets within other IP packets, enabling them to traverse networks that would not normally be possible due to different IP address ranges, routing policies, or security policies.
- Tunneling involves creating a virtual network link between two endpoints, with IP packets being encapsulated within packets of another protocol, such as GRE (Generic Routing Encapsulation), IPsec, or L2TP (Layer 2 Tunneling Protocol). The encapsulated packets are then sent over the network using the outer protocol, which allows them to traverse networks that would not normally be reachable.

## web socket
- When a client initiates a WebSocket connection, it first sends an HTTP request to the server with a specific set of headers that indicate that the client wants to upgrade the connection to a WebSocket connection. If the server supports WebSockets, it responds with an HTTP response that also includes specific headers indicating that the connection has been upgraded.

- Once the WebSocket connection has been established, it is no longer an HTTP connection, but rather a persistent, full-duplex TCP connection between the client and server. Data can be transmitted in both directions over the WebSocket connection at any time, without the need for additional HTTP requests or responses.
## 4-way TCP connection closing
- The client sends a FIN segment to the server, indicating that it has no more data to send.

- The server responds with an ACK segment, indicating that it has received the FIN segment.

- The server sends a FIN segment to the client, indicating that it has no more data to send.

- The client responds with an ACK segment, indicating that it has received the FIN segment and that the connection is now closed.
# Performance
## Bandwidth vs Throughput
- Bandwidth: Bandwidth refers to the maximum amount of data that can be transmitted over a network in a given time period. It is usually measured in bits per second (bps), and it is a measure of the capacity of a network connection. For example, a network connection with a bandwidth of 100 Mbps can transmit up to 100 million bits of data per second.

- Throughput: Throughput, on the other hand, refers to the actual amount of data that is transmitted over a network in a given time period. It is also measured in bits per second (bps), and it is a measure of the actual performance of a network connection. For example, a network connection with a bandwidth of 100 Mbps may have a throughput of 80 Mbps, depending on various factors such as network congestion, packet loss, and network latency.
# millions of connections
- Scaling out: One of the most effective strategies for handling large numbers of connections is to scale out horizontally, by adding more servers to the cluster. This can be accomplished using load balancers and other techniques for distributing traffic across multiple servers. By dividing the workload across multiple servers, each server can handle a smaller number of connections, which reduces the overhead and resource requirements for each server.

- Kernel optimizations: The Linux kernel provides a number of optimizations for improving network performance, such as TCP Fast Open, epoll, and SO_REUSEPORT. These features are designed to minimize the overhead of handling large numbers of connections and to maximize the throughput and responsiveness of the server.

- Efficient data structures: In order to manage large numbers of connections efficiently, many applications use specialized data structures that are optimized for high throughput and low latency. These might include hash tables, bloom filters, and other algorithms that are designed to quickly look up and process large numbers of connections.

- Asynchronous I/O: Many modern applications use asynchronous I/O techniques, such as epoll and AIO, to minimize the overhead of managing large numbers of connections. These techniques allow the application to process multiple connections simultaneously without blocking on I/O operations, which can improve the responsiveness and throughput of the application.

- Hardware acceleration: Some servers use hardware acceleration, such as offloading network processing to dedicated network interface cards (NICs), in order to handle large volumes of traffic more efficiently.
## bufferbloat
- In a network, data is transmitted in packets, which are stored in buffers at various points in the network until they can be forwarded to their destination. If the buffers are too large, they can cause packets to be delayed and increase latency in the network, resulting in poor performance for users.
- To address bufferbloat, various techniques have been developed, including active queue management (AQM) algorithms, such as CoDel and PIE, that can help to reduce the size of buffers and prevent excessive queuing of packets. In addition, Quality of Service (QoS) mechanisms can be used to prioritize certain types of traffic and prevent the bufferbloat phenomenon from negatively affecting real-time applications, such as voice and video.
## Receive packet steering (RPS)
- The main purpose of RPS is to improve the scalability and performance of network packet processing in multi-core systems by distributing incoming packets across multiple CPU queues or cores. This can help to avoid bottlenecks and improve parallelism, and can be especially useful in high-bandwidth or high-throughput scenarios.
- However, RPS can also introduce overhead and contention, especially if the CPU queues or cores are not evenly loaded or if there is a high degree of contention for shared resources such as memory or network buffers. In some cases, this can lead to increased latency, lower throughput, or even lower CPU utilization than a single-queue or single-core system.
- To mitigate these issues, there are several techniques that can be used in conjunction with RPS, such as receive flow steering (RFS), which can help to further distribute incoming packets across multiple CPU cores or threads based on their flow or connection characteristics, and RSS (receive-side scaling), which can help to balance incoming traffic across multiple NIC queues.
## Generic Receive Offload (GRO)
- When a network interface receives a large packet, GRO can group the individual packets that make up the large packet into a single buffer or "segment" in the kernel memory. This can help to reduce the number of packets that need to be processed and passed up the networking stack, and can also reduce the amount of memory required to store the individual packets.
- GRO can be especially useful for high-bandwidth or high-throughput scenarios where the network interface is receiving a large number of packets, such as in data center or cloud environments. By reducing the amount of CPU and memory overhead required for packet processing, GRO can help to improve the scalability and performance of the networking stack, and can help to avoid bottlenecks and contention.
- Other related features of the networking stack include Generic Segmentation Offload (GSO), which can perform a similar function for outgoing packets, and Large Receive Offload (LRO), which can perform a similar function at the network interface hardware level.
- fragmentation of IP packet vs GRO
  - The fragmentation of IP packets at the IP layer is a different operation than the grouping of IP packets into a single buffer or "segment" by GRO. Fragmentation is used when a network packet is too large to be transmitted over the network in a single packet, so it is divided into smaller fragments that can be transmitted and reassembled at the receiving end.

  - On the other hand, GRO is used when a large network packet is transmitted as a series of smaller IP packets that can be processed individually by the networking stack. GRO groups these individual IP packets into a single buffer or "segment" in the kernel memory, which represents the original, larger network packet that was transmitted.
## HTTP persistent connections
- HTTP persistent connections allow multiple HTTP requests to be sent over a single TCP connection, without the need to establish a new connection for each request. This can improve the performance of web applications by reducing the overhead of connection establishment.
## Persistent TCP connections
- Persistent TCP connections, also known as keep-alive connections, are a technique used in web applications to improve the performance and efficiency of client-server communication.

- When a client makes an HTTP request to a server over a TCP connection, the connection is typically closed after the server sends the response. In a persistent TCP connection, the connection is kept open after the response is sent, allowing for additional requests to be sent over the same connection without t`he overhead of connection establishment.
- Yes, Linux does close idle TCP connections by default. The exact behavior can be configured using the tcp_keepalive_* settings in the /proc/sys/net/ipv4 directory. These settings allow you to control the interval at which keepalive packets are sent, as well as the number of times the system should retry sending the keepalive packet before closing the connection.

- By default, the system will send a keepalive packet after 2 hours of inactivity. If no response is received, the system will try again 5 times at 1 minute intervals before giving up and closing the connection. These values can be changed by modifying the appropriate settings in the /proc/sys/net/ipv4 directory.
- In Linux, you can use the keepalive option in the setsockopt() system call to enable keep-alive packets on a TCP socket. This option allows you to specify the duration of the keep-alive period, the number of keep-alive packets to be sent, and the interval between them.
  - Create a socket using the socket() system call.
  - Set the SO_KEEPALIVE option using the setsockopt() system call.
  - Specify the duration, interval, and count of the keep-alive period using the TCP_KEEPIDLE, TCP_KEEPINTVL, and TCP_KEEPCNT options, respectively.
## TCP Fast Open
- TCP Fast Open (TFO) is a protocol extension for the Transmission Control Protocol (TCP) that allows for faster connection establishment and data transfer between a client and a server.

- With traditional TCP, the three-way handshake (SYN, SYN-ACK, ACK) is required to establish a connection between a client and a server. With TFO, data can be sent in the initial SYN packet, allowing for data transfer to begin before the handshake is completed. This can reduce the latency and time-to-first-byte (TTFB) of a connection, improving the overall performance of the application.
- 
# Related commands
## know the nic information
- ethtool -i eth0
- TC
  - tc qdisc add dev eth0 ingress
  - tc filter add dev eth0 ingress protocol ip parent ffff: u32 match ip src 192.168.0.0/24 flowid 1:1
  - tc qdisc add dev eth0 root handle 1: cbq avpkt 1000 bandwidth 100mbit
  - tc class add dev eth0 parent 1: classid 1:1 cbq bandwidth 100mbit rate 10mbit allot 1500 prio 5 avpkt 1000

- iptables
  - iptables -A INPUT -p tcp --dport 22 -m limit --limit 3/second -j ACCEPT

# Hardware
## multi-queue NIC vs multi-channel NIC
- A multi-channel NIC (network interface card) is a NIC that has multiple physical interfaces or channels, typically on separate PCI or PCIe lanes. This can allow for greater bandwidth and increased network throughput by spreading the traffic across multiple channels. Each channel may have its own MAC address and may be associated with a different IP address or network interface.

- A multi-queue NIC, on the other hand, is a NIC that has multiple transmit and/or receive queues within a single physical interface. This allows for improved scalability and performance in multi-core systems, as different queues can be assigned to different processor cores to avoid contention and maximize parallelism. Each queue may have its own buffer, packet filter, or traffic classification mechanism, and may be associated with a different priority or quality of service (QoS) level.
