---
title: "Automated Channel Mappings for Natus EEG"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 2
---

# Automated Channel Mappings for Natus EEG

!!! abstract "What this page tells you"
    Run auto_channel_mappings.py on cnt1 against a Natus recording directory to generate the channel mapping text file needed for Natus2mef; it flags discrepancies across recordings and outputs per-recording files to edit.

*   This program opens the Natus EEG files, reads the channel mappings embedded within the recordings, and automatically creates the channel mapping text file that is needed for Natus2mef processing.
*   When you pass in a directory path containing multiple Natus recordings (e.g. `/mnt/cnt-fs/eeg_raw/ieeg_raw/HUPXXX/Intracranial_EEG/`), it will compare the channel mappings between each recording.
*   If all channel mappings match, then it will return a singular channel mapping text file for that group of Natus recordings.
*   However, if there are any discrepancies between the channel mappings, it will print out a separate channel mapping file for each Natus recording.

Instructions:

1. Open the VDI. Open MobaXterm. SSH into cnt1.
2. Navigate to `/project/eeg_process/programs/mef/auto_channel_mappings/`
3. Run `python auto_channel_mappings.py /mnt/cnt-fs/eeg_raw/ieeg_raw/HUPXXX/Intracranial_EEG/`
`python auto_channel_mappings.py /mnt/cnt-fs/eeg_raw/ieeg_raw/HUPXXX/Research/CCEPS`

    1. Warning: This will take awhile to run, especially if there are many Natus recordings.
    2. The program will skip any Natus recordings that have errors and will print the error message in the terminal.
2. Once the program finishes reading the channel mappings for each Natus recording, one of two options will happen:
    1. If all channel mappings match, the program will ask you to enter a filename (e.g. `HUPXXX_channel_mapping`), and then it will create a singular channel mapping text file.
    2. If there are discrepancies between channel mappings, the program will create a separate channel mapping text file for each Natus recording.
3. Once the channel mapping text file(s) is created, open the channel mapping text file and make any necessary edits (e.g. deleting extraneous channels).
    1. By default, the channel mapping file(s) will be saved in `/project/eeg_process/programs/mef/auto_channel_mappings/`
    2. If multiple channel mapping files were generated, compare channel mappings and make edits as needed to create a singular master channel mapping file.
