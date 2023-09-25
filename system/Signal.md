# Types
## SIGHUP
- The SIGHUP signal, short for "Signal Hang Up," is a signal used in Unix-like operating systems to notify a process that the controlling terminal or session has been disconnected or terminated. Historically, it was used to instruct processes to reload their configuration files or restart. Here's when and how to use the SIGHUP signal:

  - Terminal Hang-Up: The primary use of SIGHUP is to inform processes that they should terminate or reset because their controlling terminal has been disconnected. For example, when a user logs out of a terminal session, processes associated with that session may receive a SIGHUP signal.
  - Configuration Reload: Some daemons and long-running processes are designed to reload their configuration files when they receive a SIGHUP signal. Instead of stopping and restarting the process, which could cause service interruption, SIGHUP is used to trigger a graceful reconfiguration.
  - Log Rotation: In the context of log management, SIGHUP is often used to signal processes like syslogd or logrotate to close and reopen log files. This helps in log rotation and prevents log files from growing indefinitely.
  - Custom Application Use:In some cases, SIGHUP can be used within custom applications to trigger specific actions. For example, you might implement a SIGHUP handler in your application to reload an internal configuration or perform other maintenance tasks.
  - How to Send a SIGHUP Signal: To send a SIGHUP signal to a running process, you can use the kill command with the -HUP option, followed by the process ID (PID) of the target process.
## SIGCHLD:
- The kernel sends the SIGCHLD signal to the parent process of the terminated child. This signal informs the parent that one of its child processes has terminated.
