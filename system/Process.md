# Process Types
## Process 0
- The operating system kernel identifies each process by its process identifier. Process 0 is a special process that is created when the system boots; after forking a child process (process 1), process 0 becomes the swapper process (sometimes also known as the “idle task”). Process 1, known as init, is the ancestor of every other process in the system.
- When using systemd as the init system, systemd takes the place of the traditional init process. So systemd is the first process started at boot time, and it has PID 1.
### init process
- Starting essential system services - init sets up basic system services like udev, crond, network services, etc. required early in the boot process.
- Managing runlevels/targets - init handles switching between runlevels/targets which determine what processes and services are started in different system modes.
- Process monitoring - init continually monitors and reaps orphaned child processes to prevent zombies.
- System shutdown/reboot - init coordinates the proper shutdown and reboot of the system when requested.
- Respawning crashed processes - init can be configured to restart crashed or failed processes like daemons.
- Running shell scripts - Executing init scripts at specific runlevels to start/stop additional services.
- Changing process states - init can signal processes to reload, restart, etc.
- Troubleshooting - Outputs logging and diagnostic messages to help troubleshoot boot issues.
- User communicaotion - Informs users of system state changes like shutdown/reboot.
- No user session
  - No Controlling Terminal: The init process is typically started during system initialization and is not associated with any specific terminal. It doesn't interact with users directly, so it doesn't need a controlling terminal.
  - No Terminal Session: Terminal sessions are created when users log in and start a shell or other interactive processes. The init process is not part of any user session and doesn't create sessions.
  - No Process Group: While the init process creates and manages other processes during system startup and shutdown, it doesn't create or belong to a specific process group related to user sessions.
## Parent vs Child
## Orphan
- An orphan process is a computer process whose parent process has finished or terminated, though it remains running itself.
- In a Unix-like operating system any orphaned process will be immediately adopted by the special initsystem process. This operation is called re-parenting and occurs automatically. Even though technically the process has the initprocess as its parent, it is still called an orphan process since the process that originally created it no longer exists.
- To help avoid accidentally leaving orphaned processes, the shells in Unix-like systems use process groups. All processes started from the shell become part of the shell's process group. When the shell detects that the parent process has exited, it sends a SIGHUP signal to all processes in the process group, which will cause them to terminate gracefully. This prevents them from continuing to run as unmanaged orphan processes.
## Daemon
- In a Unix environment, the parent process of a daemon is often, but not always, the init process. A daemon is usually created by a process forking a child process and then immediately exiting, thus causing init to adopt the child process. In addition, a daemon or the operating system typically must perform other operations, such as dissociating the process from any controlling terminal (tty). Such procedures are often implemented in various convenience routines such as daemon(3) in Unix.
- No Controlling Terminal:
  - Daemon processes are usually designed to run in the background without any direct interaction with a controlling terminal. Unlike interactive or foreground processes, daemons do not attach to a terminal, and they do not have a controlling terminal associated with them.
  - This means that daemons are not influenced by terminal events like terminal hang-up (SIGHUP) or user input.
- Detached from Terminal Sessions:
  - Daemons are typically designed to be detached from any terminal session. They are not part of any session, and they do not create or join process groups associated with terminal sessions.
  - This independence from terminal sessions ensures that daemons can continue running even if the user logs out or closes the terminal.
- No Job Control:
  - Daemons are not subject to job control mechanisms used for interactive processes. They are not stopped or suspended with Ctrl+Z, and they do not respond to job control commands like fg or bg.
- Forking and Double Forking:
  - Many daemons are created through a process known as "forking" or "double forking." This involves the daemon process creating a child process and then exiting, leaving the child process to continue running independently.
  - The double forking process helps disassociate the daemon from the parent process and ensures that it is not connected to any terminal session.
- Logging and Output:
  - Since daemons do not have a controlling terminal, they typically log their output to log files or other designated locations. They do not rely on standard input/output streams like terminal-based processes.
- Signal Handling:
  - Daemons may have custom signal handlers to respond to specific signals, such as reloading their configuration or gracefully shutting down. They can choose how to handle signals based on their specific requirements.
## Zombin
-  zombie process or defunct process is a process that has completed execution but still has an entry in the process table. This entry is still needed to allow the parent process to read its child’s exit status. In the term’s metaphor, the child process has “died” but has not yet been “reaped”. Also, unlike normal processes, the kill command has no effect on a zombie process.
- When a process ends, all of the memory and resources associated with it are deallocated so they can be used by other processes. However, the process’s entry in the process table remains. The parent can read the child’s exit status by executing the wait system call, whereupon the zombie is removed. The wait call may be executed in sequential code, but it is commonly executed in a handler for the SIGCHLD signal, which the parent receives whenever a child has died.
- After the zombie is removed, its process identifier (PID) and entry in the process table can then be reused. However, if a parent fails to call wait, the zombie will be left in the process table.
  - Zombie State: When a process exits, it enters the "zombie" state. In this state, the process is not consuming any system resources except for a small amount of memory to store its exit status and process ID.
  - Parent Process's Responsibility: It is the responsibility of the parent process of the zombie to "reap" or acknowledge its termination. When the parent process does this, the kernel removes the zombie process entry from the process table, freeing up any associated resources.
  - Wait System Call: The parent process usually calls the wait() or waitpid() system call to retrieve the exit status of its child process (the zombie). This call also reaps the zombie.
  - Kernel Cleanup: When the wait() or waitpid() call is made by the parent process, the kernel cleans up the zombie process entry, and it is removed from the process table. At this point, the process is completely gone.
# Other related Topics
## terminal : text input/output devices
### controlling terminal:
- A controlling terminal is a terminal device that is associated with a specific process group. The controlling terminal provides a means for processes to interact with a user or communicate with a terminal-like device.

- When a process group is created, one of the terminals (usually the terminal where the process was started) becomes the controlling terminal for that group. All processes in the group share the same controlling terminal.

- The controlling terminal is significant because it can receive signals (such as interrupt signals like Ctrl+C) and input from the user, which are then distributed to all processes in the associated process group.

### terminal session:
- A terminal session refers to a collection of processes that share a common controlling terminal. These processes typically include a shell process and any other processes launched from that shell.

- When you log in to a Unix-like system, you typically start a new terminal session. This session includes the shell that you interact with, and any processes you launch from that shell are part of the same session.

- Terminal sessions provide a way to group related processes together and manage their interactions with the terminal. For example, when you log out, all processes in your terminal session are typically sent a SIGHUP signal to notify them that the terminal is being hung up, which often results in their termination.
### process group:
- Job Control: 
  - Process groups are a fundamental part of job control in Unix-like systems. They allow you to manage and manipulate groups of processes as a single unit. This is particularly useful for controlling foreground and background jobs, suspending and resuming processes, and managing the flow of data between processes.
- Signal Handling:
  - Process groups are essential for signal handling. For example, when you send a signal to a process group, the signal is delivered to all processes within that group. This is useful for scenarios like sending a Ctrl+C (SIGINT) signal to terminate a group of related processes.
- Session Management:
  - Process groups are organized into sessions. A session is a collection of one or more process groups. A session typically starts with a terminal login and includes all the process groups associated with that login session.
- Daemon Process Management:
  - Process groups are used to manage daemon processes (background processes that run independently of terminal sessions). Daemons often create their own process groups to isolate themselves from terminal sessions.
### job control:
- Job Control:
  - Job control is a set of features provided by Unix-like operating systems to manage and control the execution of processes (jobs) in a terminal session.
  - Job control allows users to:
    - Start and manage multiple processes from a single terminal session.
    - Suspend (pause) and resume processes.
    - Move processes between the foreground and background.
    - Terminate processes selectively.
- Foreground Job:
  - A foreground job is a job that is currently running in the active terminal session, and it typically receives input and output directly from the user.
  - When you run a command in the foreground (e.g., ls or gcc), it starts as a foreground job, and its output is displayed in the terminal. The terminal is often "locked" to the foreground job until it completes or is suspended.
- Background Job:
  - A background job is a job that is running independently of the terminal session. It does not lock the terminal, allowing you to continue entering commands and interacting with other processes.
  - You can start a background job by appending an ampersand & to a command (e.g., command &). The command runs in the background, and you regain control of the terminal immediately.
- Job Control Commands:
  - jobs: Lists the jobs in the current terminal session, including their status (running, stopped, etc.).
  - fg: Brings a background job to the foreground. You can specify a job number or use % followed by the job number.
  - bg: Resumes a stopped background job in the background.
  - Ctrl+C (SIGINT): Sends an interrupt signal to the foreground job, typically terminating it.
  - Ctrl+Z (SIGTSTP): Sends a stop signal to the foreground job, suspending it. You can then use bg or fg to resume or bring it to the foreground.
# Process Management
## Job Control vs Process Scheduling
- Job Control:
  - User-Initiated: Job control is primarily initiated and managed by users within a terminal session. Users can start, stop, background, and foreground processes at their discretion using terminal commands and control key sequences.
  - User-Centric: It is user-centric, meaning that it provides users with the ability to interactively manage the execution of processes in real-time. Users can directly influence the behavior of processes, such as suspending a process with Ctrl+Z or moving it to the background with &.
  - Terminal-Based: Job control is closely tied to the terminal environment. Users interact with processes in the context of a terminal session, and terminal devices (e.g., controlling terminal) play a significant role in sending signals and managing job states.
  - Foreground and Background: Users can place processes in the foreground (where they receive user input and display output to the terminal) or the background (where they run independently of the terminal and don't lock it).

- Process Scheduling by the Kernel:
  - Kernel-Managed: Process scheduling is managed by the operating system kernel. The kernel's scheduler determines which process runs on the CPU and for how long, based on various scheduling algorithms (e.g., round-robin, priority-based).
  - Resource Allocation: The kernel allocates CPU time and system resources to processes based on priority, resource requirements, and other factors. It ensures fair and efficient resource utilization across all running processes.
  - Background Operation: Process scheduling occurs in the background without direct user intervention. Users don't typically have control over the exact timing of process execution or CPU allocation unless they use real-time scheduling features.
  - Efficiency and Fairness: Kernel-level scheduling is designed to provide efficient CPU utilization and fairness among processes, ensuring that no single process monopolizes system resources.
- Relationship:
  - Job control and process scheduling are related because job control commands (e.g., fg, bg, Ctrl+Z) influence the state and scheduling of processes within a terminal session.
  - For example, moving a process to the background effectively allows the kernel's scheduler to allocate CPU time to other processes while the background process runs independently.
