---
title: "Mounting cnt-fs"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 3
---

# Mounting cnt-fs

!!! abstract "What this page tells you"
    In the VDI, open File Explorer and click CNT under This PC. If missing, map network drive Z: to \\pmacs.upenn.edu\depts\NE-4322-Neurology\CNT (or \\172.16.50.149\CNT) using different credentials, username pmacs\pennkey.

**pmacs\\Mounting cnt-fs:**

1. Log into VDI
2. Search up file explorer
3. Go to “This PC”
4. You should see the CNT server there
5. Click on CNT
6. If CNT is not there, then you have to remount it:
    1. Right-click on Network
    2. Select “Map Network Drive
    3. In Drive, select Z:
    4. In Folder, type in this pathway:
**\\\\**[**pmacs.upenn.edu**](http://pmacs.upenn.edu/)**\\depts\\NE-4322-Neurology\\CNT**
OR
**\\\\172.16.50.149\\CNT**

    1. Be sure to check "Connect using different credentials"
    2. Hit Finish
    3. When the login page pops up, put in your pmacs login:
        1. If the Domain does not say pmacs, then for your username put in **pmacs\\pennkey**
        2. In the screenshot below, if the domain did not say PMACS then the username would have been: **pmacs\\jacb**
        3. ![Windows credential prompt for 172.16.50.149, user jacb, password masked](../../assets/electrophysiology/mounting-cnt-fs/mounting-cnt-fs-01.png)
