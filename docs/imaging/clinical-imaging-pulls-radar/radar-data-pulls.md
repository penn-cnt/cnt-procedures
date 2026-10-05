---
title: "RADAR Data Pulls"
stage: "Data Collection"
roles: [data-rc]
order: 1
---

# RADAR Data Pulls

!!! abstract "What this page tells you"
    Request RADAR imaging pulls via redcap.link/RADAR (PI fills out), then on MJ0HKNDA map \\isilon-cardiology\mim_anon, rsync to BSC /project/davis_group_1, fix chown/chmod, run dcm2niix/BIDS, and move dicoms to Borel/Sauce.

## Submitting data requests

*   RADAR Application to request RADAR data pulls (for PI to fill out): [https://redcap.link/RADAR](https://redcap.link/RADAR)
*   Once received, you will receive a Welcome Email from RADAR similar to this:

    Good morning \_\_\_\_\_\_,

    Thank you for submitting a request for imaging data through the Radiology Data Analytics Portal. We will begin working with you to transfer the data.

    In the past, we have transferred PHI studies, but we no longer offer this due to risk. We will fully deidentify the metadata and pixel data in your request. If the IRB has permitted it, we can provide you with a linking table (a csv file or similar) that connects any PHI (an MRN or accession) with the study ID.

    Please review the link below to determine folder structure for de-identified studies.

    [FAQ | RADAR | Perelman School of Medicine at the University of Pennsylvania (upenn.edu)](https://www.med.upenn.edu/radar/secure/frequently-asked-questions)

    RADAR doesn’t support the actual storing or operating of this data, so you may want to figure into your costs what the cost of image storage and compute will be. We can help you plan that out or estimate the costs if you want.

    If this is an industry sponsored research project before we begin the transfer of studies, we need to ensure Penn has signed off on the transfer of imaging data offsite. Is there a data usage agreement for your study or similar documentation?

    Based on your application detailing the number of imaging studies requested, we anticipate that the cost for the RADAR service will be $\_\_\_\_\_\_.

    The true cost will be based on the number of studies transferred, which could be lower due to some studies not being in the VNA, or higher because there may be more new studies than we anticipated, or other reasons. For budgeting a grant proposal, we can use approximate numbers.

    Please feel free to reach out to Shawn Bosley ([shawn.bosley@pennmedicine.upenn.edu](mailto:shawn.bosley@pennmedicine.upenn.edu)) if you have any questions.

    Many thanks,

    RADAR team

## Steps to transfer data from UPHS fileshare to CNT

1. Login to the Hayden Hall kitchen UPHS Windows 10 computer MJ0HKNDA
    1. You can either login in person or remotely (through [https://pennmedaccess.uphs.upenn.edu/my.policy](https://pennmedaccess.uphs.upenn.edu/my.policy)) using your UPHS/PennMed account (not your PMACS account)
    2. **Note**: This assumes you have a PennMed account
2. Open File Explorer and map the `\\isilon-cardiology\mim_anon` network drive
    1. This is the folder that Shawn from RADAR typically uploads the CNT's data pulls to
    2. Right click "This PC", then click "Map network drive"
    3. Select the "Y:" drive, then for Folder enter `\\isilon-cardiology\mim_anon`
    4. Typically the data pull is stored in the subfolder with the requestor's name, e.g. `\\isilon-cardiology\mim_anon\Josh`
    5. **Note**: You will first need to have your PennMed account be granted access to the network drive by Shawn/RADAR
3. Open a Cygwin Terminal window and create a new destination folder in the PMACS BSC Cluster
    1. Open Cygwin Terminal
    2. `ssh pennkey@bscsub.pmacs.upenn.edu` and enter your PMACS password
    3. `cd /project/davis_group_1/insert_project_folder`
    4. `mkdir new_destination_folder`
4. Open a second Cygwin Terminal window and run `rsync` to copy the data pull to BSC
    1. Open a new Cygwin Terminal window
        1. **Note**: Whenever you open a new window, you will be taken to your `/home/UPHS_username` folder, e.g. `/home/AsuncioJ`
    2. Run `rsync -avPhi --stats /cygdrive/y/Josh/ pennkey@bscsub.pmacs.upenn.edu:/project/davis_group_1/insert_project_folder/new_destination_folder/ > rsync_log_RADAR_2000-01-01.txt`
        1. The source data is in the `/cygdrive/y/Josh/` folder path, since we mapped `\\isilon-cardiology\mim_anon` to the "Y:" drive and the data is stored in the `\\isilon-cardiology\mim_anon\Josh` folder
        2. The destination folder path is in `/project/davis_group_1/insert_project_folder/new_destination_folder/` in BSC
        3. This code will save the output of `rsync -avPhi --stats` to a log file called `rsync_log_RADAR_2000-01-01.txt`. This log file will be stored locally on the UPHS computer in `/home/AsuncioJ` by default, if you don't change the file path.
5. Depending on the size of the data pull, `rsync` will take many hours to run. You can close the computer, but leave the Cygwin Terminal window open, DO NOT exit out of it.
6. Once `rsync` is finished, login to BSC Cluster on your own local computer and fix the file permissions as needed
    1. Usually you will need to recursively change the usergroup ownership for each of the files and folders in the data pull, so that the `davisgroup` usergroup can have access. In BSC, run `chown -R :davisgroup /project/davis_group_1/insert_project_folder/new_destination_folder`
    2. You may also need to change the `rwx` permissions for the files and folders. If needed, run `chmod -R 750 /project/davis_group_1/insert_project_folder/new_destination_folder` to give `rwx` access for the user, `r-x` access for the usergroup, and no access for other.
        1. **Note**: See this helpful link that explains `chmod` and `rwx` access: [https://quickref.me/chmod](https://quickref.me/chmod)
7. Run `dcm2niix` and/or BIDS on the imaging data
8. Once the `nifti` and `json` files are generated, we will store the `nifti` files on BSC and save the original `dicom` files to the CETS Sauce storage server
    1. Run `rsync` to copy the `dicom` files to the Borel compute server (files stored on Borel are actually being stored on Sauce): `rsync -ah --stats /project/davis_group_1/insert_project_folder/new_destination_folder/nifti pennkey@borel.seas.upenn.edu:/data/Human_Data/insert_project_folder/`
        1. The source folder is `/project/davis_group_1/insert_project_folder/new_destination_folder/nifti` in BSC
        2. The destination folder is `/data/Human_Data/insert_project_folder/` in Borel/Sauce
    2. Once confirmed that the `dicom` files have been successfully transferred over to Sauce/Borel, delete the `dicom` files from BSC: `rm -r /project/davis_group_1/insert_project_folder/new_destination_folder/dicom`
