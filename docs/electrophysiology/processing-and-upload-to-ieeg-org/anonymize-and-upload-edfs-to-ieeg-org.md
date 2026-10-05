---
title: "Anonymize & Upload EDFs to ieeg.org"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 4
---

# Anonymize & Upload EDFs to ieeg.org

!!! abstract "What this page tells you"
    Anonymize Mxene EDFs on cnt1 with anonymize_edfs.sh (-n, -i, -d, -o required; date-shifts to 1/1/2000), create an ieeg-dataset.ini channel mapping, then upload the deid folder with ieeg upload-directory.

### Mxene EEG Processing/Uploading


1. move EDF file into **cnt-fs**
    1. For Mxene EEG: `/eeg_raw/Mxene_project/RIDXXXX/original`
2. de-identify EDF file
    1. Open Mobaxterm, and in **cnt1**, navigate to `/project/eeg_process/programs/edf_anonymize`
    2. in the command line run `bash anonymize_edfs.sh -n NAME -i ID -d DIRECTORY_INPUT -o DIRECTORY_OUTPUT -a ADD_DATE -s SUBTRACT_DATE`
        1. This will create a new EDF file with anonymized headers
            1. the de-identified file will be named `<original_filename>_deid.edf`
        2. Options
            1. `-n` : Removes the patient name from the header and replaces with a new name specified here. I recommend inputting `deid`
            2. `-i` : Removes the patient ID from the header and replaces with a new ID specified here. I recommend inputting `deid`
            3. `-d` : The path to the source directory where the EDF is stored. E.g. `/mnt/cnt-fs/eeg_raw/Mxene_project/RIDXXXX/original`
            4. `-o` : The path to the output directory where the deid EDF will be stored. E.g. `/mnt/cnt-fs/eeg_raw/Mxene_project/RIDXXXX/deid`
            5. `-a` : The default behavior will date shift the recording date of the EDF to 1/1/2000. Instead, if you would like to date shift by adding days to the original recording date, input the number of days you would like to add
            6. `-s` : The default behavior will date shift the recording date of the EDF to 1/1/2000. Instead, if you would like to date shift by subtracting days from the original recording date, input the number of days you would like to subtract
        3. The `-n` , `-i` , `-d` and `-o` flags are mandatory. It will error if any of these are missing
        4. The `-a` and `-s` flags are optional. By default, without these parameters the code will date shift the EDF to 1/1/2000, and this is generally recommended. If both parameters are included accidentally, then the code will error.
3. create the `ieeg-dataset.ini` channel mapping file
    1. copy the `ieeg-dataset.ini` template file and paste into **cnt-fs** `/eeg_raw/Mxene_project/RIDXXXX/deid`
    2. open the `ieeg-dataset.ini` file through Notepad, and edit the channel mappings as needed for the EDF recording
        1. Template: `channels=Fp1,Fp2,F7,F8,....`
        2. Notes:
            1. Each channel is separated by a comma. Be sure that there are no spaces between each channel
            2. The order of the channels matter! This will determine the order of the channels in [ieeg.org](http://ieeg.org)
            3. If you need to rename a channel, it will look like this: `channels=FP1:Fp1,FP2:Fp2,F7,F8,T3:T7,T4:T8,....`
                1. The old channel name is specified to the left of the colon, and the new channel name is specified to the right of the colon
            4. DO NOT rename the `ieeg-dataset.ini` file or else the upload process will error
4. upload the deid edf folder to [ieeg.org](http://ieeg.org)
    1. make sure the `<original_filename>_deid.edf` file and the `ieeg-dataset.ini` channel mapping file are both in the cnt-fs `/eeg_raw/Mxene_project/RIDXXXX/deid` directory, and no other files are in there
    2. In **cnt1**, navigate to `/project/eeg_process/programs/ieeg-cli-1.14.60`
    3. run `./ieeg upload-directory -n 'Human_Data/Hospital of the University of Pennsylvania/Mxene/RIDXXXX' '/mnt/cnt-fs/eeg_raw/Mxene_project/RIDXXXX/deid'`
    4. check [ieeg.org](http://ieeg.org) and verify the EDF looks good
