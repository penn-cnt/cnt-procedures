---
title: "Deleting a Dataset from ieeg.org"
stage: "Data Governance"
roles: [data-rc, pipeline]
order: 8
---

# Deleting a Dataset from ieeg.org

!!! abstract "What this page tells you"
    To delete an ieeg.org dataset: in the project, uncheck the dataset and copy its name first, then in cnt1 go to /project/eeg_process/programs/ieeg/ieeg-latest and run ./ieeg delete nameofdataset, confirming with Y.

1. In [ieeg.org](http://ieeg.org):
    1. hit projects
    2. go to the project folder where you need to delete a file
    3. hit open project
    4. uncheck the database you want to delete; **COPY THE NAME BEFORE DOING SO**
2. In the VDI➝mobaXterm
3. ssh cnt1
4. cd /project/eeg\_process/programs/ieeg/ieeg-latest
5. ./ieeg delete nameofdataset
6. Type “Y” for yes to delete
