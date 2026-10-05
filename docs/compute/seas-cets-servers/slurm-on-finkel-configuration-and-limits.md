---
title: "SLURM on Finkel: Configuration & Limits"
stage: "Data Analytics"
roles: [analyst, pipeline]
audit: merge
order: 5
---

# SLURM on Finkel: Configuration & Limits

!!! abstract "What this page tells you"
    Finkel SLURM settings: 8 GPU shards (4 per L40S, ~12GB each), 14-day max job time, 100 queued jobs per user, /scratch purged after 21 days, open to cntgroup; Josh Asuncion coordinates config changes with CETS. Links the cluster tutorial deck.

## Tutorial:

[📄 Litt Lab Cluster Tutorial.pptx](../../assets/compute/slurm-on-finkel-configuration-and-limits/01-litt-lab-cluster-tutorial.pptx)

## Current Configurations on Finkel:

*   **Governance model for deciding what changes to make for the lab**
    *   Josh Asuncion will coordinate with CETS on any changes that are needed
*   **Number of shards per GPU**
    *   There are a total of 8 shards available on [finkel.seas.upenn.edu](http://finkel.seas.upenn.edu/), 4 per GPU.
        *   Each shard is the smallest unit. You only need to request a shard to run jobs on a GPU. Jobs which do not request a shard can run (using CPU/memory but not a GPU) when all of the shards have been claimed.
        *   Estimate for the smallest typical job that users would run is 12GB. On a single L40S with 48GB that would be 4 x 12GB shards per card, so 8 of those jobs could fit simultaneously on Finkel. Currently configured is 8 total, 4 per GPU card.
*   **Maximum time limit per job**
    *   There is a 14 day time limit on any job.
*   **Maximum number of jobs per user in queue / running**
    *   No user can have more than 100 jobs at once in the queue.
*   **Scratch space management**
    *   There is a tool which automatically removes files older than 21 days from the `/scratch` directory.
*   **Allowed users**
    *   `cntgroup` usergroup (all CNT users)
