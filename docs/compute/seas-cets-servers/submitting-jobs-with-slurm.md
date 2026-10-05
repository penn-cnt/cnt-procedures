---
title: "Submitting Jobs with SLURM"
stage: "Data Analytics"
roles: [analyst, pipeline]
order: 4
---

# Submitting Jobs with SLURM

!!! abstract "What this page tells you"
    How and when to run jobs on the Finkel GPU via SLURM from Borel or Pioneer: salloc for interactive jobs, sbatch with #SBATCH headers for batch jobs, squeue for status, with example shell and Python scripts. Finkel cannot be ssh'd into directly.

“I have the scheduler set up. It could use more than basic testing but I was able to submit both batch jobs (“sbatch”) and interactive jobs (with “salloc”) to log into Finkel interactively. Jobs can be submitted from either Borel or Pioneer, though the various required paths will only be set up for new login sessions (e.g. if you are already logged in you won’t be able to run those commands).
    Right now there are jobs running on both GPUs of Finkel presumably started by someone who logged in. SLURM won’t work properly until it is the only thing which can control access to those GPUs and other system resources so it probably does not make sense to start using it just yet. In addition, I should cut off SSH access to Finkel. People who want to log in to Finkel should run “salloc” on Borel or Pioneer to do so.
    I believe that Dan Widyono is working with you to schedule a talk where he explains the basics of SLURM. We have a write-up on how to use SLURM here: 

[hpc.seas.upenn.edu](https://hpc.seas.upenn.edu/home/mp-clusters/how-to-use-mp-clusters-slurm/)

 . SLURM’s documentation is here: 

[slurm.schedmd.com](https://slurm.schedmd.com/documentation.html)

Hi everyone, attached is the tutorial from CETS on the servers, job scheduler, and other resources. I am pulling mostly from advice from CETS and practical experience (not an expert!), so consider this as more of a conversation starter.
If you are having any issues with the servers, consider this channel as the starting point for getting support.
**Should I use the job scheduler?**
There are few main reasons you might want to submit scripts to the SLURM job scheduler:

1. You want to run many scripts at once on borel/pioneer
2. You want to run jobs that are quite long (>1 hour) and require a lot of memory (>16GB)
3. You want to take advantage of the finkel GPU to run GPU-compatible scripts.
In most cases, it’s perfectly okay to run scripts without submitting them as a job. There is quite a lot of RAM available on borel/pioneer and CETS is adding generous per-user memory limits (128GB). However, if too many people are running large jobs at once interactively (i.e., on the command line without the job scheduler), it can cause borel/pioneer to “freeze”, preventing users from reading/writing files or running scripts.
**How do I submit a script as a job?**
Here are two example use cases of how you could run a script called [`script.sh`](http://script.sh) with the job scheduler, which uses the computing resources on [finkel.seas.upenn.edu](http://finkel.seas.upenn.edu/).
You can check the status of your job with the `squeue` command.

1. **From the command line**
`salloc --gres=shard:1 --cpus-per-task=1 --mem=8GB`

*   This command creates an interactive job with the following resources
    *   1 GPU shard (currently the 2 GPUs are divided into 8 shards so more users can use the GPU at once)
    *   1 CPU Core
    *   8GB of RAM
`./script.sh`
If resources are available, the script will begin running. The job will end when you close the terminal.

2. **Within a script**
Requested resources are specified in the header of the script itself
Even though this requires an extra script, this method is recommended because you can close your terminal and your job will continue running to completion.
It’s helpful to specify where you want your logs to be saved so you can check that it ran correctly
`run_script.sh`

```bash
#!/bin/bash

## Define and create directory to save logs
logs_dir=logs; mkdir -p ${logs_dir}

## Define how you want your logs to be named

## %j --> SLURM JOB ID

## .o --> stdout (primary output stream for script)

## .e --> stderr (separate output stream for errors, diagnostics)
logs_output=${logs_dir}/script_job-%j.o
logs_error=${logs_dir}/script_job-%j.e

## Submit job
sbatch --output=${logs_output} --error=${logs_error} script.sh
```

[`script.sh`](http://script.sh)

```bash
#!/bin/bash
#SBATCH --gres=shard:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB

## Create an empty .txt file
touch hello_world.txt
```

If you want to run a non-shell script, such as a Python script called [`script.py`](http://script.py) , you just need to adjust the interpreter at the top of the script:
[`script.py`](http://script.py)

```sql
#!/usr/bin/python3
#SBATCH --gres=shard:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB

## Create an empty text file
open('hello_world.txt', 'a').close()
```

[📄 Litt Lab Cluster Tutorial.pptx](../../assets/compute/submitting-jobs-with-slurm/01-litt-lab-cluster-tutorial-1.pptx)

Also, CETS just shared an overview of the servers and how it relates to the SLURM job scheduler, if helpful
> First, Sauce is your fileserver. There are various data sets there such as “data” and “users”. These are accessed on Borel, Pioneer, and Finkel at /mnt/sauce/littlab or through symlinks like /data, /users, etc.  
>     Before we set up SLURM, Borel, Pioneer, and Finkel were standalone servers. People could SSH into all of them and run jobs on the server they SSHed in to. The “connection” between them was that the files on Sauce were accessible in the same places on each of them, namely /mnt/sauce/littlab, or /admin, /data, etc.  
>     When I set up SLURM I only made Finkel a SLURM-managed server. I believe we discussed which servers to manage with SLURM at the time I set it up. Anyway, now you cannot SSH into Finkel. However you can SSH into Borel and Pioneer and use SLURM commands to schedule jobs on Finkel. You cannot use SLURM to schedule jobs on Borel or Pioneer but you can run jobs directly on Borel and Pioneer just like you could before.
