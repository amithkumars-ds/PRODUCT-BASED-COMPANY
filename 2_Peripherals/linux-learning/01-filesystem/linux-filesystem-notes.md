# Linux Filesystem Fundamentals

## 1. Linux Directory Structure

Linux uses a single hierarchical filesystem that starts at the root
directory `/`.

Unlike Windows, Linux doesn't use separate drive letters such as `C:` or
`D:`.

  Directory    Purpose
  ------------ ------------------------------------------------------------
  `/`          Root of the filesystem
  `/home`      Home directories of regular users
  `/root`      Home directory of the root user
  `/etc`       System and application configuration
  `/var`       Variable data, including logs
  `/var/log`   System and application logs
  `/tmp`       Temporary files
  `/usr`       User applications, libraries and utilities
  `/bin`       Essential user commands
  `/dev`       Device files
  `/proc`      Virtual filesystem exposing process and kernel information

## 2. Navigation Commands

  Command      Purpose
  ------------ --------------------------------------
  `pwd`        Print current working directory
  `ls`         List directory contents
  `ls -l`      Show detailed file information
  `ls -la`     Include hidden files
  `cd /`       Navigate to root
  `cd /home`   Navigate using an absolute path
  `cd ..`      Move to parent directory
  `cd ~`       Navigate to current user's home
  `cd`         Also navigate to current user's home

## 3. Absolute vs Relative Paths

### Absolute path

Starts from the root `/`.

Example:

``` bash
cd /var/log
```

This works regardless of the current directory.

### Relative path

Interpreted from the current working directory.

Example:

``` bash
cd ../../var/log
```

This moves up two directories and then enters `var/log`.

## 4. Home Directory and Environment Variables

The `~` symbol represents the current user's home directory.

The `$HOME` environment variable stores that directory's path.

Useful commands:

``` bash
echo $HOME
cd ~
pwd
```

In our Colima VM, the home directory is `/home/amith2831.guest`.

## 5. Creating and Viewing Files

  Command                    Purpose
  -------------------------- ------------------------------------------
  `mkdir folder`             Create a directory
  `touch file.txt`           Create an empty file if it doesn't exist
  `cat file.txt`             Display file contents
  `echo "text"`              Print text
  `echo "text" > file.txt`   Write text, replacing existing contents
  `nano file.txt`            Edit a file in the terminal

## 6. Important Concepts

-   Linux paths use `/` as the directory separator.
-   Hidden files usually begin with a `.`.
-   `ls -a` displays hidden files.
-   `/etc` commonly contains configuration files.
-   Directories ending in `.d` commonly contain configuration fragments.
-   `/var/log` contains system and application logs.
-   `/proc` exposes live process and kernel information.

## 7. What I Practised

-   Navigating the Linux filesystem.
-   Understanding the root directory.
-   Exploring important system directories.
-   Using absolute and relative paths.
-   Understanding the home directory.
-   Creating directories and files.
-   Reading and editing files.

------------------------------------------------------------------------

**Environment:** Ubuntu 24.04 running inside Colima on macOS.

**Learning goal:** Build the Linux fundamentals required to deploy and
operate containerized ML applications using Kubernetes.

