---
title: "Uploading to Pennsieve Locally"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst, collaborator]
audit: merge
order: 2
---

# Uploading to Pennsieve Locally

!!! abstract "What this page tells you"
    To upload de-identified data from your laptop: run 'pennsieve agent' and 'pennsieve whoami', copy the dataset node ID (N:...) from the dataset overview, run 'pennsieve dataset use <id>', 'pennsieve manifest create <folder>', then 'pennsieve upload manifest <id>' and confirm the files appear.

**How to upload to Pennsieve from your local computer**

*   **Open terminal:** Run 'pennsieve agent'
*   Run 'pennsieve whoami'
    *   Make sure your profile it output
*   **Connect to dataset:**
    *   Open the pennsieve dataset you want to upload to
    *   Go to 'overview'
    *   At the top, above 'Open Dashboard' copy the Dataset node id
    *   It should look like 'N:xxxxxxxxxxxxx'
*   **Back in your terminal:** use the command 'pennsieve dataset use \*paste the N node id here\*' and enter
*   It should output the correct dataset you want as an 'Active dataset' with the correct information
*   **Create Manifest:** Use the command 'pennsieve manifest create \*path to local folder where the data exists\*' and enter
    *   This will create a Manifest ID for the data you want to upload
*   **Uploading data:** Use the command 'pennsieve upload manifest id #
    *   If done correctly it should output 'Upload initiated for manifest #' and subscribe you to updates for said upload
    *   Once the data is uploaded it will says 100.0% and unsubscribe client ID #
*   Go back to pennsieve and check the 'Files' of the workspace to make sure the correct files were all uploaded.
