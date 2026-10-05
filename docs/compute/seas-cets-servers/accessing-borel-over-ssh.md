---
title: "Accessing Borel over SSH"
stage: "Data Analytics"
roles: [analyst, pipeline]
order: 2
---

# Accessing Borel over SSH

!!! abstract "What this page tells you"
    Step-by-step to reach Borel: enroll in Duo two-step, connect to Global Protect VPN if off AirPennNet, ssh PennKey@borel.seas.upenn.edu, enter PennKey password and Duo option, then cd to CNT directories (/users/pennkey, /tools, /projects, /data, /cache).

## ssh into borel

PREREQUISITE: You must be enrolled in University Two-Step Verification service and Duo. 
Check your enrollment here: [https://twostep.apps.upenn.edu/](https://twostep.apps.upenn.edu/)

### 1\. Connect to the University VPN client (Global Protect) with your PennKey and password (if not on AirPennNet wifi)
[https://www.isc.upenn.edu/how-to/university-vpn-getting-started-guide](https://www.isc.upenn.edu/how-to/university-vpn-getting-started-guide)
Open 

### 2\. SSH into borel

```plain
ssh PennKey_Username@borel.seas.upenn.edu
```

### 3\. Enter your PennKey password

### 4\. Enter the Duo option that you wish to use
This may only be required the first time you login: 
Duo two-factor login for PennKey\_Username
Enter a passcode or select one of the following options:

 (ex)  1. Duo Push to phone\_push (iOS)…6. Passcode or option (1-6):

 After entering your password, your prompt will show PennKey@borel, but you will be in your SEAS general home directory, NOT your CNT home directory. See Step 5 to navigate to your home directory.
_future instructions: (public SSH key to the authorized\_keys file for your account, but I'm working on those step by step instructions)_

### 5\. Navigate to CNT directories in borel
The following directories are available to use for the CNT. Please read through the "Migration to Leif + new server system" page in the "SEAS - Borel, Pioneer, Leif" folder for an orientation before using these directories.

```plain
cd /users/pennkey
cd /tools/
cd /projects/
cd /data/
cd /cache/
```
