---
title: "Moving Imaging Data Across CNT Servers"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst, pipeline]
order: 2
---

# Moving Imaging Data Across CNT Servers

!!! abstract "What this page tells you"
    Use rsync -avPhi source /destination to move data between cnt-fs, bscsub.pmacs.upenn.edu (davis_group), and borel.seas.upenn.edu; a trailing slash on the source moves contents without the top folder. Josh's diagram of the CNT servers is attached as a PDF.

**to move top directory and content within**
rsync -avPhi source/dir /destination/dir
example: rsync -avPhi /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/Justin\_images\_nii mjosyula[@bscsub.pmacs.upenn.edu](mailto:pennkey@bscsub.pmacs.upenn.edu):/project/davis\_group/mjosyula

rsync -avPhi /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/3T\_819126/RIDXXXX mjosyula[@bscsub.pmacs.upenn.edu](mailto:pennkey@bscsub.pmacs.upenn.edu):/project/davis\_group/mjosyula

example: rsync -avPhi /project/davis\_group/mjosyula/Justin\_images\_nii [mjosyula@borel.seas.upenn.edu](mailto:mjosyula@borel.seas.upenn.edu):/mnt/sauce/littlab/users/jchin09/projects/p1\_7T\_thalamus/source\_data/3T\_Clinical

rsync -avPhi /project/davis\_group/mjosyula/Justin\_images\_nii [mjosyula@borel.seas.upenn.edu](mailto:mjosyula@borel.seas.upenn.edu):/data/Human\_Data

rsync -avPhi /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/ [pennkey@bscsub.pmacs.upenn.edu](mailto:pennkey@bscsub.pmacs.upenn.edu):/project/davis\_group/mjosyula

**ssh mjosyula**[**@borel.seas.upenn.edu**](mailto:pennkey@borel.seas.upenn.edu)

**to move everything in top directory but not the top directory itself**
rsync -avPhi source/dir /destination/dir/
example: rsync -avPhi /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/3T\_819126/ [pennkey@bscsub.pmacs.upenn.edu](mailto:pennkey@bscsub.pmacs.upenn.edu):/project/davis\_group

**Josh's Diagram**\-

[📄 moving\_data\_CNT\_servers.pdf](../../assets/data/moving-imaging-data-across-cnt-servers/01-moving-data-cnt-servers.pdf)
