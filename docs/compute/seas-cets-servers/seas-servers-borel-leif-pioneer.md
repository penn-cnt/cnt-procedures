---
title: "SEAS Servers: Borel, Leif, Pioneer"
stage: "Data Analytics"
roles: [analyst, pipeline]
order: 1
---

# SEAS Servers: Borel, Leif, Pioneer

!!! abstract "What this page tells you"
    Borel is the CETS Linux compute server (ssh with PennKey); Leif is the file store you mount, which needs a SEAS Local Password set at accounts.seas.upenn.edu; Pioneer is Borel's GPU. No PHI on any. Access lasts while your SEAS account is active.

### Littlab Servers (Borel, Leif, Pioneer)

**Borel**: Linux compute server under CETS, not PMACS. We own this, and no other group can access it. No PHI data is allowed here.
Borel and Leif are essentially two parts of one system -- Leif is the server/drive where you store your data/files (you mount it and open it in Finder / File Explorer), and Borel is the linux compute server where you run your code/computations (you ssh into this), and Borel and Leif are connected. For example, in Leif when you create a file in your USERS/pennkey folder, it will show up in Borel in `cd /users/pennkey`

I don't think people need to set their SEAS local password to SSH into Borel. They use their PennKey username and password for that. Specifically it looks like we're using Kerberos which authenticates against the campus Kerberos servers.

       Are you using your PennKey password or your SEAS Local Password? You need to use your SEAS Local Password, which is a separate password pretty much just for SMB. Unfortunately we can't get the SMB server to use PennKeys for authentication.

       To set your SEAS Local Password, go to [https://accounts.seas.upenn.edu](https://accounts.seas.upenn.edu/) and log in with your PennKey. Then click "SEAS local password" on the left and follow the instructions.

**Pioneer**: The GPU attached to borel. No PHI is allowed here.

*   Pioneer *(retired page)*

### Software

*   Matlab *(retired page)*

### Security and Best Practices

*   CETS Security Presentation Fall 2023:

[📄 seascetssecurity.pptx](../../assets/compute/seas-servers-borel-leif-pioneer/01-seascetssecurity.pptx)
        Sorry for the delay. Their SEAS account has been renewed for another year. That will grant them access to SEAS resources. As for access to the Littlab servers they have no expiration on their access so as long as their SEAS account is active, they will be able to access those servers.
