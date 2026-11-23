# Linux File Permissions

## 1. Why Permissions Matter

Linux controls who can access files and directories and what actions
they can perform.

Permissions are especially important when deploying applications because
scripts, configuration files, and application processes need appropriate
access.

## 2. Understanding `ls -l`

Command:

``` bash
ls -l test.txt
```

Example output:

``` text
-rw-rw-r-- 1 amith2831 amith2831 0 Nov 17 16:54 test.txt
```

The first field represents file type and permissions.

``` text
-rw-rw-r--
│││ │││ │││
│││ │││ └── Others
│││ └────── Group
│└───────── Owner
└────────── File type
```

### File types

  Symbol   Meaning
  -------- ---------------
  `-`      Regular file
  `d`      Directory
  `l`      Symbolic link

## 3. Three Permission Categories

Linux permissions are divided into three categories:

  Category       Meaning
  -------------- -------------------------------------
  Owner (user)   Owner of the file
  Group          Users belonging to the file's group
  Others         Everyone else

Example:

``` text
-rw-rw-r--
```

-   Owner: Read and write
-   Group: Read and write
-   Others: Read only

## 4. Permission Types

  Permission   Symbol   Meaning                Numeric value
  ------------ -------- ---------------------- ---------------
  Read         `r`      Read file contents     4
  Write        `w`      Modify file contents   2
  Execute      `x`      Execute a file         1

A `-` means that permission is not granted.

## 5. Numeric Permissions

Permissions can be represented using numbers.

Each category gets an independent value calculated by adding the
permission values.

  Number   Combination   Permissions
  -------- ------------- ------------------------
  0        0             None
  1        1             Execute
  2        2             Write
  3        2 + 1         Write + Execute
  4        4             Read
  5        4 + 1         Read + Execute
  6        4 + 2         Read + Write
  7        4 + 2 + 1     Read + Write + Execute

### Example: 640

``` bash
chmod 640 test.txt
```

Breakdown:

  Digit   Category   Permissions
  ------- ---------- --------------
  6       Owner      Read + Write
  4       Group      Read
  0       Others     None

Result:

``` text
-rw-r-----
```

## 6. Changing Permissions with `chmod`

`chmod` stands for change mode.

It modifies file or directory permissions.

Syntax:

``` bash
chmod <permissions> <filename>
```

Examples:

``` bash
chmod 644 file.txt
chmod 755 deploy.sh
chmod 640 config.txt
chmod 750 deploy.sh
```

### Common permission patterns

  Permission   Typical use
  ------------ ------------------------------------------------
  `644`        Regular readable files
  `755`        Executable scripts or directories
  `600`        Private files
  `640`        Files accessible to owner and group
  `750`        Executable files restricted to owner and group

## 7. Execute Permission

A script needs execute permission to be run directly.

Example:

``` bash
chmod 750 deploy.sh
```

Results in:

``` text
-rwxr-x---
```

-   Owner: Read, write, execute
-   Group: Read, execute
-   Others: No permissions

An important distinction:

-   Execute permission on a file allows it to be be executed.
-   Execute permission on a directory allows traversal through that
    directory.

## 8. Useful Commands

  Command                Purpose
  ---------------------- -----------------------------------------
  `ls -l`                View file permissions
  `ls -la`               View permissions including hidden files
  `chmod 644 file.txt`   Change permissions
  `touch file.txt`       Create an empty file
  `whoami`               Display current user
  `groups`               Display groups of current user

## 9. What I Practised

-   Understanding file types and permission categories.
-   Reading permissions using `ls -l`.
-   Understanding owner, group, and others.
-   Converting permission symbols into numeric values.
-   Changing permissions using `chmod`.
-   Understanding why scripts need execute permission.

------------------------------------------------------------------------

**Environment:** Ubuntu 24.04 running inside Colima on macOS.

**Learning goal:** Understand Linux permissions required to safely run
and deploy applications.

