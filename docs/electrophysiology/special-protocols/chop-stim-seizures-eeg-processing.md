---
title: "CHOP Stim Seizures EEG Processing"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 2
---

# CHOP Stim Seizures EEG Processing

!!! abstract "What this page tells you"
    Processing commands for CHOP stim seizure data: natus2mef with natus-converter-1.2.14 using paths under /mnt/cnt-fs/chop_fs/CHOP_stim_seizures, mefvalidate, redact annotations, copy annotations and montages, then upload to Human_Data/CHOP/CHOP_Stim_Seizures/CHOPXXX.

#### **Open VDI**

#### **Natus to mef conversion**

*   ssh cnt1
*   cd /project/eeg\_process/programs/natus-converter-1.2.14
*   screen -S CHOPXXX\_convert
*   ./natus2mef -c /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_natusDir.txt -m /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_channelMapping.txt -o ../../CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef >/mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_convert\_log 2>&1
*   Check to make the convert log says "Processing successful" before moving to the next steps.

#### **Mef validate**

*   cd /project/eeg\_process/programs/ieeg-cli-latest
    *   ./mefvalidate ../../CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef/\*.mef | grep PASS
    *   ./mefvalidate ../../CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef/\*.mef | grep FAIL

#### **Redact the annotations**

*   cd /project/eeg\_process/programs/
*   python redact\_annots\_python3.py ../CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef/annotations.iann.json ../CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef/annotations\_edit.iann.json

#### **Once you redact the annotations (any with PHI), enter the mef file that you just created with:**

*   cd /project/eeg\_process/CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef

#### **copy over both annotations files and the montages, and then delete the original annotations file from the mef**

*   cp -r annotations.iann.json /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data
*   cp -r annotations\_edit.iann.json /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data
*   cp -r montages.imtg.json /mnt/cnt-fs/chop\_fs/CHOP\_stim\_seizures/CHOPXXXspontaneous\_seizure\_data

**Delete original annotations file if it has PHI before uploading!!** **(unless you made no edits)**
rm -r annotations.iann.json

#### **Upload to** [**ieeg.org**](http://ieeg.org)

*   cd /project/eeg\_process/programs/ieeg-cli-latest
*   screen -S CHOPXXX\_ieeg\_upload
*   ./ieeg upload-directory -n 'Human\_Data/CHOP/CHOP\_Stim\_Seizures/CHOPXXX' '../../CHOPXXXspontaneous\_seizure\_data/CHOPXXX\_mef'
