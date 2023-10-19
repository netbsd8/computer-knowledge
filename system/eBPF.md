# Kernel
## Kprobes/Kretprobes
- Entry to / exit from a kernel function
- example:
  - tcp_v4_connect()
- attach to raw socket()
  - by pass data to kernel, but forward to user space directly
- XDP
  - attach_xdp(), bypass kernel
- traffic control
  - Qdisc (queue discipline)
  - TC command based
# bcc framework
- python based
- 