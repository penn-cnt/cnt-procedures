---
title: "Transferring Files from Box to cnt-fs (rclone)"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst, pipeline]
order: 3
---

# Transferring Files from Box to cnt-fs (rclone)

!!! abstract "What this page tells you"
    Move files between PennBox and cnt1/cnt-fs with rclone: ssh cnt1, mkdir the destination, then rclone copy remote:<Box path> <destination> -P (or reverse to upload). First-time setup is in Josh's rclone SOP, now marked outdated.

#### **Before running this script for the first time, follow the first steps of this SOP to get set up:** OUTDATED- (SOP: rclone file transfer between PennBox & cnt1) (“OUTDATED- (SOP: rclone file transfer between PennBox & cnt1)” *(retired page)*)

*   After doing this once, you will not have to do it again and can start with the steps below (aka step 3 on the above SOP)

### Downloading and Uploading Files

After configuring rclone (see sub-page titled "one time set up process), you can start
transferring files between PennBox and cnt1.


1. FIRST: ssh cnt1
2. Be sure to create the destination folder first if it does not already exist:
*   mkdir <path\_to\_destination>
    *   Example for CHOP data: mkdir /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data

1. To download files from PennBox to cnt1:
*   rclone copy remote:<path\_to\_file\_or\_folder\_on\_PennBox> <path\_to\_destination\_on\_cnt1>
    *   Example for CHOP data: rclone copy remote:CHOP\_CCEPs/CHOP\_spontaneous\_seizures/CHOPXXXspontaneous\_seizure\_data /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data -P

To upload files to PennBox from cnt1:

*   rclone copy <path\_to\_source\_on\_cnt1> remote:<path\_to\_destination\_on\_PennBox>

*   Replace remote with the name you assigned to your Box remote during the rclone configuration. Substitute <path\_to\_file\_or\_folder\_on\_PennBox> and <path\_to\_destination\_on\_cnt1> with the appropriate paths for your files.
*   Destination path can be a path on cnt1 or cnt-fs. You may need to create the directory first before running rclone, if it does not already exist
*   Include \-P to see progress update while downloading/uploading files.

#### Use Josh's SOP if this one ever doesn't work (possibly due to updates he has made):OUTDATED- (SOP: rclone file transfer between PennBox & cnt1) (“OUTDATED- (SOP: rclone file transfer between PennBox & cnt1)” *(retired page)*)
