---
title: "Uploading MRI CDs to cnt-fs"
stage: "Data Collection"
roles: [crc, data-rc]
audit: merge
order: 3
---

# Uploading MRI CDs to cnt-fs

!!! abstract "What this page tells you"
    Connect via Ivanti VPN and smb://pmacs.upenn.edu/depts/NE-4322-Neurology/CNT, then for each CD look up the patient in the REDCap CNT Surgical Repository, confirm RID and scan date, copy images into imaging_process_fs/imaging_raw/3T_819126/RID#### (RID###_2 for a second scan), and write the RID on the CD.

*   Open on Ivanti Secure Access Client
*   Press "connect"
*   type in PMACS username and password

*   go to the "Go" tab in the top left corner of your computer screen
*   hit "Connect to Server"
*   Choose: [smb://pmacs.upenn.edu/depts/NE-4322-Neurology/CNT](smb://pmacs.upenn.edu/depts/NE-4322-Neurology/CNT)
*   Press connect
*   in CNT, navigate to: /imaging\_process\_fs/imaging\_raw/3T\_819126
    *   this is the folder you will put the CD images into

*   put CD you want to upload into CD burner
*   have REDCap, "CNT Surgical Repository" open
*   look up the patient on the CD in REDCap
*   if they have an RID, look in /imaging\_process\_fs/imaging\_raw/3T\_819126 to ensure they do not have an RID folder already
*   you can also check the instruments, "Consenting and Subject Numbers" and "3T MRI LEN Preimplant" to see if the scan date/consent match with the scan date written on the CD
*   if they match, create their RID#### folder and put the images in
*   write their RID### on their CD so we know it was uploaded
*   if they have multiple research scans
    *   upload as RID### and RID###\_2
*   if you can't identify a scan, please write the issue on a sticky note and attach to the CD
    *   it might be good to also have an excel sheet where we can view the CDs with issues all in one place

*   PennChart can be used to verify if the patient had an fMRI or other scans done that day as the research date is often done right after fMRI appointment/on days of other scans
