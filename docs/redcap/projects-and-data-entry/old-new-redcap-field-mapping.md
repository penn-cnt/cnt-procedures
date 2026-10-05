---
title: "Old → New REDCap Field Mapping"
stage: "Data Standardization & Integration"
roles: [crc, data-rc]
order: 5
---

# Old → New REDCap Field Mapping

!!! abstract "What this page tells you"
    Cat's rulings for migrating 'non-lateralizing' answers from the old REDCap to the new one: fMRI to bilateral L=R, 3T to non-lesional, scalp EEG to diffuse onset, neuropsych to no dysfunction, PET to no hypometabolism, MEG/ESI/SPECT to no clusters; drop language-concern answers not tied to resection/ablation.

**Questions with Cat's responses in bolded blue**
**fMRI**
is the ‘non-lateralizing’ option in the old REDCap equivalent to 'no language activation' on the new REDCap?  **Would make non-lateralizing into bilateral activation L=R**
**3T**
is the ‘non-lateralizing’ option in the old REDCap equivalent to 'non-lesional' on the new REDCap? **Yes, non-lesional as default, as this is most common. Note to selves that a few of these may be bilateral lesions L=R in reality and this may need to be double checked if needed for a project**

#### **Scalp EEG**
is the ‘non-lateralizing’ option in the old REDCap equivalent to 'no seizures' or 'diffuse onset' on the new REDCap? **Diffuse onset as default, as this is most common. Note to selves that a few of these may be no seizures in reality and this may need to be double checked if needed for a project**

#### **Neuropsych**
is the ‘non-lateralizing’ option in the old REDCap equivalent to ‘no dysfunctin’ on the new REDCap? **Ugh good question. I think it might be close to 50/50 which of these have no vs bilateral dysfunction. I think no dysfunction as default with a similar note to selves that this may need to be double checked at some point.**

#### **Degree of concern that surgical intervention would affect language:**
I am noticing the older survey responses include the language concern option but do not have anything under proposed plan checked off. Should I just leave the language estimate out since this only comes up when ablation or resection are checked now? **Yes I think we can scrap any of the language concern answers that are not coupled with resection or ablation being checked off in plan (they will still be archived somehow right?)**

#### **PET**
Old REDCap is 'non-lateralizing' should I do 'no hypometabolism' or 'bilateral hypometabolism (Left=Right)' in the new REDCap? **No hypometabolism**

**My notes**
**MEG**
For 'non-localizing/non-lateralizing' in old REDCap, I put 'no clusters' in new REDCap. I think this could also be bilateral clusters for some patients.

**iEEG**
Just filling out the ictal intracranial EEG field, not interictal. Unsure if I need to go back and add to interictal as well.

**ESI**
When 'non-lateralizing' in old REDCap, I am putting 'no clusters' in new REDCap. I think this could also be 'bilateral clusters' for some patients.

**Ictal Spect**
When 'non-lateralizing' in old REDCap, I am putting 'no clusters' in new REDCap. I think this could also be 'bilateral clusters' for some patients.
