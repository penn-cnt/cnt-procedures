---
title: "The config Folder"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 5
---

# The config Folder

!!! abstract "What this page tells you"
    After all uploads, make config_intracranial, config_CCEPS, config_Gold, etc. folders (natusdir, data collection, convert log, both annotation files, montages), put them plus the PowerPoints/PDFs in a config folder, move it to ieeg_metadata/HUPXXX, then tell Josh A. the raw EEG is ready to archive.

1. Once you have run all of your processing and uploaded all of your files to [ieeg.org](http://ieeg.org), we will make a config folder with all of our text files. This config folder will be separated out from the raw eeg data files, as these files will eventually be archived to save space in cnt-fs.
2. Make a config folder for each task that was done (config\_intracranial, config\_CCEPS, config\_Gold, etc.)
3. The config folders should contain:
        1. Natusdir
        2. Data Collection
        3. Convert log
        4. annotations.iann.json
        5. annotations\_edit.iann.json (if present)
        6. Montages
4. In **cnt-fs/ieeg\_raw/ieeg\_raw/HUPXXX** make a folder called **config**
5. Take all of the config folders you have made (config\_intracranial, config\_CCEPS, config\_Gold, etc.) and put them all in the config folder that you just made.
6. Put the PowerPoints and pdf files in the config folder as well.
7. Go to **ieeg\_metadata** in cnt-fs and make a folder titled **HUPXXX**
8. Move the config folder out of the HUPXXX folder in **ieeg\_raw** and put it in the HUPXXX folder in **ieeg\_metadata**
    1. The idea here is to separate out the text files from the raw eeg files because the raw eeg files will eventually be archived to save space because they take up a TON of room.
9. Once this is done, the raw eeg files are ready to be archived - let Josh A. know!
