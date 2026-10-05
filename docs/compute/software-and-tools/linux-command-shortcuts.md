---
title: "Linux Command Shortcuts"
stage: "Data Analytics"
roles: [analyst, data-rc]
order: 2
---

# Linux Command Shortcuts

!!! abstract "What this page tells you"
    Linux snippets: cp -Rvn to copy without overwriting, ls | wc -l to count files, and chown -R :davisgroup to fix group ownership on BSC. Includes pasted terminal output listing the davisgroup members.

### Useful Shortcuts


*   Copy from one directory to another without overwriting existing files

    ```plain
    cp -Rvn folder1 folder2
    ```

*   Count files in directory

    ```plain
    $ ls | wc -l
    ```

    As an example, let’s say that you want **to count the number of files** present in the “/etc” directory.

    ```plain
     $ ls /etc | wc -l

    ```

chown -R :davisgroup sub-RIDXXXX/
chown -R :davisgroup nifti\_BIDS\_missing\_3T/

\[asuncion@bscsub1 nifti\_BIDS\_missing\_3T\]$ groups
asuncion sftp cntaccess bsclpc davisgroup cnt\_staff\_group gugger cnt\_gpu

\[asuncion@bscsub1 nifti\_BIDS\_missing\_3T\]$ getent group davisgroup
davisgroup:\*:54740:holder,sudas,guggerj,nishants,arevell,chenyzh,allucas,mjaskir,bjprager,asuncion,ezou626,agowd,ethaneis,kkermani,nahu,smouchta,kulickc,mjosyula,phadar,tamjid,geasley,dilinir1,cheymach,pattnaik,audluo,stevennb,jenayej,erinconr,daviska
