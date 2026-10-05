---
title: "Troubleshooting Processing Errors"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 2
---

# Troubleshooting Processing Errors

!!! abstract "What this page tells you"
    Troubleshooting: run kinit for permission denied or stalled convert logs; check ieeg.org admin rights for upload errors; delete old mef, montage, and convert log before re-uploading; split datasets by sampling frequency (check in Persyst, comment lines with #); restart or manually fix redacted annotations.

1. If you ever get a “permission denied” message, input code: **kinit**
2. If the convert log stalls (but doesn't say "processing failed"), you can use **kinit** to resume processing
3. the natus to mef conversion takes a few minutes to run; if it finishes right away something wrong
4. if you have errors uploading to [ieeg.org](http://ieeg.org/), make sure you are added as an administrator
    1. log in to ieeg.org➝click on the project➝hit open project (top left)➝project admins are listed at the bottom
5. if you need to reupload something to [ieeg.org](http://ieeg.org/), delete the montage, convert log and the mef file from the HUP folder before retrying
    1. ssh cnt1
    2. cd /project/eeg\_process
    3. ls
    4. go into HUP folder you want to delete from (cd HUPXXX)
    5. rm -r the mef file you are redoing
6. If you are making the convert log and see that the sample frequency is not consistent throughout all the intracranial recordings, you will need to split the dataset to process the recordings in groups of their sampling frequency **(example in cnt-fs under HUPXXX)**
    1. To check the sampling frequency of the recordings:
        1. Open remote desktop
        2. Open Persyst
        3. In persyst, click "open" in the top left
        4. Click "browse file system"
        5. Click "This PC" ➝ "Network Drive" and then click through the folders in cnt-fs until you get to the eeg recording you want to check the sampling frequency for (Make sure it is in format: XLTEK)
        6. Once the recording is open, click "Patient" and you should see the sampling frequency for this recording
    2. Put # in front of any line on the data collection or natusdir that you don't want the program to read
        1. i.e. when exporting the datasets with the larger sampling frequency, you will need to put a # in front of all of the lines in the natusdir and data collection that correspond to the lower frequency
        2. Then when exporting the datasets with the lower sampling frequency, edit the natusdir and data collections so that the # is now in front of the lines that correspond to the higher frequency
7. If you make a mistake and you keep an annotation that should be deleted, hit **control + c** to end the script.
    1. Go into: cd /project/eeg\_process/HUPXXX/HUPXXX\_CCEPS\_mef
    2. Delete the edited annotations file with: rm -r annotations\_edit.iann.json
    3. Go back to the redact annotations script and start over:
    4. In cnt1: cd /project/eeg\_process/programs/
        1. python redact\_annots\_python3.py ../HUPXXX/HUPXXX\_CCEPS\_mef/annotations.iann.json ../HUPXXX/HUPXXX\_CCEPS\_mef/annotations\_edit.iann.json

**If you do not want to start over, you can manually fix the annotations file:** finish making the annotations, copy into cnt-fs like you normally would, open the file, command+f to search for any key words you noticed you missed, delete the annotation between the parentheses
