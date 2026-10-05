---
title: "Channel Mapping for EDFs (ieeg-dataset.ini)"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
audit: merge
order: 4
---

# Channel Mapping for EDFs (ieeg-dataset.ini)

!!! abstract "What this page tells you"
    Copy the ieeg-dataset.ini template into the RIDXXXX/deid folder and edit channels= as a comma-separated, space-free, ordered list; rename channels with old:new syntax. Do not rename the .ini file or the upload will fail.

1. create the `ieeg-dataset.ini` channel mapping file
    1. copy the `ieeg-dataset.ini` template file and paste into **cnt-fs** `/eeg_raw/Mxene_project/RIDXXXX/deid`
    2. open the `ieeg-dataset.ini` file through Notepad, and edit the channel mappings as needed for the EDF recording
        1. Template: `channels=Fp1,Fp2,F7,F8,....`
        2. Notes:
            1. Each channel is separated by a comma. Be sure that there are no spaces between each channel
            2. The order of the channels matter! This will determine the order of the channels in [ieeg.org](http://ieeg.org/)
            3. If you need to rename a channel, it will look like this: `channels=FP1:Fp1,FP2:Fp2,F7,F8,T3:T7,T4:T8,....`
                1. The old channel name is specified to the left of the colon, and the new channel name is specified to the right of the colon
            4. DO NOT rename the `ieeg-dataset.ini` file or else the upload process will error
