---
title: "Automated Channel Mapping"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 1
---

# Automated Channel Mapping

!!! abstract "What this page tells you"
    Run python auto_channel_mappings.py on an exported Natus folder (usually CCEPS) in cnt1 to generate HUPXXX_channelMapping, add a GND/REF header, delete extra channels after EKG1/2, and copy it to CCEPS and Intracranial_EEG. For Gottfried and Gold, append DC01/DC07 (256/262 or 128/134) and RESP channels.

*   This program opens the Natus EEG files, reads the channel mappings embedded within the recordings, and automatically creates the channel mapping text file that is needed for Natus2mef processing.
*   When you pass in a directory path containing multiple Natus recordings (e.g. /mnt/cnt-fs/eeg\_raw/ieeg\_raw/HUPXXX/Intracranial\_EEG/), it will compare the channel mappings between each recording.
*   If all channel mappings match, then it will return a singular channel mapping text file for that group of Natus recordings.
*   However, if there are any discrepancies between the channel mappings, it will print out a separate channel mapping file for each Natus recording.
*   Export CCEPS file to cnt-fs. The script uses the natus recordings, so one set of recordings must be fully exported for this to work
    *   i.e. CCEPS, Gold\_Audio, or all of the Intracranial recordings. Since CCEPS is typically done first, it is easiest to use this recording to make the channel mapping

**Scripts to Run:**

1. Open the VDI. Open MobaXterm. **ssh into cnt1**
2. Navigate to: **cd /project/eeg\_process/programs/mef/auto\_channel\_mappings/**
3. Run: **python auto\_channel\_mappings.py /mnt/cnt-fs/eeg\_raw/ieeg\_raw/HUPXXX/Research/CCEPS**
    1. Warning: This can take awhile to run, especially if there are many Natus recordings.
    2. The program will skip any Natus recordings that have errors and will print the error message in the terminal.
    3. Don't forget to change the file name at the end to the destination needed
4. Name the file: **HUPXXX\_channelMapping**
5. Copy the channel mapping file to the HUPXXX folder in cnt-fs:
    1. enter the file: **cd /project/eeg\_process/programs/mef/auto\_channel\_mappings/**
        1. copy into cnt-fs: **cp -r HUPXXX\_channelMapping.txt** **/mnt/cnt-fs/eeg\_raw/ieeg\_raw/HUPXXX/Research/CCEPS**
6. Once the channel mapping text file(s) is created, open the channel mapping text file and make any necessary edits (e.g. deleting extraneous channels).
    1. Add at the top of the file**:** **\# HUPXXX channel mapping # XX GND # XX REF**
        1. include both the name of the electrode and the number for the ground and ref electrodes (i.e. # 89 LA4 GND)
    2. If multiple channel mapping files were generated, compare channel mappings and make edits as needed to create a singular master channel mapping file.
    3. _delete all of the extra channels--the channel mapping will create 400+ channels; delete all of the ones after the EKG1 and 2, or whatever your last two electrodes should be._
7. **Within the HUP folder in cnt-fs, copy the channel mapping file you made for CCEPS into the Intracranial\_EEG folder, as they are the same**
8. If Gottfried and Gold Audio Tasks were done, follow the steps below to add the appropriate channels to the channel mapping you created above.

**Gottfried Channel Mapping**

1. Sarah Cormiea will email you and let you know when she has completed her bedside testing task and has clipped the file in Natus. She will tell you if she used the DC1/DC7 channels and if she used Respiration channels.
2. Once you have the Intracranial/CCEPS channel mapping made, make a copy and paste it into the Gottfried folder in **ieeg\_raw/HUPXXX/Research/Gottfried**
3. Rename the channel mapping with **HUPXXX\_Gottfried\_channelMapping**
4. Open the text file.
5. At the very bottom of the channel mapping you need to add the DC1/DC7 channels. This will be either
**256 DC01**
**262 DC07**
OR
**128 DC01**
**134 DC07**

_Try the 256/262 channels and if the convert log fails, try running it with the 128/134 channels there instead_


1. Use the Respiration Channels that Sarah gave you and add in the Respiration channels as:
**RESP1**
**RESP2**
(You may have to relabel one of the intracranial electrodes with the RESP channels; put them at whatever number sarah tells you)

**Gold Audio Task Channel Mapping**

1. Once you have the Intracranial/CCEPS channel mapping made, make a copy and paste it into the Gold folder in **ieeg\_raw/HUPXXX/Research/Gold\_Audio**
2. Rename the channel mapping with **HUPXXX\_Gold\_channelMapping**
3. Open the text file.
4. At the very bottom you need to add the DC1/DC7 channels. This will be either
**256 DC01**
**262 DC07**
OR
**128 DC01**
**134 DC07**

_Try the 256/262 channels and if the convert log fails, try running it with the 128/134 channels there instead_
