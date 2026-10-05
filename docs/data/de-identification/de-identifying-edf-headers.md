---
title: "De-Identifying EDF Headers"
stage: "Data Governance"
roles: [data-rc, pipeline]
audit: merge
order: 2
---

# De-Identifying EDF Headers

!!! abstract "What this page tells you"
    Move the Mxene and Clinical EDF files into cnt-fs, copy an ieeg-dataset.ini channel map, run anonymize_edf.sh on cnt1 to strip patient name and ID, then upload both deid folders to ieeg.org with the ieeg CLI and verify.

1. **move EDF file into cnt-fs**
*   use Remote Desktop to export Mxene edf file and the clinical edf file from the day you did testing
    *   place Mxene edf file into /mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXX/RIXXX\_Mxene
    *   place Clinical edf file into /mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Clinical

1. **create the ieeg-dataset.ini channel mapping file**
    *   you can just copy and paste the channel mapping file from a previous subject (Mxene vs Clinical be different)
    *   leave the name as it is and channels as they are
        *   ieeg-dataset.ini

1. **de-identify EDF file**
    1. Open Mobaxterm, and in cnt1, navigate to: cd /project/eeg\_process/programs/edf\_headers
    2. run: bash anonymize\_edf.sh -n NAME -i ID -d DIRECTORY\_INPUT -o DIRECTORY\_OUTPUT
        1. this will create a new EDF file with anonymized headers
            *   file will be named "original\_filename"\_deid.edf
            *   options
                *   \-n: removes the patient name from the header and replaces with a new name specified here. I recommend inputting deid
                *   \-i: removes the patient ID from the header and replaces with a new ID specified here. I recommend inputting deid
                *   \-d: the path to the source directory where the EDF is stored
ex: /mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXX/RIDXXX\_Mxene

*       *       *       *       *   \-o: the path to the output directory where the deid EDF will be stored.
ex: /mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Mxene

*       *       *   The -n, -i, -d, and -o are mandatory. It will error if any of these are missing

4. **upload the deid edf folder to** [**ieeg.org**](http://ieeg.org)

*   make sure the "original\_filename"\_deid.edf file and the ieeg-dataset.ini channel mapping file are both in the cnt-fs/eeg\_raw/Mxene\_project/RIDXXX/deid directory, and no other files are in there
*   in cnt1, navigate to: cd /project/eeg\_process/programs/ieeg-cli.1.14.60
*   first upload the Mxene EDF with this code:
./ieeg upload-directory -n 'Human\_Data/Hospital of the University of Pennsylvania/Mxene\_Electrode/RIDXXXX\_Mxene' '/mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXX/RIDXXX\_Mxene/'

*   then upload the Clinical EDF with this code:
./ieeg upload-directory -n 'Human\_Data/Hospital of the University of Pennsylvania/Mxene\_Electrode/RIDXXXX\_Clinical' '/mnt/cnt-fs/eeg\_raw/Mxene\_project/RIDXXXX/RIDXXXX\_Clinical'


*   check [ieeg.org](http://ieeg.org/) and verify the EDF looks good
