---
title: "Manual Channel Mapping (legacy)"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 3
---

# Manual Channel Mapping (legacy)

!!! abstract "What this page tells you"
    Superseded instructions for building a channel map by hand with ./buildcm_python3.bak --gnd --ref HUPXXX in cnt1, entering electrodes in implant-map order with EKG1/EKG2, then copying to CCEPS and Intracranial_EEG. Use the Automated Channel Mapping page instead.

!!! note "Superseded"
    Kept for reference. Use **Automated Channel Mapping** for current work.

**THESE ARE INSTRUCTIONS FOR THE OLD WAY TO CREATE THE CHANNEL MAPPING. YOU SHOULD NOW USE THIS SOP TO CREATE THE CHANNEL MAPPING FILE:** Automated Channel Mapping ([Automated Channel Mapping](automated-channel-mapping.md))

Each type of EEG recording will need a separate channel mapping aside from the intracranial and CCEPS eeg files; **these 2 can share the same channel mapping.** Instructions are below on how to make each type of channel mapping. Research channel mapping typically has the DC1/DC7 channels added.

**Intracranial + CCEPS Channel Mapping**

1. Make sure that you have the implant map saved to the HUPXXX folder in cnt-fs as you will be using the electrodes in the map to make the channel map.
    *   You will need to follow these electrodes accurately.
    *   If there were changes in ref/gnd or addition/removal of electrodes due to a revision, pennchart/email thread/REDCap should contain this information 
        *   There will need to be a separate channel map
2. Make sure that you have the ref and gnd electrodes
3. Log into the VDI
4. Open MobaXterm
5. Enter cnt1 with: **ssh cnt1**
    *   Enter in pmacs password
6. Once in cnt1, go into programs: **cd /project/eeg\_process/programs/mef/build\_channel\_mappings**
    *   **We are using the ./buildcm\_python3.py script to make the channel mapping.**
    *   This is essentially a shortcut that allows us to list the electrodes in the implant map in a text file, without having to manually enter in each of the 12 electrode contacts (or however many there are).
    *   Enter in the code:
        *   ~~./buildcm\_python3.py --gnd XXXX --ref XXXX HUPXXX~~
        *   **./buildcm\_python3.bak --gnd XXXX --ref XXXX HUPXXX (USE THIS ONE)**
        *   new working code:
            *   ~~./buildcm\_python3.py --gnd XXXX --ref XXXX HUPXXX --ppt\_file ~/Documents/DATA\_ECOSYSTEM/IMPLANT\_LEADS/DATA/anon1.pptx --nlead XXX~~
            *   After --ref and --gnd, replace XXXX with the appropriate electrode contact name (ex: ref LA04 --gnd LB12) 
    *   You can then enter in the depth electrodes in the below format:
        *   LA1-12
        *   LB1-12
        *   Etc.
        *   **Enter the electrodes in the order that they appear in the implant map. If you mess up you will need to restart.**
    *   Note: **The two EKGs in a the map should be called EKG1 and EKG2** when you make the channel map
7. When you are done entering all of the electrodes, hit: **control + C** **to exit** 
8. You should have a channel map named HUP###\_channelMapping.txt created
    *   Check with **ls**

1. Copy the channel mapping file to the HUPXXX folder in ieeg\_raw in cnt-fs, and delete from the programs directory in cnt1
    *   Code for copying over (make sure you are in programs):
        *   **cp -r HUPXXX\_channelMapping.txt /mnt/cnt-fs/eeg\_raw/ieeg\_raw/HUPXXX**
    *   You will need to **delete off cnt1 once it is copied**, there is no need for it to be there and clutter the programs directory.
        *   **rm -r HUPXXX\_channelMapping.txt** 
    *   In cnt-fs, in eeg\_raw ➝ ieeg\_raw ➝ HUPXXX place this channel map in **both** the CCEPS folder and the Intracranial\_EEG folders
    *   **open text file and check if overall electrode number matches the powerpoint**
        *   **(will be n-1)**

**Gottfried Channel Mapping**

1. Sarah Cormiea will email you and let you know when she has completed her bedside testing task and has clipped the file in Natus. She will tell you if she used the DC1/DC7 channels and if she used Respiration channels.
2. Once you have the Intracranial/CCEPS channel mapping made, make a copy and paste it into the Gottfried folder in **ieeg\_raw/HUPXXX/Research/Gottfried**
3. Rename the channel mapping with **HUPXXX\_Gottfried\_channelMapping**
4. Open the text file.
5. At the very bottom you need to add the DC1/DC7 channels. This will be either
**256 DC01**
**262 DC07**
OR
**128 DC01**
**134 DC07**

1. Use the Respiration Channels that Sarah gave you and add in the Respiration channels as:
**RESP1**
**RESP2**
(You may have to relabel one of the intracranial electrodes with the RESP channels) 

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
