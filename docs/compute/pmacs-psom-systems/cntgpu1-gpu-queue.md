---
title: "cntgpu1 GPU Queue"
stage: "Data Analytics"
roles: [analyst, pipeline, data-rc]
audit: merge
order: 4
---

# cntgpu1 GPU Queue

!!! abstract "What this page tells you"
    To use the CNT GPU queue (cntgpu) on the PMACS LPC, be on a PMACS/UPHS network or VPN and ssh to scisub7.pmacs.upenn.edu with PMACS credentials. Includes PMACS wiki links for LPC access, LSF batch scheduling, modules, VPN setup, and GPU job requests.

### LPC and cntgpu queue

####################################

You can now use your PMACS credentials to access the LPC and the cntgpu queue. You will need to be on supported PMACS or UPHS network to access the cluster. This includes the PMACS and UPHS VPN's or wired PMACS or UPHS networks on campus. The submit host for CNT is
[scisub7.pmacs.upenn.edu](http://scisub7.pmacs.upenn.edu/)
Once on a supported network you can connect to scisub7 through ssh.

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

GPU jobs and requesting GPU resources in LPC
[https://wiki.pmacs.upenn.edu/public/GPU\_in\_LPC](https://wiki.pmacs.upenn.edu/public/GPU_in_LPC)
