---
title: "Pennsieve Downloader"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst, collaborator]
order: 4
---

# Pennsieve Downloader

!!! abstract "What this page tells you"
    How to run pennsieve_downloader.py to pull one dataset (e.g. sub-NY648) from a Pennsieve DataSet: supply the dataset name, DataSet ID from the URL, and a short-lived API key obtained by running the download-manifest request on docs.pennsieve.io.

It currently allows you to download a single “dataset” from Pennsieve at a time (e.g. download “sub-NY648" and all its contents, inside the NYU Pennsieve DataSet).
On my to-do list was to adapt the code so that you can optionally download the entire DataSet (i.e. multiple datasets at a time), as well as download individual files (e.g. a single EDF file).

Run `python pennsieve_downloader.py` then it will prompt you to enter three things:

1. Dataset name
    1. If you want to specifically download the sub-NY648 dataset from the “NYU\_Data\_Ecosytem” DataSet in Pennsieve, enter `sub-NY648`
2. DataSet ID
    1. Enter the DataSet ID that corresponds with the “NYU\_Data\_Ecosytem” DataSet. You can find it in the URL when you navigate to that DataSet in Pennsieve. As an example, the ID takes the form `N:dataset:99097abf-d3d9-4f0b-83d6-2aefb7e9e988`
3. API key
    1. Go to [https://docs.pennsieve.io/reference/download-manifest](https://docs.pennsieve.io/reference/download-manifest) and login to your account
    2. In the “BODY PARAMS” section, in the “nodeIds” field, click “ADD STRING”, then copy and paste the DataSet ID (e.g. `N:dataset:99097abf-d3d9-4f0b-83d6-2aefb7e9e988` )
    3. To the right, in the “CURL REQUEST” box, click “Try it”. You should get a 200 response.
    4. Once you do, copy the API key which is in the “Query” box under “AUTHORIZATION” (Make sure when you copy that you scroll all the way to the end of the box to get the full API key).
    5. Notes
        1. If you don’t get a 200 response, you’ll need to re-try logging out and logging in again until it works. Often it will take several attempts to get a 200 response and an API key that works
        2. If the API key doesn’t work when you enter it into the script, make sure you’ve copied the whole API key. You may then need to try regenerating a brand new API key by logging out and logging in again
        3. I think the API key lasts for 10 mins
