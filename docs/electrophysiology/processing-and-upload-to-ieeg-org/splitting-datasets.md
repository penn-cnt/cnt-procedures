---
title: "Splitting Datasets"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
order: 6
---

# Splitting Datasets

!!! abstract "What this page tells you"
    When Natus files overlap in start times or electrodes changed, split into two natusdir and data collection files suffixed D01 and D02 (plus two channel maps if electrodes changed), then process each with the intracranial instructions, updating file names. HUPXXX is the example.

**Please see HUPXXX in ieeg\_metadata in cnt-fs as an example patient!**

For eeg files in Natusdir that **overlap in their start times**, you need to **split the dataset** into 2 separate natusdir files because otherwise the natus2conversion will fail.

If there is an **electrode change**, you also will need to split the datasets into 2 to reflect the different electrodes used. This will also require **making a new channel map** to reflect the changed electrodes.

The processing is all done in the same way. The only change is that you will make 2 natusdir and data collection files and label them with D01 and D02 at the end. For example:
**HUPXXX\_natusdir\_D01**
**HUPXXX\_natusdir\_D02**

**HUPXXX\_datacollection\_D01**
**HUPXXX\_datacollection\_D02**

You can keep the same channel mapping if there is no electrode change. If there is an electrode change, then you also need to make 2 separate channel map files to reflect the different electrodes used. For example:
**HUPXXX\_channelMapping\_D01**
**HUPXXX\_channelMapping\_D02**

**Please find processing instructions in** Processing for [ieeg.org](http://ieeg.org) ([Processing for ieeg.org (natus2mef → validate → upload)](processing-for-ieeg-org-natus2mef-validate-upload.md)) and follow the intracranial instructions. **Because you are changing the names of the natusdir files by adding D01/D02 at the end, you NEED to change the file names in the example codes.**
