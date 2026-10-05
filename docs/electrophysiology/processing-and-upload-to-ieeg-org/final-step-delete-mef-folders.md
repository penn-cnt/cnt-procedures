---
title: "Final Step: Delete mef Folders"
stage: "Data Standardization & Integration"
roles: [data-rc, pipeline]
audit: merge
order: 7
---

# Final Step: Delete mef Folders

!!! abstract "What this page tells you"
    Final step: after everything is uploaded to ieeg.org, ssh cnt1, cd /project/eeg_process, and rm -r HUPXXX to delete the converted mefs, because cnt1 is for processing, not storage.

The FINAL step in the ieeg processing pipeline is to delete the mef files from cnt1 once they are uploaded to [ieeg.org](http://ieeg.org)

**The reason we do this is because we want to use cnt1 solely as a space for processing data and running scripts. We do not want to use cnt1 as a storage space, and the mef files take up a lot of space.**

Once and ONLY once you are done with uploading everything to [ieeg.org](http://ieeg.org), you then need to delete the HUPXXX folder with all of the converted mefs in cnt1.


1. To do this, first enter cnt1 in Mobaxterm in the VDI with this code:
    1. **ssh cnt1**
2. Then, enter the directory where all of the HUPXXX folders are stored:
    1. **cd /project/eeg\_process**
3. Type **ls** to see all of the folders. You should see the HUPXXX folder that you just processed. This folder has all of the converted mefs.
4. Delete this HUPXXX folder with all of the converted mefs with this command:
    1. **rm -r HUPXXX**

## You are now done with eeg processing!! 🙂
