---
title: "REDCap Documentation at the Scanner"
stage: "Data Collection"
roles: [crc]
order: 4
---

# REDCap Documentation at the Scanner

!!! abstract "What this page tells you"
    At the 3T/7T scanner, document the patient in the REDCap Surgical Repository: search by MRN, create the record in the Penn DAG, complete Patient Information, Consenting and Subject Numbers (next ID from RPPR reports), PEC demographics, and the preimplant scan instrument.

When you are completing a patient’s (or control’s) 3T or 7T research scan, you must document 
their demographic information in REDCap, in addition to information pertaining to the scan itself such as when the scan took place, what medications the patient is on, etc. This SOP will document how to collect that information. **This is important to collect while you are with the patient because some of the information may be difficult to find later in the patient’s chart. For example, race is typically not documented in PennChart.** 

**It is best to collect this information while you are consenting the patient. They will fill out the demographics sheet.**


1. Either before or after you consent the patient to the 3T or 7T research scan, log into the REDCap Surgical Repository
2. On the left-hand side under “Data Collection”, please select “Add / Edit Records” in red
3. Search the patient up to see if they already exist in REDCap **(Search by MRN).**
4. If they do not, then you can make a new record. **Make sure you are in the correct DAG when creating the new RID!**
5. Assign the record to the **Penn DAG**
6. When you are in the record, the first instrument that you can fill out is the “Patient Information” instrument.
    1. In this instrument, you can add in the Patient’s First Name, Last Name, MRN, DOB, subject type (control or patient), epileptologist, and institution.
    2. Only when all of this information is complete can you mark the instrument as complete.
    3. If you do not have all of this information with you while you are with the patient, then you can just put in their first and last name and then fill out the other information while they are in the scanner. 
7. The next instrument that you must fill out is the “Consenting and Subject Numbers” Instrument.
    1. Please select the study you are consenting the patient for, the date of the consent, any notes on consenting, and the subject number.
    2. Again, you can fill out the information you currently have while with the patient and then fill out the rest while they are in the scanner.
    3. To assign the patient a subject number, please follow these instructions:
    4.     *   Assigning a Subject Number to a Patient:
            *   Log into the REDCap surgical repository
            *   Scroll all the way down to the bottom until you get to the “Grants” tab in “Reports” on the left-hand side of redcap
            *   Depending on which study you are registering the patient to, select either the “RPPR (7T historical - all patients)” or “RPPR (3T historical - all patients)” report.
            *   Once here, you can look at the subject ID column to see what the last subject ID is.
            *   You then go 1 number up from that to get the new subject ID.
                *   _For example, if you are registering a 7T control to the clincard system, you would select the “RPPR (7T historical - all patients)” report in REDCap. Let’s say that the last control to be registered was “7T\_C033”. The new person would then be “7T\_C034”._
                1. Once this instrument is complete, you can mark it as complete.
8. Once this instrument is complete, please move on to the Instrument called “PEC Epilepsy Information (Patient Information)\*”
    1. Once here, please fill out the subject demographics part of the instrument, which is the first half of the instrument.
    2. Please also fill out their primary language.
    3. Once this is done, you can mark the form as “incomplete” since only the first half is completed.
9. Then move onto the instrument titled either “3T MRI LEN Preimplant” or “7T MRI Research Preimplant” depending on which scan you are doing.
    1. **This instrument will ask you a series of questions about the scan and some questions about the epilepsy history of the patient. Please fill out this information.**
    2. **If unable to complete with patient, go into their chart.**
        1. **To find medications, go to most recent appointment with their Neurologist and scroll through to find medications.** 
    3. ~~Unless the patient is a CAPES Control, you can ignore the “CAPES Controls - Medical History” section of the 3T Instrument.~~
    4. For the question “Did the participant complete the neurocognitive battery?” in both 3T and 7T instruments, you can select “No”.
    5. For the 7T Instrument, if the patient completed the entire scan in one appointment, you can select “No” for the question “Has the participant had a follow-up scan?”
    6. For the question asking where the scan was saved, you can write “cnt-fs/imaging\_process\_fs/imaging\_raw/3T\_819126 or 7T\_818407/RIDXXX”. This is the pathway for where the imaging will be moved to after the scan.
    7. Once all of the information is complete, you can mark the form as “Complete”.

You are finished! You can now scan the patient. **Once again, if there is any information you were not able to fill out at the scanner, please fill out ASAP after the scan.**
