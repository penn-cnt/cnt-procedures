---
title: "BSC Cluster"
stage: "Data Analytics"
roles: [analyst, pipeline, data-rc]
order: 3
---

# BSC Cluster

!!! abstract "What this page tells you"
    Connect to the BSC imaging cluster: turn on the PMACS VPN, ssh pennkey@bscsub.pmacs.upenn.edu, then cd to /project/davis_group, davis_group_1, gugger, or gugger_1. Lists queue limits (bsc_interactive 4 jobs/48h, bsc_normal 64/12h, bsc_short 256/1h, bsc_long 40/30d) and notes bscsub2 works for VSCode editing only.

## Penn Brain Science Center (BSC) Cluster

### Resources

*   Wiki: [https://brainsciencecenter.github.io/bscLPC/](https://brainsciencecenter.github.io/bscLPC/)

### How to Connect

1. Turn on Ivanti Secure Access PMACS VPN (formerly Pulse Secure PMACS VPN)
    1. PennMed network access will be required to access BSC. This means that you will need to use the PMACS VPN for remote connections. See PMACS VPN ([PMACS VPN](pmacs-vpn.md)) for further details
2. SSH in the terminal
    1. New job submission and file transfer host: [scisub.pmacs.upenn.edu](http://scisub.pmacs.upenn.edu/) will be replaced by [bscsub.pmacs.upenn.edu](http://bscsub.pmacs.upenn.edu/). This means that going forward, to connect to BSC you will need to run:

```plain
 ssh pennkey@bscsub.pmacs.upenn.edu 
```


3. Login with your PennKey and Password
4. BSC is a shared space. To access CNT project folders:
    1. `cd /project/davis_group`
    2. `cd /project/davis_group_1`
    3. `cd /project/gugger`
    4. `cd /project/gugger_1`

Note: BSC is also accessible in cnt1 via SSH.

#### Dec 9, 2022 Update

> BSC Downtime  
>   
> The BSC PMACS Virtual is scheduled for downtime on 12/12 and 12/13  
>   
> The downtime will remove the 10TB limit for project directories and also support a new CentOS 7 head node for BSC users with ssh and https outbound access.  
>   
> Queue Restrictions  
>   
> In order to prevent oversubscription of the BSC compute nodes, the following queue limits are now in place:  
>   
>   


| Queue | Max Jobs/User | Max Jobs/Queue | Max Runtime |
| ---| ---| ---| --- |
| bsc\_interactive | 4 | \- | 2880 Minutes (48 Hours/2 Days) |
| bsc\_normal | 64 | \- | 720 Minutes (12 Hours) |
| bsc\_short | 256 | \- | 60 Minutes |
| bsc\_long | 40 | 160 | 720 Hours (30 Days) |

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> \*             ATTENTION: LPC MAINTENANCE                \*  
> \*                                                       \*  
> \*            Monday, December 12th (8:00am)             \*  
> \*                         to                            \*  
> \*            Tuesday, December 13th (4:00pm)            \*  
> \*                                                       \*  
> \*        We will work to complete the maintenance       \*  
> \*        and restore services as soon as possible.      \*  
> \*                                                       \*  
> \*  IMPORTANT: After this maintenance window \*  
> \*            the LPC will ONLY be accessible            \*  
> \*            from Penn Medicine networks.               \*  
> \*                                                       \*  
> \*            Please note the following new              \*  
> \*         job submission and file transfer hosts:       \*  
> \*                                \*  
> \*            -General: [scisub7.pmacs.upenn.edu](http://scisub7.pmacs.upenn.edu/)          \*  
> \*            -CCEB: [ccebsub.pmacs.upenn.edu](http://ccebsub.pmacs.upenn.edu/)             \*  
> \*      -BSC: [bscsub.pmacs.upenn.edu](http://bscsub.pmacs.upenn.edu/)    \*  
> \*      -FTDC: [ftdcsub.pmacs.upenn.edu](http://ftdcsub.pmacs.upenn.edu/)  \*  
> \*                                                       \*  
> \*       These hosts each combine the functionality  \*  
> \*            of scisub, sciget, and transfer.           \*  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

####################################

Your PMACS account has been created and you will be receiving a email shortly from Secure Share that will contain a temporary password and instructions on changing it. Your username will be your PennKey name. If you do not receive an email, you can log into Secure Share directly using your Pennkey credentials.
[https://secureshare.apps.upenn.edu/](https://secureshare.apps.upenn.edu/)

Once your password is reset you can use your PMACS credentials to access the LPC and the BSC queues. You will need to be on supported PMACS or UPHS network to access the cluster. This includes the PMACS and UPHS VPN's or wired PMACS or UPHS networks on campus. The submit host for BSC is
[bscsub.pmacs.upenn.edu](http://bscsub.pmacs.upenn.edu/)
Once on a supported network you can connect to bscsub through ssh.

Below are some links to our wiki for connecting to and using the LPC.

####################################
For information about connecting to and accessing the LPC, please see our wiki page (PennKey Authentication).
[https://wiki.pmacs.upenn.edu/pub/LPC](https://wiki.pmacs.upenn.edu/pub/LPC)

If you are not familiar with our scheduling software, this section may be helpful.
[https://wiki.pmacs.upenn.edu/pub/LSF\_Basics](https://wiki.pmacs.upenn.edu/pub/LSF_Basics)
[https://wiki.pmacs.upenn.edu/pub/Batch\_Computing](https://wiki.pmacs.upenn.edu/pub/Batch_Computing)

Applications are installed on a central shared directory so the applications are available to all the hosts in our cluster. "modules" can be used to see what is available and to load or unload software packages.
[https://wiki.pmacs.upenn.edu/pub/LPC#Modules](https://wiki.pmacs.upenn.edu/pub/LPC#Modules)

VPN download and configure
[https://www.med.upenn.edu/dart/vpn-instructions.html](https://www.med.upenn.edu/dart/vpn-instructions.html)

Configuring 2 factor authentication for VPN.
[https://www.isc.upenn.edu/how-to/two-step-verification-getting-started](https://www.isc.upenn.edu/how-to/two-step-verification-getting-started)

For complete details, see:
[https://helpdesk.pmacs.upenn.edu/userui/ticket?ID=571802](https://helpdesk.pmacs.upenn.edu/userui/ticket?ID=571802)

### \[TICK:617139\] Help reh8823 using VSCode to access BSC Cluster

\-+-+- Please reply above this line to add a comment -+-+-
Comment Submitted.

David Weise ([dweise@upenn.edu](mailto:dweise@upenn.edu)) on 2025-07-14 14:32:49
Comment:
Hi,
We made a new bscsub, called bascsub2. It is a RHEL9 server and the new VSCode should be able to connected to it. However, you may only do editing and connections to bscsub2 via VScode because the execute hosts are still Centos 7. So if you want to submit jobs or do more complex things, please do it on bscsub.
\--David
