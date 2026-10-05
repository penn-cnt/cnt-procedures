---
title: "Epilog ESI Protocol"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 3
---

# Epilog ESI Protocol

!!! abstract "What this page tells you"
    To send a presurgical MRI to Epilog: in Sectra IDS7 via remote desktop, find the pre-SEEG MRI, export the isotropic 3D T1 sequences (SAG/AX/COR) with the Default Anonymization Profile, convert DICOM to anonymized NIfTI in MRIcroGL, rename EPILOG_#_SAG.nii.gz, zip, and upload to preop-usa.epilog.care.

**EPILOG ESI PROTOCOL**
**\*\*\*8/4/23 note: Nishant might request for this\*\*** 

*   Log into Remote Workstation – 
*   From PennMedAccess (Remote Access Portal), select PennChart & CitrixApps. Open Remote Desktop Connection.  
*   Open PennChart after logging into Remote Desktop. On top right corner, press bottom arrow (located directly under “Resolute” and next to wrench icon), and click on Sectra IDS7 (may need to scroll to get to Sectra button) 
*   Look for patient’s Presurgical MRI – Under Patient History in the Middle of the Screen 
*   Scroll through imaging and click through all the MR studies. When you click the image, the description (history, technique, contrast) is on the right. Read Patient History to make sure the MRI is before SEEG (electrodes) surgery. Sometimes patients may have had previous outcome procedures (laser resection, etc.), but you are looking for an MRI before their upcoming procedure (most commonly SEEG).  
*   If the exam is archived (you can see the file cabinet icon to the left of the MR date label): right click and select “Retrieve from Archive”. Or you can double-click on the study. 
*   This may take some time. Wait until all the images have been retrieved. When they are all retrieved, the number on the right of the file cabineet will read X/X (example 36/36), and then the file cabinet and X/X will disappear. 
*   Right click on Patient’s presurgical MRI 
*   Select “Export to Media” 
*   A new window will pop up with all the imaging studies in this presurgical MRI checked. Press the plus sign next to the checked box. This will show you all the sequences in this study. Uncheck the parent box. 
*   Now check the sequence that is an isotropic 3D T1 image (ie T1 SAG MPR 176) 
*   MR SAG T1 MPRAGE ISO 
*   Uncheck “Include DICOM Viewer”, “Include Annotations”, “Export Reports (including drafts)”, “Export Scanned Documents”, and “Export requests” 
*   In beneath drop choice menu, select “Default Anonymization Profile” 
*   Destination à Browse: Create New folder on the Remote Desktop or export to PMACS server (ex. CNT1 or CNT-FS) 
*   Repeat this process for AXIAL and CORONAL T1 ISOTROPIC images. In the end you will have a folder with each type of image (Sagittal folder, Axial folder, Coronal folder) 
*   Now you have all the DICOM images. Move these images to a secure PMACS server you can access from your laptop. 
*   (Finder à Go à Connect to Server). Now you can see these DICOM images files on your computer.  
*   Open MRIcroGL to convert DICOM to Nifti and properly anonymize them 
*   Click Import (computer toolbar) à  DICOM to NIFTI à choose Compressed NIFTI (.nii.gz), Yes Anonymized, Precise Phillips Scaling, and Automatic Series Merging 
*   For the output directory, navigate to directory where you exported the DICOM images 
*   Select Folder to Convert à choose the folder where you stored the exported images 
*   Do one at a time to prevent confusion (SAG, AX, COR) 
*   Once you select the folder, it will look like the program is frozen/doing nothing (likely your mouse will be spinning), but it is running 
*   After a while, it should spit out the nifti and .json in the output folder than you gave it  
*   Rename the nifti and .json appropriately **(see Convert dicons to NIfTI section below)** 
*   Label with EPILOG\_#\_SAG.nii.gz 
*   Right click all the Nifti images and select compress. You will now have a zip file ready to upload to ESI website. 
*   [https://preop-usa.epilog.care/](https://preop-usa.epilog.care/) 
*   Select the correct EPILOG patient 
*   Upload Zip file onto MRI (Add Files)
