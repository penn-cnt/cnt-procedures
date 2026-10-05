---
title: "Moving Data Across cnt-fs, cnt1, BSC, Borel & Leif"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst, pipeline]
audit: merge
order: 1
---

# Moving Data Across cnt-fs, cnt1, BSC, Borel & Leif

!!! abstract "What this page tells you"
    Use rsync -avPhi to move data between cnt-fs, cnt1, BSC, Borel and Leif; a trailing slash on the source copies contents only. Includes example commands to BSC (bscsub.pmacs.upenn.edu) and Borel, plus a linked diagram PDF.

See diagram first:

[📄 move\_data\_CNT\_servers\_rsync.pdf](../../assets/data/moving-data-across-cnt-fs-cnt1-bsc-borel-and-leif/01-move-data-cnt-servers-rsync.pdf)

Move "dir" folder and everything in it into destination location:
`rsync -avPhi /source/dir /destination/dir`

Move contents inside "dir" folder (but not "dir" folder itself) into destination location:
`rsync -avPhi /source/dir/ /destination/dir`

E.g. move data from cnt1 into BSC:
`rsync -avPhi /source/dir asuncion@bscsub.pmacs.upenn.edu:/project/davis_group_1/____`

E.g. move data from BSC into Borel:
`rsync -avPhi /source/dir asuncion@borel.seas.upenn.edu:/data/Human_Data/____`
