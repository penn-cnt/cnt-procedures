---
title: "EMU Interictal Scalp EEG Pipeline (duplicate — merge)"
stage: "Data Analytics"
roles: [analyst, pipeline]
order: 2
---

# EMU Interictal Scalp EEG Pipeline (duplicate — merge)

!!! abstract "What this page tells you"
    Full six-step pipeline for pulling EMU interictal scalp EEG from Natus, copying to cnt-fs, generating study lists with Admission IDs, running emu_pipeline.py to convert and upload to ieeg.org, uploading metadata to REDCap, and cleaning up. Marked as a copy.

!!! info "Duplicate"
    This page duplicates another page in this section. Merge them and delete this copy.

### Requirements

Before proceeding with the pipeline, ensure the following requirements are met:

*   Added to IRB
*   Access to UPHS workstation "MJ09PSLQ"
*   Access to UPHS `isilon-neurology` folder
*   Access to PMACS Virtual Desktop Interface (VDI)
*   Access to PMACS `cnt-fs` Windows HIPAA fileshare (Address: `\\172.16.50.149\CNT`)
    *   Access to the `/eeg_raw` folder
*   Access to PMACS `cnt1` Linux HIPAA server
    *   Access to the `/project/eeg_process` folder
*   Access to [ieeg.org](http://ieeg.org) EMU Interictal project folders (e.g. `EMU_Interictal_2024_01to04`)
*   Access to REDCap "EMU Scalp Interictal EEG" project

### Workflow

Follow these steps to execute the EMU Interictal Scalp EEG Collection, Processing, and Uploading Pipeline:
**Note:** When going through this processing pipeline, if you ever run a script in `cnt1` that attempts to access files in `cnt-fs` and encounter an issue such as a file or folder not being found, most likely the issue is that your PMACS account authentication between the `cnt1` and `cnt-fs` servers has timed out. Simply run the command `kinit` in the cnt1 terminal and enter your PMACS password to refresh your connection between `cnt1` and `cnt-fs`.

#### Step 1: Create EMU Export List


1. Use Erin's EMU export list pipeline to create an EMU export list.
    *   **Pipeline to generate list of file directories**
        1. Go to EMU Database
        2. Make view you want in Natus
            1. In Natus, go to Tools -> Options
            2. Select columns
                1. Last Name
                2. First Name
                3. Start time
                4. Duration
                5. Study name
                6. CD label
                7. MRN #
                8. Birth date
                9. EEG #
                10. File path
                11. Acquired on
                12. Headbox Type **(this is to get the correct channel mapping)**
        3. Create filter for interictal clips
            1. On left tab, click filters
            2. Click add
            3. Name the filter “interictal”
            4. Select “Study Name”
                1. Type “interictal”
            5. Select “Headbox”
                1. Select All
                2. Deselect Quantum
                3. (This makes it exclude Quantum, thus excluding intracranial)
        4. **_Alternate list 2024 - for seizures, no filter!_**
        5. Export list to Excel
            1. Tools->Export to Excel
            2. Filtered Studies
            3. Save it to `\\isilon-neurology\neurology\projects\EMU interictal clips`
            4. Call it `interictal_clip_list` (save as an xlsx file)
        6. Edit list to have full file path
            1. Run Erin’s Matlab code `prepare_eeg_file_list`
                1. [https://github.com/erinconrad/scalp\_interictal/blob/main/eeg\_data\_collection/prepare\_eeg\_file\_list.m](https://github.com/erinconrad/scalp_interictal/blob/main/eeg_data_collection/prepare_eeg_file_list.m)
2. Save the export list to the `cnt-fs` Windows fileshare. Save it in the folder `/eeg_raw/scalp_eeg/1_natus_export/` as an `.xlsx` file
    1. **DO NOT edit the column names in the Excel sheet**

#### Step 2: Login to UPHS Workstation and Copy EMU Database

The `copy_emu_db.py` script copies the EMU Interictal Scalp EEG datasets from the UPHS `isilon-neurology` folder over to the CNT's PMACS `cnt-fs` server. The data is in the raw Natus format. It also creates a copy log file.

1. Login to UPHS Workstation "MJ09PSLQ" (Erin's UPHS desktop). Login using your UPHS account and password
2. In File Explorer, map `cnt-fs` Windows fileshare to drive Z: (`\\172.16.50.149\CNT`). Login using your PMACS account.
    1. Click "Connect using different credentials". For User name, type `PMACS\pennkey` to change the Domain from UPHS to PMACS.
3. Map `\isilon-neurology` folder to drive Y: (`\\isilon-neurology\Neurology`).
4. Open Windows Command Prompt.
    1. Type "cmd" in the bottom search bar to open
5. Run `python copy_emu_db.py Z:/eeg_raw/scalp_eeg/1_natus_export/example_file.xlsx`
    *   A CSV file named `interictal_log_XXXX.csv` will be generated in `/eeg_raw/scalp_eeg/3_copy_logs/interictal/`
    *   **Note: Close the** **`.xlsx`** **file before running the Python script. Do not open the file while the process is running.**

#### Step 3: Login to VDI and Edit EMU Studylist

Pass in the copy log file to the `edit_studylist` Python script. The script does several things, including figuring out what the Admission ID should be for each recording, what the [iEEG.org](http://iEEG.org) filename should be, and what the date-shifted start time should be.

*       *   **Rules for Admission ID:**
        *   "Admission" is defined as a single EMU visit within a 30-day period. Any EMU recordings from a single patient within this time period are given the same Admission ID.
        *   Recordings that are part of the same "Admission" for a single patient are given the same Admission ID. Patients have different Admission IDs, but if a patient has multiple Admissions, then each Admission is a different Admission ID as well.
*       *   The `edit_studylist` Python script takes in a previously generated EMU\_studylist CSV file. For each record in the current study list being generated, it checks if that record meets the criteria of being within 30 days for the same patient. The last used Admission ID and REDCap record ID need to be entered for the script to know where to continue in generating Admission IDs and REDCap IDs.
1. Login to REDCap using your PMACS account. Open the "EMU Scalp Interictal EEG" Project.
2. Go to "Record Status Dashboard". Find the most recently used REDCap Record ID and save that number.
3. In Reports, go to the "admission\_ids" report. Click through the last few pages and sort by Admission ID to find the newest / largest used Admission ID number. Make sure to look through the last few pages and not simply the last page, as sometimes the largest ID number is not in the last page even after sorting. Be sure to save this number.
4. Login to the VDI using PMACS credentials. Open the MobaXterm application (search for it)
5. SSH into `cnt1` using your PMACS account (`ssh pennkey@cnt1`)
6. Navigate to `/project/eeg_process/scalp_eeg/scalp_eeg_programs/interictal_pipeline/`
7. Run `python edit_studylist.py /path/to/current/interictal_log.csv admit_n record_id /path/to/previous/studylist.csv`
    *   1\. Example path for current interictal log => `/mnt/cnt-fs/eeg_raw/scalp_eeg/3_copy_logs/interictal/interictal_log_XXXX.csv`
    *   2\. admit\_n => Input the largest used Admission ID so far
    *   3\. record\_id => Input the most recently used REDCap Record ID
    *   4\. Example path for the most recently used EMU Studylist => `/mnt/cnt-fs/eeg_raw/scalp_eeg/4_studylist/interictal/EMU_studylist_YYYYMMDD_XXXXXX.csv`
8. A CSV file named `EMU_studylist_YYYYMMDD_XXXXXX.csv` will be generated in `/eeg_raw/scalp_eeg/4_studylist/interictal/`
    1. I like to rename the file to append the starting and ending REDCap Record IDs that are a part of this data batch

#### Step 4: Run EMU Pipeline

The `emu_pipeline.py` pipeline does several things:

*       *   It runs `natus2mef` to convert the raw Natus recordings into .mef datasets. It uses the headboxes built into the natus converter to figure out the channel mappings.
    *   It looks through the EEG data and finds the gaps where there isn't any recorded data, i.e., it finds the clip times where there is real data. It creates annotations for these clip times and updates the studylist with them.
    *   It de-identifies the original EEG annotations of PHI and then merges the clip time annotations with the original de-identified annotations.
    *   Afterward, it uploads the full dataset to [iEEG.org](http://iEEG.org) into its appropriate [iEEG.org](http://iEEG.org) project folder. (The [iEEG.org](http://iEEG.org) EMU Interictal project folders are broken up by year and trimester, for example, `EMU_Interictal_2022_01to04` for recordings between January 2022 and April 2022).
1. Create the [ieeg.org](http://ieeg.org) project folder (`EMU_Interictal_YEAR_XXtoXX`) you are uploading to if it doesn't already exist.
    1. Log in to [ieeg.org](http://ieeg.org/). Click "Data", then "Create Project". Create "EMU\_Interictal\_2024\_01to04" (example)
    2. Click on the project name, then click "Open Project". Click "Project Admins". Click Command+F or Ctrl+F, then search for "Erin Conrad". Check the checkbox next to the username. Repeat to grant access to this project for any other collaborators.
2. In `cnt1` launch a new Linux Screen
    1. Run `screen -S insert_screen_name` to open a new Screen
3. Run `module load python` to load Python in the new environment
4. Make sure you're in `/project/eeg_process/scalp_eeg/scalp_eeg_programs/interictal_pipeline/`
5. Run `python emu_pipeline.py /path/to/emu/studylist.csv`
    1. Example path for current EMU studylist file => `/mnt/cnt-fs/eeg_raw/scalp_eeg/4_studylist/interictal/EMU_studylist_YYYYMMDD_XXXXXX.csv`
6. Detach from the Linux Screen. It will take a few minutes to process each record.
    1. Hold `Ctrl + A + D` to detach from Linux Screen
    2. You can always reattach to a Screen by typing `screen -r insert_screen_name`
    3. If you forget the Screen name, you can type `screen -ls` to find it
7. Wait until the batch processing finishes OR the processing halts/freezes
    1. DO NOT open the EMU Studylist `.csv` file in `cnt-fs` while this process is being run as the file is actively being modified
    2. If the program is stuck, type `Ctrl + C` to kill the batch processing. You will need to restart the batch processing from where it left off
        1. For the `EMUXXX_DayXX_X` dataset it was in the middle of processing, you will need to delete all of the incomplete files from cnt-fs. Go to the folder `cnt-fs/eeg_raw/scalp_eeg/5_mef/EMUXXX/EMUXXX_DayXX_X/` and delete its contents
        2. Make a duplicate copy of the current `EMU_studylist_YYYYMMDD_XXXXXX.csv` file in `cnt-fs`. In the duplicate copy, delete all the entries/rows that have already been processed, so that the `.csv` file now starts with the `EMUXXX_DayXX_X` dataset it was in the middle of processing. Rename this file (I like to append to the filename the starting and ending REDCap Record IDs that are a part of this new batch)
        3. Back in the Linux Screen, run `emu_pipeline.py` again but using the newly edited EMU Studylist `.csv` file
8. Once the batch has finished processing, logon to [ieeg.org](http://ieeg.org) and open the `EMU_Interictal_YEAR_XXtoXX` project folder to check if the datasets have uploaded to the [ieeg.org](http://ieeg.org) platform (user facing)
    1. Typically I just check if the last EEG dataset in the batch is searchable and viewable in the [ieeg.org](http://ieeg.org) project folder, since the records are processed sequentially

#### Step 5: Upload to REDCap

The `redcap_emu.py` script uploads the metadata from the EMU Studylist `.csv` log files to the REDCap "EMU Scalp Interictal EEG" project.

1. In `cnt1` make sure you're in `/project/eeg_process/scalp_eeg/scalp_eeg_programs/interictal_pipeline/`
2. Run `python redcap_emu.py /path/to/emu/studylist.csv`
    1. Example path for current EMU studylist file => `/mnt/cnt-fs/eeg_raw/scalp_eeg/4_studylist/interictal/EMU_studylist_YYYYMMDD_XXXXXX.csv`
3. Logon to REDCap, open the "EMU Scalp Interictal EEG" project, and verify that the records have successfully uploaded.

#### Step 6: Cleanup `cnt-fs`

I recommend deleting the `.mef` files from `cnt-fs` (stored in `/eeg_raw/scalp_eeg/5_mef/`) to free up disk space (and since these can be regenerated if needed).

1. In cnt1 go to `/project/eeg_process/scalp_eeg/scalp_eeg_programs/shared_processing/`
2. Run `python delete_mefs_from_studylist.py /path/to/emu/studylist.csv` to delete the `.mef` files that were generated from this batch processing
    1. Example path for current EMU studylist file => `/mnt/cnt-fs/eeg_raw/scalp_eeg/4_studylist/interictal/EMU_studylist_YYYYMMDD_XXXXXX.csv`

I also recommend deleting the original raw Natus files from `cnt-fs` to free up disk space (and since these can be re-copied from the UPHS `isilon-neurology` folder if needed).

1. In cnt1 go to `/project/eeg_process/scalp_eeg/scalp_eeg_programs/shared_processing/`
2. Run `python delete_natus.py /path/to/emu/studylist.csv` to delete the Natus files from this batch
    1. Example path for current EMU studylist file => `/mnt/cnt-fs/eeg_raw/scalp_eeg/4_studylist/interictal/EMU_studylist_YYYYMMDD_XXXXXX.csv`

If you are planning to keep the original raw Natus files, create a `yyyymmdd` folder in `cnt-fs` in `/eeg_raw/scalp_eeg/2_data_pull/` and move the datasets there.
