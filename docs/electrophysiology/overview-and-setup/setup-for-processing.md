---
title: "Setup for Processing"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 2
---

# Setup for Processing

!!! abstract "What this page tells you"
    Before processing, get the implant map (text Lisa if missing), confirm ground/reference electrodes, make limited and anonymized PDF versions of the implant PowerPoint, upload them to cnt-fs under eeg_raw/ieeg_raw/HUPXXX, and create Intracranial_EEG and Research subfolders (CCEPS, Gold_Audio, Gottfried).

First, make sure that you have an [ieeg.properties](http://ieeg.properties) file created in cnt1 for you. Follow instructions here: [ieeg.properties](http://ieeg.properties) File ([The ieeg.properties File](the-ieeg-properties-file.md))

*   **You need the implant map**
    *   If the map is not emailed to you by Thursday morning (the morning after the implant), then please text Lisa to ask for the powerpoint (Important Contacts List)
*   **Make sure that the powerpoint has the ground and reference electrodes.**
    *   If not, text Lisa and ask what they are
    *   OR, you can go into the patient’s pennchart and open the discharge summary from their SEEG stay and the ground and reference electrodes will be stated there
*   Put powerpoint from email onto desktop
*   We are going to make 2 versions of the powerpoint and save them as PDF's
    *   1\. Limited Version
        *   Remove all names and any other information about the patient aside from Implant Date (i.e. crop name from surgery map, MRN, EEG#, etc.)
        *   Replace the patint’s name with **“HUPXXX RIDXXX”** on the title page
        *   Rename the powerpoint: **RID###\_HUP###\_limited** and save as PDF
    *   2\. Anonymized version
        *   Remove all names and dates and any other patient information (i.e. from red Surgery Date box, etc.)
        *   Replace the patient name with HUPXXX on the title page
        *   Rename the powerpoint: **HUP###\_anon** and save as PDF
        *   Replace the implant date with **01/01/2000**
*   You now have 3 documents on your desktop (1 powerpoint and 2 pdfs)
    *   If you are a CRC doing reconstructions, keep a copy of the anonymized version on your desktop to add to the reconstruction folder to upload to box.
*   **We are now going to upload those documents into cnt-fs**
*   **Turn the UPHS VPN on**
*   On the top left of your desktop go to:
    *   Go → connect to server → [**smb://172.16.50.149/CNT**](smb://172.16.50.149/CNT) →Put in PMACS username and password
*   We are now in cnt-fs.
*   In cnt-fs, go into **eeg\_raw ➝ ieeg\_raw** and then **make a HUP folder** titled HUPXXX with the HUP ID of the implant patient.
*   Copy the 3 files from your desktop and move them into the HUPXXX folder
*   Delete the files from your desktop permanently 
    *   If you are doing the reconstruction you can keep the anon pdf to add to upload to Penn Box.
*   Close cnt-fs and log out of UPHS VPN
*   Log into the VDI
*   Enter cnt-fs from the file explorer
    *   If you need to mount it go to Mounting cnt-fs ([Mounting cnt-fs](mounting-cnt-fs.md))
*   Go to **ieeg\_raw** into the HUPXXX folder that you made.
    *   Make a folder called **Intracranial\_EEG** and **Research** within HUPXXX
    *   Go into Research and create folders for all the testing done with the implant. Below are all the possible folders that could be made:
        *   **CCEPS**
        *   **Gold\_Audio**
        *   **Gottfried**
        *   If any of these tests are not done, then you do not need to make a folder within research as you will not be processing that eeg file. For example, if the CNT was not able to complete bedside testing with the patient then we would not make a Gold\_Audio folder in Research.
