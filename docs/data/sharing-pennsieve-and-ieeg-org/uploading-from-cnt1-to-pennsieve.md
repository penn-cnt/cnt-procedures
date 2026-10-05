---
title: "Uploading from cnt1 to Pennsieve"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst, collaborator]
order: 3
---

# Uploading from cnt1 to Pennsieve

!!! abstract "What this page tells you"
    To upload from CNT1: ssh to bscsub then CNT1, run 'module load pennsieve', complete the config wizard with your API token/secret, verify with whoami, 'pennsieve dataset use N', create a manifest for the CNT1 folder, and upload it. Page contains an API token/secret.

!!! warning "Credential removed"
    A password or key that appeared in the original text has been removed. Get it from the lab password manager, never from a wiki page.

### Uploading from CNT1 to Pennsieve


1. **Open Terminal**
2. **SSH into BSC cluster**
    *   Command: ssh [USER@bscsub.pmacs.upenn.edu](mailto:USER@bscsub.pmacs.upenn.edu)
    *   For example: ssh [bach2@bscsub.pmacs.upenn.edu](mailto:bach2@bscsub.pmacs.upenn.edu)
3. SSH into CNT1
    *   Once into bsc log into CNT1 with ssh USER@CNT1
4. **Load and Configure Pennsieve Agent or use script command ./pennsieve\_setup.sh to do this manually (the setup script's companion page was not migrated)**
    *   Load module: module load pennsieve
    *   Start config wizard: pennsieve config wizard
    *   In a separate terminal, get your secret and token with this command: cat .pennsieve/config.ini
    *   Enter the api\_token and api\_secret from your own `.pennsieve/config.ini` (they are personal; never paste them into a wiki page)
    *   Create a new profile bach2 (name it as you wish)
    *   Confirm with 'Y'
5. **Verify Pennsieve Login**
    *   Command: pennsieve whoami
    *   Ensure it returns your Pennsieve username
6. **Identify Dataset Number**
    *   Log in to Pennsieve and find the dataset node ID (N) you want to use
7. **Select the Dataset**
    *   Command: pennsieve dataset use N
8. **Create a Manifest for Your Folder**
    *   Command: pennsieve manifest create "cnt1 folder name"
    *   _Example:_ pennsieve manifest create "/project/rns/NYU\_Neuropace/"
9. **Upload the Manifest**
    *   Command: pennsieve upload manifest # (replace # with the manifest ID)
10. **(Optional) View Command History**
    *   Command: history

* * *

This version provides a clear, step-by-step guide for transferring files between Pennbox and CNT1, with improved organization and clarity.
