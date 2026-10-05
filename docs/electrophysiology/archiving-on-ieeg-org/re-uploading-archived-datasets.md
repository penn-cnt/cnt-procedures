---
title: "Re-uploading Archived Datasets"
stage: "Data Governance"
roles: [pipeline]
order: 3
---

# Re-uploading Archived Datasets

!!! abstract "What this page tells you"
    To fix an already-archived dataset, ask Josh to unarchive it to /project/eeg_process/azure_archive/recently_unarchived/HUPXXX, recreate the HUPXXX folder in cnt-fs with channel mapping, natusdir, and data collection from ieeg_metadata, cp the recordings back, then rerun the Processing for ieeg.org SOP from the mef conversion.

If there is an error in an uploaded dataset that has already been archived from cnt-fs, follow the steps below.

1. Ask Josh to put in a ticket to request that it be unarchived
2. He will move it to cnt1 in project/eeg\_process/azure\_archive/HUPXXX
3. Create a HUPXXX folder in cnt-fs in eeg\_raw/ieeg\_raw
    1. move the channel mapping, natusdir, and data collection files from ieeg\_metadata to this HUPXXX folder
4. In Mobaxterm in the VDI, enter the unarchived HUPXXX folder in cnt1: **cd /project/eeg\_process/azure\_archive/recently\_unarchived/HUPXXX**
5. Now you are going to copy the unarchived data from cnt1 into cnt-fs : **cp -r Intracranial\_EEG /mnt/cnt-fs/eeg\_raw/ieeg\_raw/HUPXXX**
6. This will take some time to finish
7. Remember you need to following files to reupload:
    1. All the eeg recordings
    2. natusdir
    3. channel mapping
    4. data collection
8. Once you have everything unarchived, you can proceed with the Processing for [ieeg.org](http://ieeg.org) ([Processing for ieeg.org (natus2mef → validate → upload)](../processing-and-upload-to-ieeg-org/processing-for-ieeg-org-natus2mef-validate-upload.md)) SOP, starting from the beginning with converting the recordings to mefs
