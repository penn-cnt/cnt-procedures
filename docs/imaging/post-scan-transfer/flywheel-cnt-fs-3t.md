---
title: "Flywheel → cnt-fs (3T)"
stage: "Data Collection"
roles: [crc, data-rc]
order: 1
---

# Flywheel → cnt-fs (3T)

!!! abstract "What this page tells you"
    Move a 3T scan from Flywheel into cnt-fs: download all dicoms for the RID from the presurgicalEpilepsy project, scp the RIDXXX folder to cnt1 /project/imaging_process/3T_819126 over VPN, then from the VDI cp it into cnt-fs imaging_raw/3T_819126 and delete the cnt1 copy.

!!! warning "Credential removed"
    A password that appeared in the original text has been removed. Get it from the lab password manager, never from a wiki page.

To mount cnt-fs, go to Mounting cnt-fs ([Mounting cnt-fs](../../electrophysiology/overview-and-setup/mounting-cnt-fs.md))

**Introduction:**
After a 3T or 7T research scan, move the scan into cnt-fs which is where the imaging will be stored so that other researchers in the lab can access the images for their projects

**3T - Flywheel into cnt-fs:**

1. Log into Flywheel: [https://login.flywheel.io/login?state=hKFo2SA0UWk1WTcwbFV6X1Y5RFc0T3VBclFXalNxQW5GUmtMTKFupWxvZ2luo3RpZNkgU1dnWk96Qjl3cU05S2lBMGVsRl9qSjEtdW8ydi1lbVqjY2lk2SAyVHhnQzFOaEtseEdHSlEwS1NUNmwwVzh3MEQ5aG1VbA&client=2TxgC1NhKlxGGJQ0KST6l0W8w0D9hmUl&protocol=oauth2&audience=https%3A%2F%2Fflywheel.io%2Fapi&scope=openid%20profile%20email&response\_type=code&response\_mode=query&nonce=MkRiUGlMfm5VNjJodEdna3Q2ZVd1eUdYZ0xUTW1qNjdILURrYzVSMm9pYQ%3D%3D&redirect\_uri=https%3A%2F%2Fupenn.flywheel.io%2F%23%2Fprojects&code\_challenge=ghWaQY09nMyEsa8JiZD2CdhWiuORxV8bve8QT1n50t0&code\_challenge\_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjIuNSJ9](https://login.flywheel.io/login?state=hKFo2SA0UWk1WTcwbFV6X1Y5RFc0T3VBclFXalNxQW5GUmtMTKFupWxvZ2luo3RpZNkgU1dnWk96Qjl3cU05S2lBMGVsRl9qSjEtdW8ydi1lbVqjY2lk2SAyVHhnQzFOaEtseEdHSlEwS1NUNmwwVzh3MEQ5aG1VbA&client=2TxgC1NhKlxGGJQ0KST6l0W8w0D9hmUl&protocol=oauth2&audience=https%3A%2F%2Fflywheel.io%2Fapi&scope=openid%20profile%20email&response_type=code&response_mode=query&nonce=MkRiUGlMfm5VNjJodEdna3Q2ZVd1eUdYZ0xUTW1qNjdILURrYzVSMm9pYQ%3D%3D&redirect_uri=https%3A%2F%2Fupenn.flywheel.io%2F%23%2Fprojects&code_challenge=ghWaQY09nMyEsa8JiZD2CdhWiuORxV8bve8QT1n50t0&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjIuNSJ9)
    1. Flywheel handle for 3T research scans: 
        1. **sub-RIDXXX@davis:presurgicalEpilepsy**
2. Select the **Projects** option in the blue menu on the left
3. Select the “**presurgicalEpilepsy**” project that shows up
4. Once inside the project, click the “**Sessions**” tab
5. Select the RIDXXX for the subject you are looking for
6. Go to the pop-up that shows up on the right and scroll to the right
7. Next to each of the dicoms if you hover over the word dicom, the download option will show up on the far right
8. <span class="attachment-withheld" title="Withheld after PHI review">🚫 Screenshot withheld (PHI review): Flywheel presurgicalEpilepsy session list with sub-RID subjects and scan timestamps — replace with a de-identified capture</span>
9. Go one-by-one and **download all of the dicoms** that are in the image for that subject.
    1. You may have to go to a second page if there are a lot of dicoms.
10. Go to your **Downloads** in your laptop.
11. Make a folder titled RIDXXX in your Downloads on your laptop and move the dicoms that you just downloaded from flywheel into this folder
12. Turn on F5 VPN, drag RID folder into the pathway:

**OR**


1. Open your Terminal:
    1. **Turn on your VPN (BIG-IP Edge Client)**
    2. **cd Downloads**
        1. This is going into your Downloads folder
    3. **cd RIDXXX**
        1. This is going into the RIDXXX folder you made
    4. **ls**
        1. This is showing everything in that folder to check to make sure the dicoms are in RIDXXX folder
    5. **cd ..** 
        1. This is to exit the RIDXXX folder
    6. Now you can put the dicoms first in cnt1:
        1. Command: **scp -r RIDXXX** [**pennkey@172.16.38.146**](mailto:pennkey@172.16.38.146)**:/project/imaging\_process/3T\_819126**
    7. Let the images copy into cnt1. Once they do, you can delete them from your Downloads folder.
2. Open the VDI and log in
3. Open mobaxterm (the VDI equivalent of the terminal)
    1. **ssh cnt1**
        1. This is entering cnt1
    2. **cd /project/imaging\_process/3T\_819126**
        1. This is bringing you into the folder in cnt1 where you copied the imaging from your Downloads folder.
    3. **ls** 
        1. Once you type ls, you should be able to see the RIDXXX folder that you copied into there from your laptop.
    4. Once you are in the 3T\_819126 folder, you can then copy the RIDXXX folder into cnt-fs
        1. **cp -r RIDXXX /mnt/cnt-fs/imaging\_process\_fs/imaging\_raw/3T\_819126 or 7T\_818407**
        2. If ever get a “permission denied” error, type in “kinit” and then type in your pmacs password.
4. Once this is done, please delete the RIDXXX folder from cnt1 with the command: rm -r RIDXXX (once you make sure it is copied over into cnt-fs)
