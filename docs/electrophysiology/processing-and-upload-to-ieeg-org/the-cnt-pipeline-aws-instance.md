---
title: "The cnt-pipeline AWS Instance"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 3
---

# The cnt-pipeline AWS Instance

!!! abstract "What this page tells you"
    On cnt1, run bash cnt-pipeline.sh status/start/stop in /project/eeg_process/programs to control the CNT AWS instance; then add -q CNT to ieeg upload-directory to prioritize CNT uploads.

### How to Run cnt-pipeline

The `cnt-pipeline` is an essential utility for researchers and data managers who work with [ieeg.org](http://ieeg.org), especially when dealing with concurrent data uploads from multiple sites. When enabled, it allows a user to add the `-q CNT` flag to their upload command, prioritizing their data in the processing/upload queue.

#### **What Does This Pipeline Do?**


*   The `cnt-pipeline` ensures that when you're uploading data to [ieeg.org](http://ieeg.org), you can request priority processing for CNT data.
*   By adding `-q CNT` to the `ieeg upload-directory ...` command, this data will be moved ahead in the queue.
*   This is particularly beneficial when there's a lot of traffic, ensuring that CNT data gets uploaded first.

#### **Starting the CNT AWS Instance**

Follow these steps to manage the CNT pipeline:


1. **SSH into cnt1**
    *   Securely log in to the PMACS cnt1 server using SSH.
2. **Navigate to Programs Directory**
    *   Run `cd /project/eeg_process/programs` to get to the directory where the pipeline scripts are located.
3. **List Options**
    *   Run the command `bash cnt-pipeline.sh` to display a list of available options for managing the pipeline.
4. **Check Status**
    *   Before starting or stopping the AWS instance, always check its current status:

```plain
bash cnt-pipeline.sh status
```


5. **Start the Instance**
    *   To start the AWS instance:

```plain
bash cnt-pipeline.sh start
```


6. **Stop the Instance**
    *   To shut down the AWS instance when it's no longer needed:

```plain
bash cnt-pipeline.sh stop
```

By following these instructions, you can effectively manage the priority of your data uploads, ensuring that your CNT data is processed promptly on [ieeg.org](http://ieeg.org).
