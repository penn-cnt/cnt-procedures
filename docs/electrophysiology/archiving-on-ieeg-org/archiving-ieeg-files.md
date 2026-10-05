---
title: "Archiving ieeg Files"
stage: "Data Governance"
roles: [pipeline]
order: 1
---

# Archiving ieeg Files

!!! abstract "What this page tells you"
    Archive a finished HUPXXX: in cnt1 run bash zip_dataset.sh on the cnt-fs folder inside a screen, verify checksums, delete the folder from cnt-fs, move the tarball to ready_for_archiving, upload with upload_azcli.sh (via cntgpu1 or cnt2), confirm it in the cntlitt Azure container, then delete it.

1. In cnt1, navigate to scripts in /project/eeg\_process/azure\_archive folder:
cd /project/eeg\_process/azure\_archive/scripts


1. open a new screen in cnt1: screen -S HUPXXX\_archive

1. bash zip\_dataset.sh /mnt/cnt-fs/eeg\_raw/ieeg\_raw/HUPXXX
*   if you get an error that says "permission denied", run kinit
*   this step zips up the HUPXXX file into a tarball (zip file)

1. when the script has finished running (this takes a long time):
*   check that the 2 top numbers are =
*   check that 2 bottom numbers are =

1. delete the HUPXXX folder from cnt-fs

1. move the HUPXXX tarball HUPXXX.tar.gz file into the logs\_archive folder /project/eeg\_process/azure\_archive/ready\_for\_archiving
*   The HUPXXXtarball will be in the **/project/eeg\_process/azure\_archive/scripts**, so make sure you are in that file path first before running the below script:
    *   mv HUPXXX.tar.gz /project/eeg\_process/azure\_archive/ready\_for\_archiving

1. In a new screen / tab, ssh pmacsusername@scisub9
*   Enter your pmacs password to log in

1. bsub -Is -q cntgpu -m cntgpu1 'bash'
*   You should see this pop up and your user change from \[pmacsuser@scisub9 ~\]$ to \[pmacsuser@cntgpu1 ~\]$
Job <47179607> is submitted to queue <cntgpu>.
<<Waiting for dispatch ...>>
<<Starting on cntgpu1>>


1. cd /project/eeg\_process/azure\_archive/scripts
nohup ./upload\_azcli.sh HUPXXX.tar.gz > /project/eeg\_process/azure\_archive/logs\_azure/HUPXXX\_azure\_archive.log 2>&1 &

*   You can check the process using ps -ef|grep az

10\. Login to [http://portal.azure.com](http://portal.azure.com) to check that the tarball has been uploaded to Brian Litt's account

    1. Login using Penn Medicine (UPHS) account
    2. Search for the "**cntlitt**" storage account
    3. In the dropdown on the left-hand side, go to **"Data Storage" → "Containers"**
    4. Open "**cntlitt**" container
    5. Look for **HUPXXX.tar.gz**

11\. Once you make sure the HUPXXX.tar.gz is in Brian Litt's Azure account, delete it from cnt1

*       *   Go to the ready\_for\_archiving folder:
cd /project/eeg\_process/azure\_archive/ready\_for\_archiving

*       *   rm -r HUPXXX.tar.gz

**05/19/2026 - cnt1 crashed and cannot support azure uploads so this step is unusable. If cnt2 is running, try replacing Steps 7-9 above with the below step.**


1. Make sure you are in the **/project/eeg\_process/azure\_archive/scripts** folder, then run the code to upload the tarball to Azure:

nohup bash upload\_azcli.sh HUPXXX.tar.gz &> /project/eeg\_process/azure\_archive/logs\_azure/HUPXXX\_azure\_archive.log


1. Check the log file **/project/eeg\_process/azure\_archive/logs\_azure/HUPXXX\_azure\_archive.log** for process on uploading the tarball to Azure. Check that the upload is finished and check that the size of the remote tarball file **\=** size of the local tarball file
**Josh's SOP**
KNOWLEDGE BASE (a page *(retired page)*)
