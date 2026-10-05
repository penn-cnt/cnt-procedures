---
title: "Azure Portal & Storage Tiers"
stage: "Data Governance"
roles: [pipeline, data-rc]
order: 3
---

# Azure Portal & Storage Tiers

!!! abstract "What this page tells you"
    CNT Azure storage lives in the cntlitt container at portal.azure.com (log in with PennMedicine account). Explains hot, cool (30-day minimum), cold (90-day), and archive (180-day) blob tiers and their storage-vs-access cost tradeoffs.

[portal.azure.com](http://portal.azure.com)
login with PennMedicine (asuncioj)
cntlitt storage container


*   **Hot tier** - An online tier optimized for storing data that is accessed or modified frequently. The hot tier has the highest storage costs, but the lowest access costs.
*   **Cool tier** - An online tier optimized for storing data that is infrequently accessed or modified. Data in the cool tier should be stored for a minimum of **30** days. The cool tier has lower storage costs and higher access costs compared to the hot tier.
*   **Cold tier** - An online tier optimized for storing data that is rarely accessed or modified, but still requires fast retrieval. Data in the cold tier should be stored for a minimum of **90** days. The cold tier has lower storage costs and higher access costs compared to the cool tier.
*   **Archive tier** - An offline tier optimized for storing data that is rarely accessed, and that has flexible latency requirements, on the order of hours. Data in the archive tier should be stored for a minimum of **180** days.

[https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
Access tiers for blob data - Azure Storage | Microsoft Learn
Azure storage offers different access tiers so that you can store your blob data in the most ccostly-effective manner based on how it's being used. Learn about the hot, cool, cold, and archive access ...
