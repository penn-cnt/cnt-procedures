---
title: "Overview of CNT Systems"
stage: "Data Analytics"
roles: [data-rc, analyst, pipeline]
order: 1
---

# Overview of CNT Systems

!!! abstract "What this page tells you"
    Crash courses on cnt-fs (mount paths, user-group access via Josh), Persyst (LabArchives link), data sharing (use HUP numbers not RID; limited vs anonymized definitions), ieeg.org (adding datasets to projects, admins, upload path names), and AWS (upenn-ieeg and upenn-surgrec consoles).

This is supplemental information to the CNT Data and Computing Orientation powerpoint:
_cnt1 Crash Course_ 
·                cnt1 is the linux sever  

_cnt-fs Crash Course_  
·                cnt-fs is the HIPAA-secure Windows fileshare that we can mount to a Windows machine 
·                This is where we store a variety of data, especially things that we need to read 
·                Staff can access all directories; students, post-docs, etc. can only access things they are added to as part of a larger user group  
o        Ask Josh for more info about this and who is part of which user group for their projects 
·                Can mount one of two ways:  
o        \\\\[pmacs.upenn.edu](http://pmacs.upenn.edu/)\\depts\\NE-4322-Neurology\\CNT 
o        \\\\172.16.50.149\\CNT 
·                Can also mount onto your local machine/computer if you have the UPHS VPN open  
·                We are pushing to eventually move the raw Natus files to a storage space, Microsoft Azure, to make more room on cnt-fs  

_Persyst Crash Course_  
·                See [_Data Collection and Preprocessing/EEG/Persyst_](https://mynotebook.labarchives.com/share/CNT%2520Notebook/ODY5Ljd8NjkzNDY1LzY2OS0xNDkzL1RyZWVOb2RlLzIyMTY4NzA2NDB8MjIwNy43) in LabArchives

_Data Sharing Crash Course_ 
·                All data should be shared using Subject Number (HUPXXX), NOT with the RID number. 
·                Intracranial EEG clinical recordings "Spontaneous EEG" - Publicly shared intracranial datasets are associated with the project called "Multi" on [IEEG.org](http://ieeg.org/) 
·                Imaging data and reconstructions are de-dentified (converted to nifti), RID numbers changed to HUP numbers and shared. These scans are not masked/de-faced. 
·                As far as the difference between limited and anonymized data:  
o        Limited: can have RID numbers and dates of service 
o        Anon: only HUP numbers and date-shifted dates of service (usually shifted to 2000-01-01 for their intracranial first day of recording or with respect to this date) 

[_ieeg.org_](http://ieeg.org/) _Crash Course_ 
·                To upload to [ieeg.org](http://ieeg.org/), you will need to have an [ieeg.properties](http://ieeg.properties/) file in your home (~) directory on cnt-fs 
o        
·                To create a project:  
·                To add a preexisting dataset to another project:  
o        In the project the dataset already exists in, open the dataset you would like to add to another project 
o        Close the project 
o        Open the project you’d like to add to 
o        Scroll down to find the name of the dataset you want to add 
§     It should be unchecked (empty check box) 
o        Check it (box should now be blue) 
o        Done 
·                To become an admin or manager on a project (or to add others as that role):  
o        Open the project, clock Project Admin, search to find the name, click the check box so that it is blue  
§     Same with Project Team  
·                Changing paths when uploading:  
o        Most example code I have has “Hospital of the University of Pennsylvania”. But not everything that you upload will be data from HUP. In those instances, change “Hospital of the University of Pennsylvania” to the name of the institution the data came from 
§     Ex: UCLA, CCHMC, Children’s Hospital of Philadelphia, etc.  
·                Quick note: if you are uploading to ieeg and after hitting enter with your code, “>” appears in the following command line, it just means you have an open quotations mark 
o        Hit control C, and edit to include the appropriate quote mark, then rerun  

_AWS Crash Course_ 
·                AWS stands for Amazon Web Services 
·                Through our AWS logins (see John Frommeyer for granting account access), we can sign into the AWS web console with our IAM users for the following account IDs:  
o        upenn-ieeg 
o        upenn-surgrec  
·                The upenn-ieeg console allows us to access the back end of [ieeg.org](http://ieeg.org/), in case we need to trace who uploaded what and to where, redownload data, request data from storage (Glacier), or delete data  
o        Go to org-ieeg-inbox  
·                The upenn-surgrec console allows us to access the instance being utilized for the reconstruction pipeline. We can also edit security groups to add IP addresses for specific users so they can work from a static location that is not in the lab  
·                Anyone who has uploaded to ieeg has their own bucket number  
o        Can find some+ the individual’s name on Lab Archives if you search “bucket”
