# Day 3 — Linux Processes

> **Topics:** `ps` · `top` · background jobs · process states · signals · `kill`

---

## Table of Contents

1. [What is a process?](#1-what-is-a-process)
2. [Listing processes using `ps`](#2-listing-processes-using-ps)
3. [Monitoring processes using `top`](#3-monitoring-processes-using-top)
4. [Running processes in the background](#4-running-processes-in-the-background)
5. [Process states in Linux](#5-process-states-in-linux)
6. [Terminating processes using `kill`](#6-terminating-processes-using-kill)
7. [Why this matters for deployment and Kubernetes](#7-why-this-matters-for-deployment-and-kubernetes)
8. [Quick command reference](#8-quick-command-reference)

---

## 1. What is a process?

A **process** is a running instance of a program.

Examples:

- A Python script running in the terminal
- A FastAPI application
- PostgreSQL
- Docker background services

Every process has a **PID (Process ID)**, which identifies it while it is running.

---

## 2. Listing processes using `ps`

### Basic process listing

```bash
ps
```

By default, `ps` displays processes associated with my current terminal.

Useful variations:

```bash
ps -a    # Processes associated with terminals, excluding session leaders
ps -e    # All processes on the system
```

Some important processes I observed:

| Process      | Purpose                                    |
| ------------ | ------------------------------------------ |
| `systemd`    | System and service manager (usually PID 1) |
| `dockerd`    | Docker daemon                              |
| `containerd` | Container runtime                          |
| `sshd`       | SSH server                                 |
| `bash`       | Shell                                      |

> The `ps` command itself can appear in its own output because it is also a running process.

### Inspecting a particular process

```bash
ps -p 2078
```

`-p` filters the output using the specified PID.

```bash
ps -p 2078 -f
```

`-f` requests a **full-format** listing.

Important columns:

| Column | Meaning                              |
| ------ | ------------------------------------ |
| UID    | User running the process             |
| PID    | Process ID                           |
| PPID   | Parent Process ID                    |
| C      | CPU utilisation indicator            |
| STIME  | Process start time                   |
| TTY    | Terminal associated with the process |
| TIME   | Total CPU time consumed              |
| CMD    | Command that started the process     |

Another format:

```bash
ps -p 2078 -l
```

`-l` provides a **long-format** listing with additional scheduling and process-state information.

### Selecting specific columns

```bash
ps -p 2090 -o pid,stat,cmd
```

`-o` lets us choose which columns to display:

- `pid` — Process ID
- `stat` — Process state
- `cmd` — Command

> **Important:** Column names must be comma-separated, without spaces.

---

## 3. Monitoring processes using `top`

```bash
top
```

`top` is a **live process monitor**. It refreshes periodically and helps monitor CPU and memory consumption.

Important columns:

| Column | Meaning                         |
| ------ | ------------------------------- |
| PID    | Process ID                      |
| USER   | User running the process        |
| PR     | Scheduling priority             |
| NI     | Niceness value                  |
| VIRT   | Virtual memory                  |
| RES    | Physical RAM currently occupied |
| SHR    | Shared memory                   |
| %CPU   | CPU usage                       |
| %MEM   | Percentage of RAM used          |
| TIME+  | Total accumulated CPU time      |

Useful keys inside `top`:

| Key | Action                |
| --- | --------------------- |
| `P` | Sort by CPU usage     |
| `M` | Sort by memory usage  |
| `q` | Quit                  |

To monitor only one process:

```bash
top -p 2067
```

This is useful when I want to watch a specific application instead of all processes.

---

## 4. Running processes in the background

I created a Python process that sleeps for 300 seconds:

```bash
python3 -c "import time; time.sleep(300)" &
```

Understanding the command:

- `python3` — Starts Python
- `-c` — Executes the supplied Python code
- `time.sleep(300)` — Keeps the program alive while sleeping
- `&` — Runs the process in the background

Linux prints something like:

```text
[1] 2078
```

- `1` is the **shell job number**
- `2078` is the **process ID**

The PID is used with commands such as `ps` and `kill`.

---

## 5. Process states in Linux

A process isn't always actively executing. Linux tracks its current state.

| State | Meaning                                             |
| ----- | --------------------------------------------------- |
| `R`   | Running or ready to run                             |
| `S`   | Interruptible sleep — waiting for something         |
| `D`   | Uninterruptible sleep — commonly waiting for I/O    |
| `T`   | Stopped or suspended                                |
| `Z`   | Zombie — finished, but not yet reaped by its parent |

### Experiment 1: Sleeping process

I ran:

```bash
python3 -c "import time; time.sleep(300)" &
```

Then inspected it:

```bash
ps -p 2090 -o pid,stat,cmd
```

Output:

```text
PID   STAT  CMD
2090  S     python3 ...
```

The process state was `S`.

This makes sense because Python was waiting for its timer to finish. The process was alive but not actively using the CPU.

### Experiment 2: CPU-intensive process

I ran a Python loop for 30 seconds:

```bash
python3 -c "import time; end=time.time()+30; exec('while time.time()<end: pass')" &
```

Then inspected it:

```bash
ps -p 2097 -o pid,stat,%cpu,cmd
```

Output:

```text
PID   STAT  %CPU
2097  R     99.9
```

Observations:

- `R` means running or ready to run
- Around `100% CPU` means the process is consuming approximately one CPU core
- It eventually terminated because the loop was limited to 30 seconds

> **Deployment connection:** A CPU-intensive loop in a FastAPI application can consume an entire CPU core and reduce the capacity available to handle other requests.

---

## 6. Terminating processes using `kill`

Despite its name, `kill` sends a **signal** to a process. It doesn't always forcibly terminate it.

Basic syntax:

```bash
kill <PID>
```

By default, this sends `SIGTERM` (signal 15).

We can specify a signal explicitly:

```bash
kill -15 <PID>
kill -9 <PID>
kill -2 <PID>
```

> Unlike `ps`, the Bash `kill` command does not use `-p` to specify a PID. We provide the PID directly.

### Important Linux signals

| Signal  | Number | Purpose                      |
| ------- | ------ | ---------------------------- |
| SIGINT  | 2      | Interrupt                    |
| SIGKILL | 9      | Force immediate termination  |
| SIGTERM | 15     | Request graceful termination |

### SIGTERM — graceful termination

```bash
kill -15 <PID>
```

This **requests** the process to terminate. The application gets an opportunity to:

- Finish or safely stop ongoing work
- Close database connections
- Flush logs
- Release resources

`SIGTERM` is the default signal sent by `kill <PID>`.

### SIGKILL — forced termination

```bash
kill -9 <PID>
```

This **forcibly** terminates the process.

The process cannot catch or handle `SIGKILL`, so it cannot perform its own cleanup.

> **Rule of thumb:** Prefer graceful termination (`SIGTERM`) whenever possible. Use `SIGKILL` only when necessary.

### SIGINT — interrupt

```bash
kill -2 <PID>
```

This sends an interrupt signal. In my Python experiment, it produced:

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
KeyboardInterrupt
```

Python received the interrupt and exited.

Pressing `Ctrl+C` in a terminal running a foreground process typically sends `SIGINT`.

---

## 7. Why this matters for deployment and Kubernetes

Understanding processes helps me troubleshoot applications running on Linux and inside containers.

- `ps` helps identify whether an application is running
- `top` helps investigate high CPU or memory usage
- Process states provide clues when an application is stuck or waiting
- Signals control how processes are stopped
- Kubernetes commonly sends `SIGTERM` when shutting down a container, allowing the application time to shut down gracefully
- If the application doesn't exit within the configured grace period, Kubernetes can force termination

---

## 8. Quick command reference

| Task                            | Command                          |
| ------------------------------- | -------------------------------- |
| List current-terminal processes | `ps`                             |
| List all processes              | `ps -e`                          |
| Inspect a PID                   | `ps -p <PID>`                    |
| Full process details            | `ps -p <PID> -f`                 |
| Long process listing            | `ps -p <PID> -l`                 |
| Select output columns           | `ps -p <PID> -o pid,stat,cmd`    |
| Live process monitor            | `top`                            |
| Monitor one PID                 | `top -p <PID>`                   |
| Run process in background       | `command &`                      |
| Terminate gracefully            | `kill <PID>` or `kill -15 <PID>` |
| Force termination               | `kill -9 <PID>`                  |
| Send interrupt                  | `kill -2 <PID>`                  |

---

## Day 3 completed ✅

**My learning outcome:** I now understand how to inspect, monitor, identify the state of, and terminate Linux processes. I also understand the difference between graceful and forced termination, which will become important when deploying applications with Docker and Kubernetes.
