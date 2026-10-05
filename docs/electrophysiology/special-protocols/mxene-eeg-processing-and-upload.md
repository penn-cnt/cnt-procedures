---
title: "Mxene EEG Processing & Upload"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
audit: merge
order: 1
---

# Mxene EEG Processing & Upload

!!! abstract "What this page tells you"
    Export the Mxene and clinical recordings from Natus (EEG database) as EDF into cnt-fs/eeg_raw/Mxene_project/RIDXXXX subfolders, copy the .ini channel mapping from a previous patient, run anonymize_edfs.sh in cnt1 to create _deid.edf files, move originals to Original_edfs, then ieeg upload-directory each folder to the Mxene_Electrode project.

#### **Exporting the data:**

*   The data will be exported into cnt-fs
*   In cnt-fs, create a folder titled **RIDXXXX** in cnt-fs/eeg\_raw/Mxene\_project
*   Inside this folder (cnt-fs/eeg\_raw/Mxene\_project), create 2 folders called **RIDXXXX\_Mxene** and **RIDXXXX\_Clinical**
cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Mxene
cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Clinical

*   Create a data collection file and document the actual times and dates that the Mxene and Clinical recordings were done. You can leave this file in the RIDXXXX folder.
    *   This is just for record-keeping to make sure we have the actual dates/times documented somewhere. We do not need this for processing. Look at a previous patient for an example.
*   Log into the remote desktop to access the Natus computer
*   In the Natus computer, go to Database on the upper left hand side, and make sure to select EEG instead of EMU
*   Scroll to the date that the test was completed
*   Right click on the clip you want to export -> select export -> choose edf file -> video should be unchecked, but uncheck if not -> choose folder you need (RIDXXX\_Mxene)
*   **Export the data as an edf file!**
*   Export both the research file that you did AND the clinical eeg recorded. These will be 2 separate files
*   Export the Mxene file in the following folder in cnt-fs: eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Mxene
*   Export the Clinical file in the following folder in cnt-fs: eeg\_raw/Mxene\_project/RIDXXX/RIDXXXX\_Clinical

#### **Anonymizing edf files:**

*   We are first going to anonymize the edf files and then upload them to ieeg
*   Enter the VDI and mount cnt-fs: Mounting cnt-fs ([Mounting cnt-fs](../overview-and-setup/mounting-cnt-fs.md))
*   Copy over the Mxene .ini file (channel mapping file) from the previous patient's RIDXXXX\_Mxene folder into the current patient’s RIDXXXX\_Mxene folder
    *   **It is the same channel mapping file because the same channels are used!**
*   Copy over the Clinical .ini file (channel mapping file) from the previous patient's RIDXXXX\_Clinical folder into the current patient’s RIDXXXX\_Clinical folder
    *   **It is the same channel mapping file because the same channels are used!**
*   At this point, you should have 2 completed folders for the current patient in cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX: **1st folder (RIDXXXX\_Mxene)** with the Mxene edf file + Mxene .ini file and then the **2nd folder (RIDXXX\_Clinical)** with the Clinical edf file + Clinical .ini file
*   Now open Mobaxterm
*   Enter cnt1 with the following code:
    *   ssh cnt1
1. move EDF file into cnt-fs
    1. For Mxene EEG: cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXX\_Mxene

1. de-identify EDF file
    1. Open Mobaxterm, and in cnt1, navigate to
cd project/eeg\_process/programs/edf\_anonymize

    1. in the command line run
bash anonymize\_edfs.sh -n NAME -i ID -d DIRECTORY\_INPUT -o DIRECTORY\_OUTPUT -a ADD\_DATE -s SUBTRACT\_DATE


    1. 1. This will create a new EDF file with anonymized headers
            1. the de-identified file will be named:
<original\_filename>\_deid.edf

    1. 1. Options
            1. \-n: Removes the patient name from the header and replaces with a new name specified here. I recommend inputting deid
            2. \-i: Removes the patient ID from the header and replaces with a new ID specified here. I recommend inputting deid
            3. \-d:The path to the source directory where the EDF is stored
ex: cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Mxene

    1. 1.     1. `-o` : The path to the output directory where the deid EDF will be stored. E.g. `cnt-fs/eeg_raw/Mxene_project/RIDXXXX/deid`
            2. `-a` : The default behavior will date shift the recording date of the EDF to 1/1/2000. Instead, if you would like to date shift by adding days to the original recording date, input the number of days you would like to add
            3. `-s` : The default behavior will date shift the recording date of the EDF to 1/1/2000. Instead, if you would like to date shift by subtracting days from the original recording date, input the number of days you would like to subtract
    1. 1. The `-n` , `-i` , `-d` and `-o` flags are mandatory. It will error if any of these are missing
        2. The `-a` and `-s` flags are optional. By default, without these parameters the code will date shift the EDF to 1/1/2000, and this is generally recommended. If both parameters are included accidentally, then the code will error

*   Now at this point, the script will have created 2 anonymized edf files with .deid at the end!
    *   These are the ones we are going to upload to ieeg instead of the original edf files!
*   Go into the file explorer and enter cnt-fs
*   Enter eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Mxene
*   Move the original edf file out of this folder into the folder titled **"Original\_edfs"** in cnt-fs/eeg\_raw/Mxene\_project
*   Do the same for the original edf file in eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Clinical
*   All that should be left in the Mxene and Clinical folders for the current patient are the anonymized .deid edf files and the respective .ini files

1. upload the deid edf folder to [ieeg.org](http://ieeg.org/)
    1. make sure the `<original_filename>_deid.edf` file and the `ieeg-dataset.ini` channel mapping file are both in the `cnt-fs/eeg_raw/Mxene_project/RIDXXXX/deid` directory, and no other files are in there
    2. In cnt1, navigate to `/project/eeg_process/programs/ieeg-cli-1.14.60`
    3. run `./ieeg upload-directory -n 'Human_Data/Hospital of the University of Pennsylvania/Mxene/RIDXXXX' '/mnt/cnt-fs/eeg_raw/Mxene_project/RIDXXXX/deid'`
    4. check [ieeg.org](http://ieeg.org/) and verify the EDF looks good

#### **Upload anonymized edf files to ieeg:**

*   Go back to cnt1 in Mobaxterm
*   Enter the ieeg upload directory with this code:
    *   cd /project/eeg\_process/programs/ieeg-cli-latest
*   First upload the Mxene edf with this code:
    *   ./ieeg upload-directory -n 'Human\_Data/Hospital of the University of Pennsylvania/Mxene\_Electrode/RIDXXXX\_Mxene' '/mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Mxene'
*   Then upload the Clinical edf with this code:
    *   ./ieeg upload-directory -n 'Human\_Data/Hospital of the University of Pennsylvania/Mxene\_Electrode/RIDXXXX\_Clinical' '/mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Clinical'

You are all done!! 🙂
