---
title: "Pedro → cnt-fs (7T)"
stage: "Data Collection"
roles: [crc, data-rc]
audit: merge
order: 2
---

# Pedro → cnt-fs (7T)

!!! abstract "What this page tells you"
    Move a 7T scan from pedro into cnt-fs promptly (pedro purges scans): ssh to pedro (meduser@10.150.146.103, password in the lab password manager), scp the YYYYMMDD.818407_XX folder to cnt1 /project/imaging_process/7T_818407, ssh to cnt1, rename it to RIDXXX, cp into /mnt/cnt-fs/imaging_process_fs/imaging_raw/7T_818407, then delete from cnt1.

!!! warning "Credential removed"
    A password or key that appeared in the original text has been removed. Get it from the lab password manager, never from a wiki page.

To mount cnt-fs, go to Mounting cnt-fs ([Mounting cnt-fs](../../electrophysiology/overview-and-setup/mounting-cnt-fs.md))

**Introduction:**
After a 3T or 7T research scan, move the scan into cnt-fs which is where the imaging will be stored so that other researchers in the lab can access the images for their projects

**7T - Pedro into cnt-fs:**
All of the imaging from the 7T scanner is stored on a server called pedro. We first will enter the pedro server from our laptop, copy the images from pedro into cnt1, and then move the images from cnt1 to cnt-fs (in a similar way to how we do it for the 3T scan). **It is important to do this right away after the scan because the 7T scans ultimately get deleted from pedro after a certain amount of time.**


1. Turn F5 VPN on
2. First we enter Pedro: **ssh -oHostKeyAlgorithms=+ssh-rsa** [**meduser@10.150.146.103**](mailto:meduser@10.150.146.103)
3. Enter the password for pedro (in the lab password manager)
4. Navigate to the Reexport\_current folder, which is where all of the imaging is: **cd /mnt/rtexport/RTexport\_Current/**
5. Now we are going to copy the images into cnt1. All of the images in Pedro are labeled first with the date in the format YYYYMMDD.818407\_XX.818407\_XX where XX are the patient’s initials. Here is the command: **scp -r YYYYMMDD.818407\_XX.818407\_XX** [**pennkey@172.16.38.146**](mailto:pennkey@172.16.38.146)**:/project/imaging\_process/7T\_818407**
6. Open a new terminal: **ssh** [**pennkey@bscsub.pmacs.upenn.edu**](mailto:pennkey@bscsub.pmacs.upenn.edu)
7. Enter cnt1: **ssh cnt1** (enter PMACS password when prompted)
8. Navigate to 7T folder: **cd /project/imaging\_process/7T\_818407**
9. Type: ls
*   Once you type ls, you should be able to see the 7T scan that you copied into there from Pedro. However, it will not have the name RIDXXX. It will be named in the pedro naming convention described above. We want to rename this to be called RIDXXX.
10\. To rename the folder, we are going to use the command mv: **mv YYYYMMDD.818407\_XX.818407\_XX RIDXXX**
11\. Now that the 7T scan is renamed in the right RIDXXX format, we can now copy that folder into cnt-fs: **cp -r RIDXXX /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/7T\_818407**
Once this is done, please delete the RIDXXX folder from cnt1 with the command: **rm -r RIDXXX**

#### **Can also do this method, not as straightforward**
**\*\*TURN F5 VPN ON**
**Part 1**

1. First we enter pedro:
    1. ssh -oHostKeyAlgorithms=+ssh-rsa [meduser@10.150.146.103](mailto:meduser@10.150.146.103)
2. Enter the password for pedro (in the lab password manager)
3. Navigate to the Reexport\_current folder which is where all of the imaging is:
    1. cd /mnt/rtexport/RTexport\_Current/
4. Now we are going to copy the images into cnt1. All of the images in pedro are labeled first with the date in the format YYYYMMDD.818407\_XX.818407\_XX where XX are the patient’s initials. Here is the command below:
    1. **scp -r YYYYMMDD.818407\_XX.818407\_XX** [**pennkey@172.16.38.146**](mailto:pennkey@172.16.38.146)**:/project/imaging\_process/7T\_818407**

**Part 2**

1. Open the VDI and log in; **turn VPN off**
2. Open mobaxterm (the VDI equivalent of the terminal)
    1. **ssh cnt1**
        1. This is entering cnt1
    2. **cd /project/imaging\_process/7T\_818407**
        1. This is bringing you into the folder in cnt1 where you copied the imaging from your Downloads folder.
    3. **ls** 
        1. Once you type ls, you should be able to see the 7T scan that you copied into there from pedro. However, it will not have the name RIDXXX. It will be named in the pedro naming convention described above. We want to rename this to be called RIDXXX.
    4. To rename the folder, we are going to use the command mv:
        1. **mv YYYYMMDD.818407\_XX.818407\_XX RIDXXX**
    5. Now that the 7T scan is renamed in the right RIDXXX format, we can now copy that folder into cnt-fs:
        1. **cp -r RIDXXX /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/7T\_818407**
3. Once this is done, please delete the RIDXXX folder from cnt1 with the command: rm -r RIDXXX
