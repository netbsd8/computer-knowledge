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

## Throughput vs Latency
- optimizing for throughput and latency often involves trade-offs, and improving one can sometimes have adverse effects on the other. Here are some considerations and examples of such trade-offs:

- Batch Processing vs. Real-time Processing:

  - Batching: Combining multiple pieces of data or tasks into a single unit for processing can improve throughput by reducing the per-item overhead. However, this can increase latency because data must wait for a batch to be complete before being processed. This is common in data streaming systems.
  - Real-time Processing: Processing data as it arrives can reduce latency, but the overhead of handling each item individually might reduce throughput.
- Buffering and Queuing:

  - Buffering or queuing can improve throughput by allowing systems to handle bursts of data or requests more efficiently. However, the time data spends in buffers or queues increases latency.
- Error Recovery Protocols:

  - Protocols like TCP that provide reliable delivery have mechanisms like retransmission, which ensure data integrity but can introduce latency. On the other hand, protocols like UDP sacrifice reliability (no built-in error recovery) for reduced latency, which might affect throughput if higher layers have to handle errors.
- Network Optimizations:

  - Techniques like Traffic Shaping and Quality of Service (QoS) can prioritize certain types of traffic to reduce their latency. However, this might result in reduced throughput for other, lower-priority traffic.
  - TCP window scaling and large windows can improve throughput significantly on long-distance links but might also introduce some latency due to buffering.
- Jumbo Frames:

  - In networks, using larger frame sizes (jumbo frames) can increase throughput by reducing overhead. However, the serialization delay (time taken to put the frame on the wire) for larger frames is more, which can increase latency slightly.
- Hardware and System Level Optimizations:

  - Parallelism: Increasing parallel processing (like multi-threading or distributing tasks across multiple servers) can improve throughput, but the overhead of coordinating between parallel entities might add latency.
  - Prefetching: Systems might prefetch data in anticipation of it being used, improving throughput. But, if predictions are wrong, it might introduce unnecessary latency.
- Algorithmic and Computational Trade-offs:

  - Some algorithms might be optimized for speed (low latency) but might process fewer items in that time. Conversely, algorithms optimized for high throughput might take longer to process each item.
    - Fast Retransmit: In TCP, instead of waiting for a timeout, fast retransmit quickly resends a packet if out-of-order packets are received, indicating potential packet loss. This mechanism prioritizes low latency in recovering from loss, but excessive fast retransmits could reduce the network's overall throughput.
    - Indexed Searches: Databases can use indices to quickly find the location of data (low latency), but building and maintaining these indices can take time and reduce the overall throughput of data insertions or updates.
  - GRO/LRO (Generic/ Large Receive Offload):

  - In networking, these techniques coalesce multiple smaller packets into larger ones, thereby improving throughput by reducing CPU interrupts. However, they can introduce slight latency as packets are buffered for coalescing.
- In many real-world scenarios, a balance is sought between latency and throughput based on the specific requirements of an application or system. For instance, real-time applications like VoIP or online gaming might prioritize latency, while data-intensive applications like video streaming or file transfers might prioritize throughput.
# millions of connections
- Scaling out: One of the most effective strategies for handling large numbers of connections is to scale out horizontally, by adding more servers to the cluster. This can be accomplished using load balancers and other techniques for distributing traffic across multiple servers. By dividing the workload across multiple servers, each server can handle a smaller number of connections, which reduces the overhead and resource requirements for each server.

- Kernel optimizations: The Linux kernel provides a number of optimizations for improving network performance, such as TCP Fast Open, epoll, and SO_REUSEPORT. These features are designed to minimize the overhead of handling large numbers of connections and to maximize the throughput and responsiveness of the server.

- Efficient data structures: In order to manage large numbers of connections efficiently, many applications use specialized data structures that are optimized for high throughput and low latency. These might include hash tables, bloom filters, and other algorithms that are designed to quickly look up and process large numbers of connections.

- Asynchronous I/O: Many modern applications use asynchronous I/O techniques, such as epoll and AIO, to minimize the overhead of managing large numbers of connections. These techniques allow the application to process multiple connections simultaneously without blocking on I/O operations, which can improve the responsiveness and throughput of the application.

- Hardware acceleration: Some servers use hardware acceleration, such as offloading network processing to dedicated network interface cards (NICs), in order to handle large volumes of traffic more efficiently.
## traffic control (TC) and queueing disciplines (qdiscs)
- TC and qdiscs, are focused on managing how packets are sent on the network (e.g., scheduling, shaping, prioritization) and can also implement active queue management to tackle congestion before it becomes severe.
- Queueing Disciplines in Linux are a set of techniques used to manage network traffic and improve the performance and fairness of the networking stack. Queueing Disciplines are implemented in the Linux kernel's network subsystem and are used to control how packets are buffered, scheduled, and transmitted over the network.

  - First-In-First-Out (FIFO): This is the simplest Queueing Discipline, where packets are transmitted in the order they arrive. This can lead to poor performance and fairness in congested networks, as some flows may dominate the queue and starve other flows.

  - Stochastic Fairness Queueing (SFQ): This is a Queueing Discipline that attempts to provide fairness among flows by dividing packets into multiple queues and scheduling them in a randomized manner. This can help to avoid the problem of queue starvation and provide better performance and fairness in congested networks.

  - Hierarchical Token Bucket (HTB): This is a more advanced Queueing Discipline that allows traffic to be classified into different classes based on certain criteria, such as IP addresses or protocols. Each class can then be given a different amount of bandwidth and latency guarantees, which can help to provide better quality of service (QoS) for different types of traffic.

  - Network Emulation (NETEM): This is a Queueing Discipline that is used for testing and emulation purposes, and allows administrators to introduce various types of network delays, packet losses, and other types of network impairments.
- Ingress: When a packet arrives at a network interface, it is processed by the ingress Queueing Disciplines to determine how it should be buffered and scheduled for processing by the kernel's networking stack. This can include actions such as classification, policing, shaping, and scheduling of the packets based on their type, source, or destination.

- Egress: Once the packet has been processed by the networking stack, it is then transmitted over the network through the egress Queueing Disciplines. These disciplines can be used to apply various policies and mechanisms to control the transmission of packets, such as traffic shaping, congestion control, and bandwidth allocation.
- In a setup with a multiqueue NIC, each hardware queue can have its own instance of a queueing discipline, and these can operate independently. However, it's not "each core has its own qdisc" but rather "each hardware queue has its own qdisc instance."
### bufferbloat
- In a network, data is transmitted in packets, which are stored in buffers at various points in the network until they can be forwarded to their destination. If the buffers are too large, they can cause packets to be delayed and increase latency in the network, resulting in poor performance for users.
- To address bufferbloat, various techniques have been developed, including active queue management (AQM) algorithms, such as CoDel and PIE, that can help to reduce the size of buffers and prevent excessive queuing of packets. In addition, Quality of Service (QoS) mechanisms can be used to prioritize certain types of traffic and prevent the bufferbloat phenomenon from negatively affecting real-time applications, such as voice and video.
## Linux Kernel networking queues
- Queueing Disciplines (qdisc) Buffers:

  - These are the most commonly referred to when discussing Linux traffic control. Each network interface has a qdisc associated with it, which can buffer packets. The default is the pfifo_fast qdisc, but there are many others like HTB, TBF, RED, etc.
- Socket Buffers:

  - As previously mentioned, each socket has send and receive buffers (managed through SO_SNDBUF and SO_RCVBUF options). These are not directly related to traffic control but can impact application-level performance.
- Device (Driver) Queues:

  - When packets are dequeued from the qdisc, they are placed into the device's transmit queue to await transmission by the NIC (Network Interface Card). The depth of this queue can be seen and adjusted using tools like ethtool.
- Backlog Queue:

  - When packets are received from the network, they are initially placed into a per-CPU backlog queue, especially if the packets arrive faster than they can be processed. The kernel periodically processes this backlog to move packets to the appropriate socket receive buffer.
- NAPI (New API) and SoftIRQ Processing:

  - NAPI is designed to improve packet processing efficiency during high traffic. When a lot of packets arrive, the NIC interrupts the CPU less frequently and instead processes packets in batches. These batches can introduce a form of buffering as packets await processing.
- TCP Reordering Queue:

  - In the case of out-of-order TCP segments, the TCP stack will buffer these segments until missing segments arrive, after which it can pass the ordered data up to the application.
- TCP Congestion Window:

  - While not a buffer in the traditional sense, the TCP congestion control algorithm uses a "window" to determine how many packets can be "in flight" (sent but not yet acknowledged). The size of this window can effectively throttle network throughput.
- Network Namespace (netns) Buffers:

  - If using network namespaces for containerization or other purposes, each netns can have its own set of buffers and queues.
- Bridging & Switching Buffers:

  - If the kernel is configured to act as a bridge or switch, there can be additional buffers associated with that functionality.
- Tunnels and VPNs:

  - Tunneling protocols or VPNs operating at the kernel level might have their own buffering mechanisms.
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

### multi-queue
- A multi-queue NIC, on the other hand, is a NIC that has multiple transmit and/or receive queues within a single physical interface. This allows for improved scalability and performance in multi-core systems, as different queues can be assigned to different processor cores to avoid contention and maximize parallelism. Each queue may have its own buffer, packet filter, or traffic classification mechanism, and may be associated with a different priority or quality of service (QoS) level.
- RSS:
  - The traffic that goes from the wire to the kernel can be spread into different queues, using a mechanism called RSS - Receive Side Scaling.
  - This mechanism assumes some hash function, that performs calculations based on packet parameters, and sends the packet to relevant queue: ethtool -l ens5f0
  - Assuming that the hashing is fair, it splits the traffic based on the SMAC, DIP/SIP and TCP/UDP port numbers.
  - When the OS maps the interrupts, it allocates interrupt request to each rx queue: ethtool -g ens5f0
  - always have one interrupt mapped to single core: echo 0xff >  /proc/irq/219/smp_affinity
## Offload
### GRO/LRO: Generic Receive Offload
- Reason:
  - with the heaviest bag of all being the 1500-byte maximum transfer unit (MTU) limit. With packet size capped at 1500 bytes, a 10G network link running at full speed will be transferring over 800,000 packets per second: 10Gb / (1500B x 8) = 8333 packets. So CPU needs to handle 800k packets/sec.
- When a network interface receives a large packet, GRO can group the individual packets that make up the large packet into a single buffer or "segment" in the kernel memory. This can help to reduce the number of packets that need to be processed and passed up the networking stack, and can also reduce the amount of memory required to store the individual packets.
- GRO can be especially useful for high-bandwidth or high-throughput scenarios where the network interface is receiving a large number of packets, such as in data center or cloud environments. By reducing the amount of CPU and memory overhead required for packet processing, GRO can help to improve the scalability and performance of the networking stack, and can help to avoid bottlenecks and contention.
- Other related features of the networking stack include Generic Segmentation Offload (GSO), which can perform a similar function for outgoing packets, and Large Receive Offload (LRO), which can perform a similar function at the network interface hardware level.
- fragmentation of IP packet vs GRO
  - The fragmentation of IP packets at the IP layer is a different operation than the grouping of IP packets into a single buffer or "segment" by GRO. Fragmentation is used when a network packet is too large to be transmitted over the network in a single packet, so it is divided into smaller fragments that can be transmitted and reassembled at the receiving end.

  - On the other hand, GRO is used when a large network packet is transmitted as a series of smaller IP packets that can be processed individually by the networking stack. GRO groups these individual IP packets into a single buffer or "segment" in the kernel memory, which represents the original, larger network packet that was transmitted.
  - LRO is a bit of a flawed solution, according to Herbert; the real problem is that it "merges everything in sight." This transformation is lossy; if there are important differences between the headers in incoming packets, those differences will be lost. 
  -  In GRO, the criteria for which packets can be merged is greatly restricted; the MAC headers must be identical and only a few TCP or IP headers can differ. In fact, the set of headers which can differ is severely restricted.
  -   there has not been a lot of effort toward using LRO in 1G drivers. In general, current CPUs can keep up with a 1G data stream without too much trouble. There might be a benefit, though, in embedded systems which typically have slower processors.

### TSO/GSO: generic segmentation offload mechanism 
## Receive packet steering (RPS)
- The main purpose of RPS is to improve the scalability and performance of network packet processing in multi-core systems by distributing incoming packets across multiple CPU queues or cores. This can help to avoid bottlenecks and improve parallelism, and can be especially useful in high-bandwidth or high-throughput scenarios.
- However, RPS can also introduce overhead and contention, especially if the CPU queues or cores are not evenly loaded or if there is a high degree of contention for shared resources such as memory or network buffers. In some cases, this can lead to increased latency, lower throughput, or even lower CPU utilization than a single-queue or single-core system.
- To mitigate these issues, there are several techniques that can be used in conjunction with RPS, such as receive flow steering (RFS), which can help to further distribute incoming packets across multiple CPU cores or threads based on their flow or connection characteristics, and RSS (receive-side scaling), which can help to balance incoming traffic across multiple NIC queues.

# Layers
## Ethernet
### [Etherenet header](../pictures/Ethernet_header.png)
### MTU and fragmentation
- MTU (Maximum Transmission Unit) refers to the maximum size of a frame (for Ethernet) or packet (for IP) that can be transmitted over a network link. If the data to be sent exceeds the MTU, it needs to be fragmented to fit.

- IP Layer:
  - IPv4: The total length field in the IPv4 header is 16 bits long, which means the maximum size of an IPv4 packet (including the header) is 2^16 - 1 = 64K

- IPv6: In IPv6, the payload length field is also 16 bits long. This means that the maximum size of the payload (not including the IPv6 header but potentially including upper-layer headers like TCP or UDP) is 65,535 bytes. However, IPv6 introduces a "jumbo payload" option, which can extend this for payloads larger than 65,535 bytes, but its use is not common in typical scenarios.

- TCP Layer:
- For TCP, the constraint is not directly about the "length" of the data, but rather the sequence number space. TCP uses a 32-bit sequence number, which theoretically allows for 2^32 = 4G of data. However, in practice, TCP's "length" or window is constrained by factors like the receive window size, congestion window, and Maximum Segment Size (MSS).

- The MSS is a TCP option that specifies the largest amount of data in bytes that a device can accept in a single non-fragmented TCP segment. It does not include the TCP header length.

- IPv4 Fragmentation: If a packet exceeds the MTU of the outbound link, and the "Don't Fragment" (DF) bit is not set in the packet's header, the IP layer will fragment the packet into smaller chunks that fit the MTU. Each fragment will have its own IP header and will be reassembled at the destination.
  - The kernel knows the MTU (Maximum Transmission Unit) of an outbound link because this value is associated with each network interface on the system. When a network interface (like an Ethernet adapter) is initialized and brought up, it's typically configured with a default MTU, which can then be queried or adjusted through system commands or configuration files.

- IPv6 Fragmentation: IPv6 doesn't support fragmentation by routers in the middle of the network. Hosts are expected to perform Path MTU Discovery (PMTUD) to determine the smallest MTU on the path to the destination and then send packets that fit within that MTU. If necessary, the source host can fragment packets, but routers in the path won't.
  - Path MTU Discovery (PMTUD): This is a mechanism by which devices on the Internet can discover the smallest MTU on the path between two hosts. If a device tries to send a packet that's too large for an intermediary link, it'll receive an ICMP "Fragmentation Needed" message (for IPv4) or "Packet Too Big" message (for IPv6). These messages inform the sending device of the next-hop MTU, allowing it to adjust its packet sizes accordingly.

- TCP and MTU: TCP tries to avoid IP fragmentation by using the MSS, which is typically set based on the MTU of the outbound interface minus the sizes of the IP and TCP headers. If PMTUD determines that an even smaller MTU is needed on the path, the MSS can be adjusted. This is why it's common to see the MSS option negotiated during the TCP three-way handshake.

- If a TCP segment or IP packet is sent that's too large for an intermediary link (and exceeds the MTU), and the DF bit is set (or it's an IPv6 packet), the sender will receive an ICMP "Fragmentation Needed" (for IPv4) or "Packet Too Big" (for IPv6) message. The sender should then adjust the size of the packets it sends.
  - The ICMP "Fragmentation Needed" (for IPv4) or "Packet Too Big" (for IPv6) messages are sent by the router or gateway that encounters the packet which is too large to be forwarded on the next hop due to its MTU constraint.

  - Here's how the process generally works:

    - Encountering Oversized Packet: A router receives a packet intended for forwarding.

    - Checking Against MTU: The router checks the packet's size against the MTU of the outbound interface (the interface the packet would be forwarded through).

    - Decision Based on DF Bit and Packet Size:

    - If the packet size is within the MTU limit, it's forwarded normally.
    - If the packet size exceeds the MTU and the DF (Don't Fragment) bit is set in the IPv4 packet header (or if it's an IPv6 packet, which inherently doesn't support fragmentation by routers), the router cannot fragment and forward the packet.
    - Sending ICMP Message:

      - For IPv4: The router drops the oversized packet and sends back an ICMP "Destination Unreachable" message with a "Fragmentation Needed and DF set" code to the sender. This ICMP message also contains the MTU of the outbound interface, providing the sender with information on the appropriate packet size.
      - For IPv6: The router sends an ICMPv6 "Packet Too Big" message back to the source, also indicating the MTU of the outbound interface.
    - Sender's Kernel Handling of ICMP Message:

      - When the source machine's kernel receives the ICMP message, it updates its Path MTU information for that specific destination. This ensures that subsequent packets to the same destination will adhere to the newly discovered Path MTU.
      - The kernel might also cache this Path MTU information to avoid similar issues in the near future.
      - For TCP traffic, the sender will adjust its Maximum Segment Size (MSS) for that connection based on the new Path MTU. This ensures that subsequent TCP segments (and their resulting IP packets) sent over this connection will fit within the discovered Path MTU.
      - If the original packet was part of a higher-level protocol that supports retransmission (like TCP), the data will be retransmitted in smaller segments that adhere to the updated MSS.
## Jumbo frames:
- "jumbo frames" refer to Ethernet frames that are larger than the standard Maximum Transmission Unit (MTU) of 1,500 bytes. Jumbo frames are used primarily on local area networks (LANs) and data center environments to improve performance, especially for high-throughput applications.
- The typical size of a jumbo frame is 9,000 bytes.
- To use jumbo frames, they must be explicitly enabled on network devices, such as switches and routers, and on the network interfaces of servers and storage devices. Once enabled, the MTU settings on all devices in the path should be adjusted accordingly.
- Reduced Overhead: Larger frames mean that, for a given amount of data, fewer frames need to be sent, which reduces the per-frame overhead.
- Better Throughput: Fewer frames lead to fewer CPU interrupts, allowing for higher data rates and better overall network throughput.
- Efficiency: Jumbo frames are especially beneficial for applications that transfer large amounts of data, like storage area networks (SANs) or certain streaming applications.
- Latency: While throughput can be improved, individual jumbo frames take longer to serialize onto the network, which can introduce a bit more latency.
## IP layer
### [ip heaer](../pictures/IP_header.png)
### longest prefix match
- The Longest Prefix Match (LPM) algorithm is fundamental for IP routing. The goal is to find the route entry with the longest prefix that matches the destination IP address of a packet.

- There are various ways to implement LPM, ranging from simple linear searches to more complex data structures like tries (specifically radix or Patricia tries) and binary search on prefix lengths. 
- Using a Trie (Radix or Patricia Trie):

  - Each node in the trie has child nodes for each possible bit value (0 or 1 for binary tries).
  - Each node can also store information about the route if a route ends at that node.
  - Insertion (Building the Trie):
    - Convert the IP address of the route to its binary representation.
    - Starting from the root, traverse the trie based on the binary value of each bit in the IP address. If the corresponding child node doesn't exist, create it.
    - When the prefix length is reached, store the route information in the current node.
  - Lookup (Finding the Longest Prefix Match):
    - Convert the destination IP address to its binary representation.
    - Start from the root and traverse the trie based on the binary value of each bit in the IP address.
    - Every time you encounter a node with route information, update the "current best match."
    - Continue traversing until you either reach the end of the IP address or hit a point in the trie where there is no matching child node.
    - The last route information you encountered is the longest prefix match.

`
function longestPrefixMatch(trie, ipAddress):
    currentNode = trie.root
    bestMatch = null

    for each bit in ipAddress:
        if currentNode has route information:
            bestMatch = currentNode.route

        if bit is 1 and currentNode has a child node for 1:
            currentNode = currentNode.child[1]
        else if bit is 0 and currentNode has a child node for 0:
            currentNode = currentNode.child[0]
        else:
            break

    return bestMatch
`
### Anycast
- Multiple Servers with the Same IP Address: In an anycast setup, multiple servers (potentially spread across different geographic locations) are configured with the same IP address. This means that when different parts of the internet try to access this IP address, they might reach different actual servers.
- BGP (Border Gateway Protocol): The backbone of anycast is BGP, the protocol used for routing traffic between different networks on the internet.
  - Each server in an anycast setup announces its presence to the internet using BGP. It tells its neighboring networks: "Hey, I'm the closest server with IP address X.X.X.X".
  - The BGP routers, in turn, propagate this announcement to other routers.
- Route Selection: When a user sends a packet to an anycast IP address, routers in the user's network will determine the shortest path to one of the servers with that IP address. "Shortest" in this context is based on the BGP path selection process and may involve criteria like the fewest number of network hops or specific routing policies. As a result, the user's request is typically (but not always) routed to the geographically nearest server with the anycast IP. This proximity helps reduce latency.
- Failover and Load Balancing: If an anycast server fails and stops announcing its IP address, routers will automatically redirect traffic to the next closest server. This provides natural load balancing and failover capabilities.
  - Some advanced anycast setups may use additional mechanisms for health checks and more granular load balancing.
- Tuning and Traffic Management:Anycast providers might use traffic engineering techniques to manage and control the distribution of user requests. This can involve tweaking BGP attributes or using other advanced routing features.
- Potential Challenges:
  - One challenge with anycast is that BGP's idea of the "shortest path" might not always align with actual geographic proximity or the lowest latency path. Some tuning and traffic engineering may be required.
  - Another challenge is stateful connections. Anycast works best for stateless protocols where each request and response are independent. For stateful protocols, there's a risk that subsequent packets could, in theory, be routed to different servers, breaking the connection. In practice, this is rare because routing tables in the internet's core are stable most of the time.
- Example: One of the most well-known uses of anycast is in the DNS system. Several of the root DNS servers are anycasted, meaning that while there appears to be a single IP address for a particular root server, there are actually multiple physical servers around the world with that IP address. When your computer queries one of these root servers, it's directed to the nearest instance, ensuring quick response times and high availability.
### BGP vs OSPF
- Scope:
  - BGP (Border Gateway Protocol): BGP is an Exterior Gateway Protocol (EGP), primarily used for routing between different autonomous systems (ASes) on the internet. Each AS is a collection of IP routing prefixes under the control of a single organization that presents a common routing policy to the internet.
  - OSPF (Open Shortest Path First): OSPF is an Interior Gateway Protocol (IGP) designed for use within an individual AS.
- Path Vector vs. Link State:
  - BGP: It's a path vector protocol. It maintains the path information that gets updated dynamically as the route gets updated and prevents loops by checking the AS-path.
  - OSPF: It's a link state protocol. It has a full topological database of the entire network and uses the Shortest Path First (SPF) algorithm to compute the best path to each subnet.
- Route Selection:
  - BGP: Uses multiple attributes for route selection, such as AS_PATH, LOCAL_PREF, MED, etc.
  - OSPF: Uses cost as its metric, which is typically derived from the bandwidth of the link.
- Scalability:
  - BGP: Designed to handle thousands of routes making it suitable for the global internet.
  - OSPF: Divides areas for scalability but has a more comprehensive topological database than BGP, making it less suitable for extremely large networks like the internet.
- Convergence Time:
  - BGP: Typically has slower convergence than OSPF.
  - OSPF: Generally, it converges faster than BGP.
- Policy vs. Topology:
  - BGP: It's more policy-driven, allowing administrators to influence routing decisions based on policies, making it flexible for the diverse policy requirements of the internet.
  - OSPF: It's more topology-driven, aiming to always select the shortest path based on its metric.
- Flexibility:
  - BGP: Offers more granularity and flexibility in terms of traffic engineering, path selection, and route manipulation due to its rich set of attributes.
  - OSPF: While OSPF can also offer traffic engineering, especially in its version for MPLS (OSPF-TE), BGP provides a broader set of tools and is more flexible in heterogeneous environments.
- Addressing:
  - BGP: Supports both IPv4 and IPv6 through separate address families.
  - OSPF: Has distinct versions for IPv4 (OSPFv2) and IPv6 (OSPFv3).

### link state vs path vector 
- Link-State Routing Protocols:
  - Examples: OSPF (Open Shortest Path First), IS-IS (Intermediate System to Intermediate System)
  - How they work:
    - Discovery: Every router discovers its neighbors and establishes a two-way communication with them.
    - Topology Database: Each router creates a topology database or link-state database, which is a map of the entire network in terms of its routers and their connecting links.
    - Distribution: When a change occurs in the network topology, a link-state advertisement (LSA) is created and flooded throughout the network. Each router then updates its topology database with this new information.
    - Calculation: Using the topology database, each router independently calculates the best path to every network using the Shortest Path First (SPF) algorithm. This results in a tree with the router at its root and the shortest path to each network as its branches.
  - Advantages:
    - Predictable and relatively fast convergence times.
    - Because they maintain a view of the entire network topology, they can make more informed routing decisions.
  - Disadvantages: In very large networks, the link-state database can become large, leading to more memory usage and longer SPF calculation times.
- Path-Vector Routing Protocols:
  - Example: BGP (Border Gateway Protocol)
  - How they work:
    - Path Information: Instead of maintaining detailed topology data like link-state protocols, path-vector protocols maintain the path information to reach the destination network. This path is a list of all the autonomous systems (ASes) the route has traversed.
    - Loop Prevention: Loops are avoided by examining the AS path. If a router sees its own AS number in the path, it knows there's a loop.
    - Policy-Based: BGP heavily relies on policies and rule sets defined by the administrator. Routes can be manipulated, filtered, and selected based on an extensive set of criteria, including but not limited to the AS path.
  - Advantages:
    - Highly scalable. While BGP is known for its complexity and extensive configuration options, it's designed to handle thousands of routes, making it suitable for the global internet.
    - Flexibility in route selection and traffic engineering due to a rich set of attributes.
  - Disadvantages:
    - Convergence might be slower compared to link-state protocols.
    - Complexity in configuration and policy definition.
- In summary:
    - Link-State protocols have a complete view of the network and use algorithms like SPF to find the shortest path.
    - Path-Vector protocols, on the other hand, don't have a detailed map of the network. Instead, they know the paths to reach various networks and use policies to make routing decisions.
## TCP/UPD layer
### [TCP header](../pictures/TCP_header.png)
### [UDP header](../pictures/UDP_header.png)
### TCP Congestion Control
- While cwnd (congestion window) is a sender-side control mechanism influenced by perceived network congestion, the TCP sender must also respect the rwnd (receiver window), which is advertised by the receiver. The rwnd indicates how much buffer space the receiver has available for incoming data. The actual amount of data the sender can transmit is the minimum of the two windows: cwnd and rwnd.
- The ssthresh (slow-start threshold) is a central concept in TCP's congestion control mechanism. When the congestion window (cwnd) is below ssthresh, the connection is in the "Slow Start" phase, where the window grows exponentially. When cwnd is above ssthresh, the connection is in the "Congestion Avoidance" phase, where the window growth becomes more conservative (typically linear). nitially, ssthresh is not based on any measurement of the network's actual capacity or current load. Instead, its initial large value simply facilitates the Slow Start process. As the connection progresses and experiences network conditions (like packet loss), ssthresh gets adjusted dynamically to adapt to perceived network congestion.
- Slow Start:

  - Objective: Increase the transmission rate rapidly to quickly utilize available bandwidth.
  - Operation: The sender starts with a congestion window (cwnd) of typically one or two segments. For each ACK received, the cwnd is increased by one segment (effectively doubling the window every round-trip time (RTT) until a threshold, ssthresh (slow start threshold), is reached or packet loss is detected.
  - If the cwnd exceeds ssthresh or if packet loss occurs, TCP transitions to the Congestion Avoidance phase.
- Congestion Avoidance:

  - Objective: Increase the transmission rate, but more conservatively than in Slow Start to avoid congestion.
  - Operation: Once cwnd exceeds ssthresh, for every ACK received, cwnd is increased by 1/cwnd (Additive Increase). This leads to a linear growth of cwnd instead of the exponential growth seen in Slow Start.
- If packet loss is detected, ssthresh is set to half of the current cwnd value, and cwnd is reset to its initial value, and TCP reenters Slow Start. If a timeout occurs, it's an indication of potential severe congestion.
- Fast Retransmit:

  - Objective: Quickly recover from a lost segment.
  - Operation: Instead of waiting for a timeout to detect a lost segment, TCP detects loss using duplicate ACKs. If a sender receives three duplicate ACKs (three ACKs acknowledging the same segment, indicating that subsequent segments are missing), it assumes that a segment has been lost and immediately retransmits the missing segment without waiting for a timeout. This mechanism speeds up loss recovery.
- Fast Recovery:

  - Objective: Resume transmission at a moderate rate after a Fast Retransmit.
  - Operation: After Fast Retransmit retransmits the lost segment, rather than dropping back into Slow Start, TCP goes into Fast Recovery. In this phase, the cwnd is halved (which also sets the new ssthresh), and then for each duplicate ACK received, the cwnd is incremented by one segment. When a non-duplicate ACK is received (indicating that the missing segments have been received, and the receiver has moved on), TCP exits Fast Recovery and goes back to Congestion Avoidance.