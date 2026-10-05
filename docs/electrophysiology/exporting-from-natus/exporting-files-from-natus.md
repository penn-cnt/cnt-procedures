---
title: "Exporting Files from Natus"
stage: "Data Collection"
roles: [data-rc, crc]
order: 1
---

# Exporting Files from Natus

!!! abstract "What this page tells you"
    Remote into MZ03GCS2 via the remote access portal, open VNC Viewer to HUP-XLTEK-CNT (password in the lab password manager; three wrong attempts wipes Natus data), select the EMU Database, mount cnt-fs, then right-click the clip and export with video unchecked. Includes fixes for a locked or black Natus screen.

!!! warning "Credential removed"
    A password that appeared in the original text has been removed. Get it from the lab password manager, never from a wiki page.

**\*\*If the natus computer is stuck on the lockscreen, use ultra VNC to send the ctrl+alt+delete signal to the natus computer, or call the EEG technologist on duty**
\*\*or use the computer in the kitchen to send the ctrl+alt+delete signal

**\*\*if the natus computer is stuck on a black screen:**

*   send the ctrl + alt + delete signal by hovering your mouse towards the top of the screen until you see the bar appear
*   once you press the ctrl + alt + delete, click "sign out"
*   You might be brought back to the page on the remote desktop where you have to click into VNC viewer
*   click back into it and sign in to UPHS with your log in
*   You will then be brought to a page that asks you to log in to a work station (currently the only users with a work station are Mariam and Michael Beauchamp, so one of them will need to log in until other users get a work station)

**When all else fails, go to the EMU and try restarting the computer**

**Any other issues with the remote desktop or VNC viewer, call 215-662-7474HUP-XL**


*   We need to remote into the Natus computer which is in the EMU testing room.
*   To do this, we first will remote into the computer in the lab kitchen and then from there enter the Natus computer.
*   First, log into the remote access portal
*   Click on PennChart and Citrix Apps
*   Click on the remote desktop connection and enter the name of the computer:
    *   **MZ03GCS2 (used for Natus and/or Sectra access)**
    *   **MJ0HKNDA (only used for PennChart/Sectra access now)**
    *   Penn medicine password
*   Once you are in the computer, search VNC Viewer and click on the VNC app
*   Click on: HUP-XLTEK-CNT
*   **Password: *(in the password manager)* (USE THE CORRECT PASSWORD !!!)**
    *   _If you put in the incorrect password 3 times, all of the data in natus across all the hospitals will delete and you cannot stop it_
*   Once you are in Natus, make sure you are in the EMU Database in the top left
    *   If natus is not already open, click on the Natus Database app on the left
*   Search patient in the left hand side by name
*   You need to mount cnt-fs in the VNC Server Computer if it is not mounted already. Instructions are here: Mounting cnt-fs ([Mounting cnt-fs](../overview-and-setup/mounting-cnt-fs.md))
*   Right click on the clip you want to **export → select export → uncheck video → click browse folder to find the folder you need (Intracranial\_EEG, CCEPS, Gottfried, Gold\_Audio, etc.)**
*   As the recording is exporting from Natus to cnt-fs, there should be a pop-up window with a green bar and estimated time left for export. Within that window, there will be the patient's name followed by a random combination of letters and numbers. For example, "XXXXX~XXX\_1g67f23h." The first 8 letters and numbers are the unique file name for each eeg.
*   **24 hour Data Exporting:**
    *   For the 24 hour clips, they will take longer to export (around 45 min – 1 hour)
    *   You can close out of the VNC connection while the file is exporting and then come back later to check in; you do not need to sit there and wait for the file to export 
    *   if a master file is less than 30 mins, no need to export it
