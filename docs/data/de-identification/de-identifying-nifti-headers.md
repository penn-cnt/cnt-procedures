---
title: "De-identifying NIfTI Headers"
stage: "Data Governance"
roles: [data-rc, pipeline]
order: 3
---

# De-identifying NIfTI Headers

!!! abstract "What this page tells you"
    De-identify nifti images in cnt1: add each /mnt/cnt-fs/imaging_process_fs/imaging_bids/subRIDXXX path to deid_json_queue.txt in /project/imaging_process/programs/deid_json (blank trailing line), then run bash deid_json.sh from the heudiconv_3T folder. Images must be nifti first (see dicom-to-nifti page).

KNOWLEDGE BASE (a page *(retired page)*)


*   to use this script, images must be in nifti format
*   [use this sop](../../imaging/formatting/dicom-nifti-non-bids.md) to convert from dicom to nifti

1. in cnt1 de-identify the nifti images using deid\_json
    1. in MobaXterm, in cnt1 go to: /project/imaging\_process/programs/deid\_json/, open the deid\_json\_queue.txt file
    2. for each line, type /mnt/cnt-fs/imaging\_process\_fs/imaging\_bids/subRIDXXX, then hit save
        1. hit enter so there is an empty line below the script
    3. go to /project/imaging\_process/programs/heudiconv\_3T/ (Mariam needs to update path)
    4. type bash deid\_json.sh and hit enter to run
