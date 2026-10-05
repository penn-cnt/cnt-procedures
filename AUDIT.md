# Audit of the procedures, October 2026

*This audit was carried out when the procedures were imported into the NeuroBridge Lab wiki, from the point of view of a new member of that lab. The "Rel." column therefore says how NeuroBridge uses a page (core: their people run it; shared: CNT infrastructure they depend on; clinical coverage: CRC work they only cover). For the CNT the useful columns are Stale, New, Action and Note, and the questions at the end, most of which only CNT staff can answer.*

Every page was read in full and scored against one question: could a new member of NeuroBridge, with no background in clinical neuroscience, follow it alone? The tables give one row per page. *Rel.* is who the page is for (core: our people do this; shared: CNT or Penn infrastructure we depend on; clinical coverage: participant-facing CNT work we only cover; reference: read once; retire). *Stale* and *New* run from 0 to 3: the risk that the page is out of date, and how far a newcomer gets unaided (3 is all the way). *Action* is the recommendation. The front matter of every procedure now carries a `scope` field and, where the audit recommends it, `audit: merge` or `audit: retire`; the site shows a banner for each, and the map has a Scope view.

Procedures: 148. Scope: core 56, shared infrastructure 23, clinical coverage 45, reference 9, retire 15. Stale risk 2 or 3: 123. Newcomer score 0 or 1: 84. Recommended actions: merge 45, rewrite 35, tighten 29, reframe-as-reference 17, retire 14, needs-pi 6, keep 2.

## What was fixed immediately

Secrets and identifiers that survived the import were removed on 5 October 2026 and the repository history was rewritten: a Pennsieve API token, the Natus VNC password (in two machine-written summaries), the pedro account password, the HUP6 door codes and scanner-laptop login, the neuropsych flash-drive password, a fund code, a session key in a URL, a patient's name in a withheld-screenshot note, a personal mobile number, coded subject identifiers in example paths, residue text from the previous knowledge base, one mention of it by name, and two links that pointed at the wrong page. `scripts/check_content.py` now fails the build on each of these patterns. Still to decide: the personal mobile numbers on *Important contacts*, staff PennKeys and names visible in screenshots, an AWS account number in the ieeg.org restart runbook, internal IP addresses, two Penn+Box folders shared as "anyone with the link", and non-defaced MRIs copied to SEAS servers (see the questions at the end).

## What a newcomer meets

The wiki is honest about what it contains but not about whom it is for. It was written over several years by and for the CNT's clinical research coordinators, and it still reads that way: 45 of the 149 procedures are participant-facing work (consenting, scanner day, bedside testing, reimbursement, scheduling trackers) that nobody in NeuroBridge performs, a further 23 describe CNT or Penn infrastructure the lab uses but does not run, and only 56 are things our own people do. Until this audit no page said which was which, so a new PhD student opening *Imaging* met eleven scanner-day pages before the four that concern them. The pages are also personal notes rather than procedures. They name people by first name (Josh, Gloria, Carolyn, Naseem, Mariam, Joel, Cat, Gabby, Marissa, Lisa, Steve) where a newcomer needs a role; they carry dates that have passed (an Azure token that expired in March 2026, a 7T protocol that ended in February, a server crash from May, a 2022 downtime banner, a 2023 VPN migration notice with empty steps); and almost none says why the step is done, what you need before you start, how you know it worked, or whom to ask. Of 149 procedures, 127 carry a stale-risk score of 2 or 3 and 125 would not get a newcomer to the end unaided.

A new data research coordinator can find the systems but not the rules. No Data page states which systems may hold identified data, and the pages contradict the lab's own rule: *Data storage locations* calls Borel "main storage for limited and anonymized EEG data", the rsync pages copy from cnt1 to Borel with no de-identification gate, the computing schematic and *PMACS overview* say the BSC cluster allows no PHI while the glossary says it does, and the reconstruction pages copy non-defaced T1 images to Leif and to a Box folder shared with anyone who has the link. The one route to every account, *Submitting CETS and PMACS helpdesk tickets*, lists CNT sponsors, a Neurology department code and a CNT IRB form, so the coordinator cannot tell who files for them or which group they join. The pipeline they must learn first, *Processing for ieeg.org*, is a 2,245-word command transcript in which the same five steps are pasted four times with small unexplained differences, struck-through commands, a "need to update with new scripts" flag and a contradiction about whether a file is deleted. Three different EDF de-identification scripts appear across two themes with no statement of which is current or what each removes.

A new PhD student from computer science meets the vocabulary before the explanation. EMU, Natus, iEEG, mef, RID and HUP numbers appear from the first paragraph of most pages and are defined only in the glossary, which nothing pointed to. There is no page that explains what the lab's data is and how it came to exist, no page on downloading a de-identified dataset from ieeg.org as a consumer rather than an uploader, and *Pennsieve downloader* never says where the script lives. The compute path exists (Borel over SSH, Leif, SLURM) but the SLURM page opens with a CETS email saying the scheduler "could use more than basic testing", and there was no page of things you must never do. The student would most likely ask a labmate within ten minutes and never return.

A master's student working on MRI-derived features finds the four workflows that matter to them, RADAR pulls, scan landing, DICOM to NIfTI and electrode reconstruction, scattered among scanner-day checklists, consent scripts and billing reviews. Reconstruction runs to about 7,200 words across five pages that repeat each other, with two routes and no rule for choosing. The NIfTI de-identification page assumes a BIDS conversion procedure that does not exist, and there is no defacing policy, no coding conventions page and no statement of where derived data should be written.

A postdoc arriving from physics to work on stroke or brain injury finds that only the Data and Compute themes apply to them unchanged; *What this lab is* says the stroke and TBI procedures are "to be added", which is true and should stay visible. The IRB and personnel pages they will be asked about are the CNT's, by first name, with one link that pointed at a page about mounting a file server. *Contributing*, the style guide and the SOP template are good and are the right place to send them when they build their first pipeline.

What the site needed, and now has, is routing: a *Start here* page that tells each of these four people what to read and in what order, a banner on every page that says whether it is ours, shared, reference or clinical coverage, a scope view on the map, and the five rules a newcomer must not break stated once, prominently. What it still needs is in the tables below: about fifty merges that would take the six themes from 149 procedures to roughly a hundred, fifteen retirements, a one-page data-governance statement that resolves the contradictions above, and a dozen pages that do not exist yet: a REDCap project catalogue, identifier mapping (MRN, RID, HUP, subject IDs), getting data out of REDCap, Data Structure v1.0 and the BIDS layout, how collaborating sites deliver data, a defacing policy, a BIDS conversion procedure, a NeuroBridge onboarding matrix by role, requesting cnt1 and cnt-fs access, required trainings, and a consumer's guide to ieeg.org and Pennsieve.


## Data

## Five biggest newcomer problems

1. **A live credential and personal identifiers remain.** "Uploading from cnt1 to Pennsieve" prints a Pennsieve `api_token`/`api_secret` (`a62ced44-…`); its abstract even announces it, and no "Credential removed" box was applied. Former members' logins (`asuncion`, `mjosyula`, `jchin09`, `bach2`, `asuncioj`) and real coded subject IDs (`RID1092`, `RID1038`, `HUP298`) sit in example paths and screenshots.
2. **The PHI boundary is never stated.** No Data page says which systems may hold identified data. The rsync pages show cnt1 → Borel copies with no gate, and "Data Storage Locations" calls Borel "main storage for limited … EEG data", contradicting the rule that SEAS servers never hold PHI.
3. **Pages are command histories, not procedures.** Almost none says why, who, when, what you need first, or how you know it worked. The 3T/7T page promises child pages that moved to Imaging; the rclone page depends on a retired setup SOP; "Pennsieve Downloader" never says where the script lives; the NIfTI page still says "(Mariam needs to update path)"; one rsync page states the trailing-slash rule backwards.
4. **Three divergent EDF de-identification scripts, no standard.** `edf_deid_wrapper.sh` (strips all annotations), `edf_headers/anonymize_edf.sh`, and the newer `edf_anonymize/anonymize_edfs.sh` with date shifting appear across Data and Electrophysiology with no statement of which is current or what each removes. "Limited vs anonymized", RID → HUP renumbering and the 1/1/2000 date shift are defined only under Compute.
5. **Expired or unowned prerequisites.** The Azure SAS token "expires on 03/15/2026" (past). The storage account is Brian Litt's `cntlitt`; BSC examples use `davis_group`; Pennsieve workspace ownership is unspecified; every page has empty `owner` and `last_reviewed` fields.

## Merge or go

Merge the two rsync pages; merge the two Pennsieve upload pages (laptop vs `module load pennsieve` on cnt1); merge "De-Identifying EDFs" and "EDF Headers" into one page and leave Mxene export/upload to Electrophysiology; fold "Azure Portal & Storage Tiers" into the scripts page; fold the 3T/7T stub into the storage table. Retire the AWS bucket roster to a CETS-owned spreadsheet, keeping a three-line note on where ieeg.org uploads land. No page names a legacy KB tool, though one carries a "You do not have access to this Doc" embed fragment.

## Missing pages a newcomer would expect

A one-page data-governance rule (what may live where, what must happen before data crosses); Data Structure v1.0 and the BIDS layout; how collaborating sites deliver data and where it lands; key custody (RID ↔ HUP ↔ identity, who holds it); a "may this leave PMACS?" checklist; and an archive inventory.

## First-read order

Data index (with a framing paragraph) → Data Storage Locations (as a table) → De-identification overview → Moving data (rsync, then rclone) → Pennsieve access rules → Pennsieve upload and download → Archiving and unarchiving.


| Page | Rel. | Stale | New | Action | Note |
|---|---|---|---|---|---|
| [Data Storage Locations](docs/data/storage-locations/data-storage-locations.md) | core | 2 | 1 | rewrite | rewrite: as a table: system / what lives there / PHI allowed? / who grants access / how to reach it (link) |
| [Where 3T and 7T Scans Are Stored](docs/data/storage-locations/where-3t-and-7t-scans-are-stored.md) | retire | 2 | 0 | merge | duplicate of `flywheel-cnt-fs-3t.md`; merge: into Data Storage Locations as two rows (3T raw DICOM: Flywheel presurgicalEpilepsy project … |
| [PennBox](docs/data/storage-locations/pennbox.md) | shared | 2 | 1 | needs-pi | reframe: as 'Penn+Box in this lab': what it is for, the lab's top-level folders, who owns them, that it is PHI-approved, how external sit… |
| [Moving Data Across cnt-fs, cnt1, BSC, Borel & Leif](docs/data/moving-data/moving-data-across-cnt-fs-cnt1-bsc-borel-and-leif.md) | core | 2 | 1 | merge | merge: absorb 'Moving Imaging Data Across CNT Servers' into this page as 'Moving data between servers (rsync)' |
| [Moving Imaging Data Across CNT Servers](docs/data/moving-data/moving-imaging-data-across-cnt-servers.md) | retire | 3 | 0 | merge | duplicate of `moving-data-across-cnt-fs-cnt1-bsc-borel-and-leif.md`; merge: carry the one new fact (cnt-fs imaging paths /mnt/cnt-fs/imag… |
| [Transferring Files from Box to cnt-fs (rclone)](docs/data/moving-data/transferring-files-from-box-to-cnt-fs-rclone.md) | core | 3 | 1 | rewrite | add: the one-time rclone setup section (rclone config -> box -> authorize on a machine with a browser -> paste token) so the page stands … |
| [Archiving EEG Data to Azure](docs/data/archiving-azure/archiving-eeg-data-to-azure.md) | core | 2 | 2 | tighten | add: a 'When to archive' line and the decision owner |
| [cnt1 Scripts for Azure Archiving & Unarchiving](docs/data/archiving-azure/cnt1-scripts-for-azure-archiving-and-unarchiving.md) | core | 2 | 2 | tighten | reorder: put the four scripts in a table (name / purpose / input / output dir / log) at the top, then the unarchive procedure |
| [Azure Portal & Storage Tiers](docs/data/archiving-azure/azure-portal-and-storage-tiers.md) | retire | 3 | 0 | retire | duplicate of `cnt1-scripts-for-azure-archiving-and-unarchiving.md`; retire: the tier list already exists on the scripts page |
| [Pennsieve Data Access Rules](docs/data/sharing-pennsieve-and-ieeg-org/pennsieve-data-access-rules.md) | core | 2 | 1 | needs-pi | rewrite: as a decision table: consent status x data type -> allowed destination (Discover public / controlled / internal only) x key cust… |
| [Uploading to Pennsieve Locally](docs/data/sharing-pennsieve-and-ieeg-org/uploading-to-pennsieve-locally.md) | core | 2 | 2 | merge | merge: with 'Uploading from cnt1 to Pennsieve' into one page with two 'where you run it' variants (laptop vs cnt1 module load) |
| [Uploading from cnt1 to Pennsieve](docs/data/sharing-pennsieve-and-ieeg-org/uploading-from-cnt1-to-pennsieve.md) | core | 3 | 1 | rewrite | duplicate of `uploading-to-pennsieve-locally.md`; URGENT cut: the api_token/api_secret values; rotate that key; add the 'Credential remov… |
| [Pennsieve Downloader](docs/data/sharing-pennsieve-and-ieeg-org/pennsieve-downloader.md) | core | 3 | 1 | rewrite | add: script location (GitHub repo and commit) and requirements |
| [AWS Bucket Numbers (ieeg.org / PREVeNT)](docs/data/sharing-pennsieve-and-ieeg-org/aws-bucket-numbers-ieeg-org-prevent.md) | retire | 3 | 0 | retire | retire: move the roster to a spreadsheet owned by whoever administers ieeg.org uploads (CETS / John Frommeyer) |
| [De-Identifying EDFs](docs/data/de-identification/de-identifying-edfs.md) | core | 2 | 1 | merge | merge: with 'De-Identifying EDF Headers' into one page 'De-identifying EDF files' with a decision line: keep annotations (anonymize_edfs.… |
| [De-Identifying EDF Headers](docs/data/de-identification/de-identifying-edf-headers.md) | core | 3 | 1 | merge | duplicate of `anonymize-and-upload-edfs-to-ieeg-org.md`; merge: the generic 'anonymize EDF header' step into one De-identifying EDF files… |
| [De-identifying NIfTI Headers](docs/data/de-identification/de-identifying-nifti-headers.md) | core | 3 | 1 | rewrite | rewrite: state what deid_json.sh does (fields removed), its true path, the queue format, the output, and a verification command (e.g., gr… |

## Compute

**Five biggest problems for a newcomer.**

1. The theme never answers its own question. `compute/index.md` asks "What do I run things on, and how do I get in?", but no page states the first rule: identified data only on cnt1/cnt-fs/BSC behind the PMACS VPN; de-identified work on Borel/Leif/Finkel behind GlobalProtect; code on GitHub, never data. The page meant to carry this, the CNT Computing Schematic, is a "WORK IN PROGRESS" table with an unlabeled column, retired-page stubs and a BSC row marked "No PHI allowed", contradicting the lab-manual glossary (BSC PHI permitted, 2026-09-20). PMACS Overview repeats the contradiction.

2. About half the body text is pasted email, Slack and ticket residue frozen mid-transition: the SLURM page opens with CETS saying the scheduler "could use more than basic testing"; the BSC page carries a 2022 downtime banner and a 2025 ticket thread; the VPN page is the 2023 Pulse-to-Ivanti notice with empty connect steps. Named CNT people (Josh, John Frommeyer, Curt) stand in for roles.

3. The access path is CNT's, not NeuroBridge's. The tickets page, the only route to every account, lists sponsors "Kathryn Davis / Brian Litt / Flavia Vitale, Dept: Neurology", a CNT IRB form, Littlab usergroups and "Contact Josh Asuncion" three times. A newcomer cannot tell who files for them or which group they join.

4. No page gives prerequisites in order or a verification step. The chain IRB, PMACS account, VPN, VDI, cnt1 is scattered across four pages; nothing says how you know a login or job worked.

5. Dead links and duplication: Software Tools Index is five retired pages; VDI/cnt-fs/cnt1 has three dead links of four; the Borel SSH page cites a "Migration to Leif" page absent from the wiki; the PMACS link block is pasted on three pages.

**Merge or go.** Retire Linux Command Shortcuts (move its group-ownership tip to the BSC page; it also dumps 29 PennKeys and a sub-RID path) and Software Tools Index. Merge SLURM limits into the SLURM how-to, the LPC welcome email and cntgpu1 into a rewritten PMACS Overview, and Hayden Hall into the Operations remote-access page. Reframe the 4,166-word AWS @ Penn guide as a link plus ten lab-specific lines. Fold the electrophysiology "Restarting ieeg.org" stub into the AWS restart runbook, the only page a newcomer could follow alone.

**Missing pages:** "Which system for which data" (schematic merged with Data > Storage Locations); "Day-one accounts and who files them"; "Set up your environment on Borel"; "The three VPNs"; an LSF quick start for BSC.

**First-read order:** rewritten schematic; access matrix from the tickets page; PMACS VPN, Borel SSH, Leif mount; SLURM how-to with limits; BSC; AWS only if you maintain ieeg.org.


| Page | Rel. | Stale | New | Action | Note |
|---|---|---|---|---|---|
| [Overview of CNT Systems](docs/compute/overview/overview-of-cnt-systems.md) | core | 3 | 1 | rewrite | split: move the Data Sharing Crash Course (HUP vs RID, limited vs anonymized, date shift to 2000-01-01) to its own page under Data and li… |
| [CNT Computing Schematic](docs/compute/overview/cnt-computing-schematic.md) | reference | 3 | 0 | rewrite | rewrite: one row per system (cnt1, cnt-fs, VDI, REDCap, BSC, cntgpu1, Borel, Leif, Pioneer, Finkel, Pennsieve, ieeg.org, Penn+Box, GitHub… |
| [VDI, cnt-fs and cnt1](docs/compute/overview/vdi-cnt-fs-and-cnt1.md) | shared | 2 | 0 | rewrite | rewrite: as 'cnt1 and cnt-fs: what lives where' — table /projects/<dir> / contents / owning user group (cnt_3t_group, cnt_7t_group, cnt_i… |
| [Hayden Hall UPHS Computers](docs/compute/overview/hayden-hall-uphs-computers.md) | shared | 3 | 1 | merge | duplicate of `remote-access-to-the-hayden-hall-uphs-computer.md`; merge: with operations/access-and-accounts/remote-access-to-the-hayden-… |
| [SEAS Servers: Borel, Leif, Pioneer](docs/compute/seas-cets-servers/seas-servers-borel-leif-pioneer.md) | core | 2 | 1 | rewrite | rewrite: five-row table — Borel (CPU, ssh), Pioneer (GPU, ssh), Finkel (GPU, SLURM only), Leif (SMB view of the same storage), Sauce (fil… |
| [Accessing Borel over SSH](docs/compute/seas-cets-servers/accessing-borel-over-ssh.md) | core | 2 | 2 | tighten | cut: the dangling 'Open' and the 'future instructions' note |
| [Mounting Leif over SMB](docs/compute/seas-cets-servers/mounting-leif-over-smb.md) | core | 1 | 2 | tighten | add: list of Leif volumes and what each maps to on Borel |
| [Submitting Jobs with SLURM](docs/compute/seas-cets-servers/submitting-jobs-with-slurm.md) | core | 2 | 2 | tighten | cut: the first pasted CETS email and the 'consider this channel' line |
| [SLURM on Finkel: Configuration & Limits](docs/compute/seas-cets-servers/slurm-on-finkel-configuration-and-limits.md) | core | 2 | 2 | merge | duplicate of `submitting-jobs-with-slurm.md`; merge: into submitting-jobs-with-slurm.md as a 'Limits (as of <date>)' section |
| [PMACS Overview](docs/compute/pmacs-psom-systems/pmacs-overview.md) | shared | 3 | 1 | rewrite | rewrite: a four-row table LPC / BSC / HPC / cntgpu1 — what it is, PHI allowed?, scheduler (LSF), submit host, who in the lab uses it, how… |
| [PMACS LPC Welcome Email](docs/compute/pmacs-psom-systems/pmacs-lpc-welcome-email.md) | shared | 2 | 2 | merge | duplicate of `bsc-cluster.md`; merge: into the tickets page as 'After approval: activate your PMACS account' — (1) open the Secure Share … |
| [BSC Cluster](docs/compute/pmacs-psom-systems/bsc-cluster.md) | core | 3 | 1 | rewrite | keep: Resources link, How to Connect steps 1-4, the queue table (re-dated), and one sentence on bscsub2 for VS Code editing only |
| [cntgpu1 GPU Queue](docs/compute/pmacs-psom-systems/cntgpu1-gpu-queue.md) | shared | 2 | 1 | merge | duplicate of `pmacs-overview.md`; merge: into pmacs-overview.md as a six-line cntgpu1 row/section: what it is, who may use it, how to get… |
| [PMACS VPN](docs/compute/pmacs-psom-systems/pmacs-vpn.md) | core | 3 | 1 | rewrite | rewrite: (1) when you need it; (2) install from med.upenn.edu/dart/vpn-instructions.html; (3) connect: open Ivanti, server remote.pmacs.u… |
| [AWS @ Penn: Getting Started](docs/compute/cloud-aws/aws-penn-getting-started.md) | reference | 2 | 2 | reframe-as-reference | reframe: replace the body with a link to ISC's canonical guide plus a ten-line lab summary — account name(s), region us-east-1, bucket pr… |
| [Restarting the ieeg.org AWS Server](docs/compute/cloud-aws/restarting-the-ieeg-org-aws-server.md) | shared | 2 | 3 | tighten | add: 'Who may do this / how to get access' line (electrophysiology stub names John Frommeyer) |
| [Git on the VDI & UPHS Computers](docs/compute/software-and-tools/git-on-the-vdi-and-uphs-computers.md) | shared | 2 | 2 | tighten | add: first line — 'Code only, never data or PHI, goes to GitHub' |
| [Linux Command Shortcuts](docs/compute/software-and-tools/linux-command-shortcuts.md) | retire | 3 | 1 | retire | retire: the page; move one paragraph to the BSC page — 'Files you create in /project/<group> must belong to that group: run newgrp <group… |
| [PennLINC BABS & ModelArray](docs/compute/software-and-tools/pennlinc-babs-and-modelarray.md) | reference | 1 | 1 | tighten | rewrite as five lines: what each tool does, when the lab would use it, where it has been run (BSC or Borel), canonical docs link; drop fa… |
| [Submitting CETS & PMACS Helpdesk Tickets](docs/compute/support-and-tickets/submitting-cets-and-pmacs-helpdesk-tickets.md) | core | 3 | 2 | rewrite | split: (a) an access-request matrix — what you need / who files / where / template / turnaround / how to verify; (b) one short page per r… |

## Imaging

28 pages (7 indexes, 21 procedures). Relevance: 9 core, 4 shared-infra, 11 cnt-clinical, 4 reference-only. Actions: 11 merge, 5 tighten, 5 reframe-as-reference, 4 rewrite, 2 retire, 1 needs-pi.

## Five biggest problems for a newcomer

1. **Live credentials.** "Pedro → cnt-fs (7T)" prints the pedro password twice and its abstract says "password given"; "Running the fMRI" prints three door codes and the laptop login, echoed in its abstract. Neither carries the "Credential removed" box. Fix first.
2. **The theme is written for a CNT scanner-day CRC.** Eleven of 21 procedures (scheduling, PennChart orders, consenting at the 3T/7T, the fMRI training script, billing review) are performed by nobody in NeuroBridge. Nothing tells an analyst that, or which four workflows are theirs: RADAR pulls, scan landing, DICOM→NIfTI, electrode reconstruction.
3. **Three contradictory 7T transfer stories:** hard drive (pointing at a retired page), CD burned by a tech, and Pedro. A newcomer cannot tell which is current, so the control-exclusion rule that depends on it is unexecutable.
4. **Reconstruction is spread over five overlapping pages** (~7,200 words, roughly 70% repeated) with two routes and no decision rule, named-person workarounds, a 2022 note, dead Google-hosted images, a punycode-broken link and a stray `scp` with a real pennkey and subject. No QC checklist anywhere.
5. **No verification steps and no owners.** Only "Opening ITK-SNAP files" says how to know it worked. Every page has empty `owner`/`last_reviewed`, names people by first name, and assumes PMACS, UPHS, Sectra, CAMRIS or Flywheel access.

## Merge or retire

Retire *Running the 7T* and *7T Badge Access* (fully duplicated). Merge the three 7T pages into one; the radiology email template into the 3T scheduling page; the three post-scan transfer pages into one "research scan → cnt-fs" page; and the five reconstruction pages into one canonical GUI/Docker procedure with appendices (Borel fallback, c3d check, MUSC variant, grids, reader-side ITK-SNAP). The theme shrinks from 21 procedures to about nine.

## Missing pages

A one-page "Imaging data in this lab" overview (modalities, protocols 819126/818407, where raw and BIDS imaging live, what is de-identified where); a BIDS/heudiconv conversion SOP, which the NIfTI de-identification page already assumes; a defacing policy, because non-defaced T1s currently travel to Borel/Leif and to a public-link Box folder; and a short "requesting access" page (PMACS, VPN client, Flywheel, Sectra, CAMRIS).

## First-read order

Rewritten Imaging index, then RADAR Data Pulls, the merged scan-landing page, DICOM → NIfTI, the canonical reconstruction page, Opening ITK-SNAP files. Scheduling and at-the-scanner pages come last, labelled "CNT clinical (reference)", for whoever covers a scan visit.

## Needs the PI

Current 7T transfer path; whether NeuroBridge runs reconstructions or consumes them; defacing on SEAS servers; which IRB covers RADAR pulls; the canonical cnt-fs mount and VPN client.


| Page | Rel. | Stale | New | Action | Note |
|---|---|---|---|---|---|
| [Visit Checklist: 3T Study](docs/imaging/scheduling-and-visits/visit-checklist-3t-study.md) | clinical coverage | 2 | 1 | reframe-as-reference | add: one-line header - protocol 819126, PI Kate Davis, who covers for CNT, whom to call |
| [Visit Checklist: 7T Study](docs/imaging/scheduling-and-visits/visit-checklist-7t-study.md) | clinical coverage | 2 | 1 | merge | duplicate of `7t-research-scans-logistics-and-safety.md`; merge: with 7T Research Scans: Logistics & Safety and 7T Badge Access into one … |
| [Email Template: Scheduling a Research 3T with Radiology](docs/imaging/scheduling-and-visits/email-template-scheduling-a-research-3t-with-radiology.md) | clinical coverage | 2 | 1 | merge | merge: into the 3T scheduling page as its final step |
| [3T Research Scans: Scheduling & Billing](docs/imaging/scheduling-and-visits/3t-research-scans-scheduling-and-billing.md) | clinical coverage | 2 | 2 | reframe-as-reference | cut: all struck-through text |
| [7T Research Scans: Logistics & Safety](docs/imaging/scheduling-and-visits/7t-research-scans-logistics-and-safety.md) | clinical coverage | 3 | 1 | merge | duplicate of `visit-checklist-7t-study.md`; merge: with Visit Checklist: 7T Study and 7T Badge Access into one 7T page |
| [Running the 7T](docs/imaging/at-the-scanner/running-the-7t.md) | clinical coverage | 2 | 0 | retire | duplicate of `visit-checklist-7t-study.md`; merge: the REDCap field list into the 7T checklist; the consent note is already on Consent No… |
| [7T Badge Access & MRI Safety Training](docs/imaging/at-the-scanner/7t-badge-access-and-mri-safety-training.md) | clinical coverage | 2 | 1 | retire | duplicate of `7t-research-scans-logistics-and-safety.md`; merge: into the single 7T page as a 'Before your first 7T visit' box |
| [Running the fMRI](docs/imaging/at-the-scanner/running-the-fmri.md) | clinical coverage | 3 | 2 | reframe-as-reference | cut: door codes (7676, 8097, 088880) and the laptop login from the body and the abstract; point to the lab password manager |
| [REDCap Documentation at the Scanner](docs/imaging/at-the-scanner/redcap-documentation-at-the-scanner.md) | clinical coverage | 2 | 2 | tighten | cut: struck-through CAPES line and the repeated 'fill out later' sentences |
| [PennChart Research Billing Review](docs/imaging/at-the-scanner/pennchart-research-billing-review.md) | clinical coverage | 2 | 0 | reframe-as-reference | add: two sentences on why (research charges must be cleared so participants are not billed) and how often |
| [Control Scan Neuroradiologist Check](docs/imaging/at-the-scanner/control-scan-neuroradiologist-check.md) | clinical coverage | 3 | 1 | needs-pi | rewrite: the 7T route once the current transfer path is confirmed; delete the retired-page reference |
| [Flywheel → cnt-fs (3T)](docs/imaging/post-scan-transfer/flywheel-cnt-fs-3t.md) | shared | 2 | 2 | rewrite | merge: with Pedro and CD pages into one 'Research scan -> cnt-fs' page; this page becomes the Flywheel source section |
| [Pedro → cnt-fs (7T)](docs/imaging/post-scan-transfer/pedro-cnt-fs-7t.md) | shared | 2 | 2 | merge | cut: the Pedro password from both occurrences and from the abstract; add the 'Credential removed' box and point to the password manager |
| [Uploading MRI CDs to cnt-fs](docs/imaging/post-scan-transfer/uploading-mri-cds-to-cnt-fs.md) | shared | 2 | 1 | merge | merge: into the single 'Research scan -> cnt-fs' page as 'Legacy CDs' with the RID###_2 naming rule |
| [DICOM → NIfTI (non-BIDS)](docs/imaging/formatting/dicom-nifti-non-bids.md) | core | 2 | 0 | rewrite | rewrite: as a short procedure - purpose, prerequisites, the one script to run, an example path edit, expected output, next step |
| [Electrode Reconstruction: Prep & Software](docs/imaging/electrode-reconstruction/electrode-reconstruction-prep-and-software.md) | core | 3 | 2 | merge | duplicate of `gui-docker-reconstruction-workflow.md`; merge: into the GUI/Docker page as the canonical procedure; keep from here only the… |
| [GUI/Docker Reconstruction Workflow](docs/imaging/electrode-reconstruction/gui-docker-reconstruction-workflow.md) | core | 2 | 2 | rewrite | rewrite: as the canonical reconstruction page - prerequisites (software, access), Part A export (CNT clinical), Part B convert and name, … |
| [MUSC Reconstruction](docs/imaging/electrode-reconstruction/musc-reconstruction.md) | core | 2 | 2 | merge | duplicate of `electrode-reconstruction-prep-and-software.md`; merge: into the canonical reconstruction page as a 'Site variant: MUSC' box… |
| [Opening ITK-SNAP Files from PennBox](docs/imaging/electrode-reconstruction/opening-itk-snap-files-from-pennbox.md) | reference | 2 | 2 | reframe-as-reference | reframe: title as 'For clinicians and reviewers: opening a reconstruction' and move the Box link to a prerequisites line |
| [Grid Electrode Labeling Conventions](docs/imaging/electrode-reconstruction/grid-electrode-labeling-conventions.md) | core | 1 | 1 | merge | merge: into the canonical reconstruction page as 'Appendix: grids and strips' |
| [RADAR Data Pulls](docs/imaging/clinical-imaging-pulls-radar/radar-data-pulls.md) | core | 3 | 2 | rewrite | rewrite: as NeuroBridge's canonical 'Requesting clinical imaging' SOP - prerequisites (IRB, PI request, RADAR fee), request, receive, lan… |

## Electrophysiology

## Five biggest newcomer problems

1. **A live password survived in two abstract boxes.** "Exporting Files from Natus" and its "(Pioneer)" copy carry the "Credential removed" warning, yet their machine-generated abstracts still print the Natus VNC password ("password xltek") — the credential that, misused, wipes every hospital's Natus data. It also gives a personal mobile number; three screenshots show real pennkeys.
2. **The core procedure is a 2,245-word command transcript pasted four times.** "Processing for ieeg.org" repeats five steps for four recording types with small unexplained differences, keeps struck-through commands and a "need to update with new scripts" flag, and contradicts itself about deleting `annotations.iann.json`. Nothing explains redaction or how to verify the upload.
3. **No framing anywhere.** The index asks how a recording gets acquired and never answers; the overview still speaks as "the staff of the CNT". No page states the PHI boundary (Natus and cnt-fs identified; ieeg.org date-shifted to 2000-01-01), who in NeuroBridge runs any of this, or how sEEG lands in Data Structure v1.0.
4. **Dead ends and dated breakage.** Archiving says "05/19/2026 — cnt1 crashed" and offers two routes with no verdict; Unarchiving and Restarting ieeg.org are stubs pointing at a retired knowledge-base page; "Lisa", "Josh A.", "Sarah Cormiea" appear by first name; the bedside task runs PsychoPy 1.83 via Box links.
5. **Duplication with drift.** Three channel-mapping pages, two scalp pipelines that disagree on `edit_studylist.py`'s arguments, Mxene content in three places, mount steps pasted into three pages. Names differ by case and version: `natusdir`/`natusDir`, `ieeg-latest`/`ieeg-cli-1.14.60`, `natus-latest`/`natus-converter-1.2.14`.

No page names a legacy KB tool.

## Merge or go

Retire the "(Pioneer)" export page, the legacy manual channel map, the duplicate scalp page and Restarting ieeg.org. Merge the second automated channel-mapping page into the first, the `.ini` page into a generalised "Anonymize & Upload EDFs", Mxene down to a one-screen specifics page, "Adding a file" into Troubleshooting, and "Final step" and "The config Folder" into Processing. Move "Mounting cnt-fs" to Compute and "Epilog ESI" to Imaging; rename the archiving section, which archives cnt-fs to Azure, not ieeg.org.

## Missing pages a newcomer would expect

A pipeline overview with roles and a diagram; a glossary (Natus, EMU, mef, CCEPS, HUP/RID); a consumer page on downloading HUP datasets from ieeg.org; text templates for natusdir and data-collection files; an unarchiving procedure; a per-patient status tracker; and how sEEG maps into Data Structure v1.0.

## First-read order

Index (framed) → sEEG overview (rewritten) → Mounting cnt-fs and ieeg.properties → Setup for Processing → natusdir & data collection → Automated Channel Mapping → Processing (one parameterised page) → Splitting and Troubleshooting → config folder → Archiving. Scalp EEG and special protocols afterwards; EMU Acquisition only for clinical cover.


| Page | Rel. | Stale | New | Action | Note |
|---|---|---|---|---|---|
| [sEEG Phase II Processing: Overview & Timeline](docs/electrophysiology/overview-and-setup/seeg-phase-ii-processing-overview-and-timeline.md) | core | 1 | 1 | rewrite | add: ordered nine-step chain with a link per step and the role that owns it |
| [Setup for Processing](docs/electrophysiology/overview-and-setup/setup-for-processing.md) | core | 2 | 1 | rewrite | add: two sentences on why two PDF versions exist (limited keeps the implant date for internal use; anonymized is shareable) and who may o… |
| [Mounting cnt-fs](docs/electrophysiology/overview-and-setup/mounting-cnt-fs.md) | core | 1 | 2 | tighten | add: one line on what cnt-fs is (PMACS HIPAA fileshare; identified data allowed) and who grants access |
| [natusdir & Data Collection Files](docs/electrophysiology/overview-and-setup/natusdir-and-data-collection-files.md) | core | 1 | 1 | rewrite | add: a plain-text template of each file with one example line and a comment per field |
| [The config Folder](docs/electrophysiology/overview-and-setup/the-config-folder.md) | core | 2 | 2 | tighten | fix: the cnt-fs path typo |
| [The ieeg.properties File](docs/electrophysiology/overview-and-setup/the-ieeg-properties-file.md) | core | 2 | 1 | rewrite | add: prerequisite - an ieeg.org account with upload rights, and who grants it |
| [Implant Coordinator Email & EMU Testing Slots](docs/electrophysiology/emu-acquisition/implant-coordinator-email-and-emu-testing-slots.md) | clinical coverage | 2 | 1 | reframe-as-reference | add: a three-line email template |
| [Bedside Testing: Gold Audio Task](docs/electrophysiology/emu-acquisition/bedside-testing-gold-audio-task.md) | clinical coverage | 3 | 1 | reframe-as-reference | add: one paragraph - whose study, what the task is, when it is run |
| [Exporting Files from Natus](docs/electrophysiology/exporting-from-natus/exporting-files-from-natus.md) | core | 3 | 1 | rewrite | reorder: procedure first, troubleshooting at the end |
| [Exporting EEG from Natus via VNC (Pioneer)](docs/electrophysiology/exporting-from-natus/exporting-eeg-from-natus-via-vnc-pioneer.md) | retire | 3 | 1 | retire | duplicate of `exporting-files-from-natus.md`; merge: the EDF-export and 'EEG database, not EMU' specifics into the Mxene page |
| [Clipping Gold Audio Task Files in Natus](docs/electrophysiology/exporting-from-natus/clipping-gold-audio-task-files-in-natus.md) | clinical coverage | 1 | 2 | reframe-as-reference | rename: 'Clipping a research segment in Natus', with Gold_Audio as the example name |
| [Automated Channel Mapping](docs/electrophysiology/channel-mapping/automated-channel-mapping.md) | core | 2 | 1 | rewrite | add: a six-line example output with header, three contacts and EKG1/2 |
| [Automated Channel Mappings for Natus EEG](docs/electrophysiology/channel-mapping/automated-channel-mappings-for-natus-eeg.md) | retire | 1 | 2 | merge | duplicate of `automated-channel-mapping.md`; merge: the two unique facts (script prompts for a filename; output lands in the programs dir… |
| [Manual Channel Mapping (legacy)](docs/electrophysiology/channel-mapping/manual-channel-mapping-legacy.md) | retire | 3 | 1 | retire | duplicate of `automated-channel-mapping.md`; carry: the 'electrode count matches the PowerPoint (n-1)' check and the 'revision requires a… |
| [Channel Mapping for EDFs (ieeg-dataset.ini)](docs/electrophysiology/channel-mapping/channel-mapping-for-edfs-ieeg-dataset-ini.md) | core | 1 | 2 | merge | duplicate of `anonymize-and-upload-edfs-to-ieeg-org.md`; merge: into Anonymize & Upload EDFs as the 'channel mapping (.ini)' step, genera… |
| [Processing for ieeg.org (natus2mef -> validate -> upload)](docs/electrophysiology/processing-and-upload-to-ieeg-org/processing-for-ieeg-org-natus2mef-validate-upload.md) | core | 2 | 1 | rewrite | rewrite: one parameterised procedure (TYPE in Intracranial, CCEPS, Gottfried, Gold) with a table of per-type differences: folder, natusdi… |
| [Troubleshooting Processing Errors](docs/electrophysiology/processing-and-upload-to-ieeg-org/troubleshooting-processing-errors.md) | core | 2 | 1 | tighten | restructure: a three-column table - symptom, likely cause, fix |
| [The cnt-pipeline AWS Instance](docs/electrophysiology/processing-and-upload-to-ieeg-org/the-cnt-pipeline-aws-instance.md) | shared | 2 | 2 | needs-pi | add: owner, account, cost and the start/stop rule |
| [Anonymize & Upload EDFs to ieeg.org](docs/electrophysiology/processing-and-upload-to-ieeg-org/anonymize-and-upload-edfs-to-ieeg-org.md) | core | 2 | 2 | rewrite | generalise: 'any EDF to ieeg.org' with Mxene as one example path |
| [Adding an iEEG File to a Project](docs/electrophysiology/processing-and-upload-to-ieeg-org/adding-an-ieeg-file-to-a-project.md) | core | 1 | 1 | merge | merge: into Troubleshooting as a 'dataset not in project' row with cause and fix |
| [Splitting Datasets](docs/electrophysiology/processing-and-upload-to-ieeg-org/splitting-datasets.md) | core | 1 | 1 | tighten | add: the three triggers (overlap, electrode change, sampling-rate change) in one list |
| [Final Step: Delete mef Folders](docs/electrophysiology/processing-and-upload-to-ieeg-org/final-step-delete-mef-folders.md) | core | 1 | 2 | merge | merge: into Processing as the closing step with a three-item precondition list (datasets open on ieeg.org; config folder in ieeg_metadata… |
| [Deleting a Dataset from ieeg.org](docs/electrophysiology/processing-and-upload-to-ieeg-org/deleting-a-dataset-from-ieeg-org.md) | core | 1 | 2 | tighten | add: when (PHI leak, wrong project, failed upload) and who approves |
| [Restarting ieeg.org](docs/electrophysiology/processing-and-upload-to-ieeg-org/restarting-ieeg-org.md) | retire | 3 | 0 | retire | retire: replace with one line in Troubleshooting - 'If ieeg.org is unreachable, report to <platform owner>' |
| [Archiving ieeg Files](docs/electrophysiology/archiving-on-ieeg-org/archiving-ieeg-files.md) | core | 3 | 1 | rewrite | rewrite: one current route; move the dated workaround to a note |
| [Unarchiving an ieeg Dataset](docs/electrophysiology/archiving-on-ieeg-org/unarchiving-an-ieeg-dataset.md) | core | 3 | 0 | needs-pi | needs content: the restore steps (az download, destination recently_unarchived/HUPXXX, who runs it, how long) |
| [Re-uploading Archived Datasets](docs/electrophysiology/archiving-on-ieeg-org/re-uploading-archived-datasets.md) | core | 2 | 1 | tighten | add: triggers and the order: delete bad dataset on ieeg.org -> restore -> rebuild folder -> reprocess |
| [EMU Interictal Scalp EEG Pipeline](docs/electrophysiology/scalp-eeg/emu-interictal-scalp-eeg-pipeline.md) | shared | 2 | 2 | tighten | add: purpose paragraph and ownership (Conrad group; who runs it; cadence per trimester) |
| [EMU Interictal Scalp EEG Pipeline (duplicate - merge)](docs/electrophysiology/scalp-eeg/emu-interictal-scalp-eeg-pipeline-duplicate-merge.md) | retire | 3 | 2 | retire | duplicate of `emu-interictal-scalp-eeg-pipeline.md`; retire: after confirming which Step 3 is current |
| [Mxene EEG Processing & Upload](docs/electrophysiology/special-protocols/mxene-eeg-processing-and-upload.md) | reference | 2 | 1 | merge | duplicate of `anonymize-and-upload-edfs-to-ieeg-org.md`; merge: keep a one-screen 'Mxene specifics' page (EEG database not EMU; two recor… |
| [CHOP Stim Seizures EEG Processing](docs/electrophysiology/special-protocols/chop-stim-seizures-eeg-processing.md) | reference | 2 | 1 | reframe-as-reference | reframe: one paragraph of context plus a 'differences from the standard pipeline' list (converter version, chop_fs paths, ieeg.org projec… |
| [Epilog ESI Protocol](docs/electrophysiology/special-protocols/epilog-esi-protocol.md) | clinical coverage | 2 | 1 | needs-pi | move: to Imaging (clinical imaging pulls) and link from here |

## REDCap & Clinical Metadata

Eleven pages (three indexes, eight content pages, 2,876 body words). The lab manual calls this "the clinical-variable layer that joins to every dataset"; as imported it is a CNT coordinator's data-entry notebook.

**Five biggest problems for a newcomer.** First, no catalogue of projects: four REDCap projects appear across the theme and wiki (the "surgical outcomes project", elsewhere the CNT or REDCap Surgical Repository; the Multimodal Clinical 3T Repository, pid 42518; Quantitative MRI for Epilepsy Surgical Planning; an unnamed "old" and "new" REDCap) with no PIDs, owners or statement of which NeuroBridge owns, while both indexes claim "projects the lab maintains". Second, the theme is entry-only: nothing explains how data leaves REDCap (exports, API tokens, de-identification, allowed locations) or how RID, MRN, HUP and subject IDs link a record to the BIDS datasets. Third, every procedure is a personal note: first names (Joel, Kate, Cat, Gabby, Mariam), "flag these for me", "I usually import in groups of 10", an "add screenshot once finalized" placeholder, a Q&A transcript and a bare DOI link. Fourth, three pages contradict themselves: the scale-invite text names instrument `prep_epileptologists` while its screenshot shows `prep_pre`; REDCap Tips says "unchecking" identifier-field removal in the abstract and "check off" in the body, for an action that grants PHI export rights; the Engel→ILAE text and table image word 4B differently. Fifth, policy residue: a patient name sits in the HTML title attribute of the withheld-screenshot placeholder on Seizure Terminology Reference; the RADAR page says clinical scans land on "borel, BSC" although Borel is not a PHI location; the working CSV with MRN and DOB has no storage rule.

**Merge or go.** Fold IC-CoDE into the RADAR page's neuropsych subsection; nest Messaging in PennChart under the Surgical Outcomes page (or move it to Operations) and drop its duplicate screenshot; turn Old → New Field Mapping into a changelog table with an analysis-caveat column; keep Triggering REDCap Scale Invites only as a CNT-coordinator reference once the instrument names are corrected, or drop it if nobody in NeuroBridge triggers invites.

**Missing pages.** A REDCap projects catalogue; "Getting data out of REDCap"; an identifier-mapping page (MRN ↔ RID ↔ HUP ↔ 3T/7T subject IDs); data-dictionary links for the Surgical Repository and the 3T repository; DAG and export-rights governance for the collaborating sites; a link to Requesting a REDCap Account, which already exists under Operations.

**First-read order.** Theme index rewritten around the project catalogue; Surgical Outcomes REDCap Project as the project overview; Seizure Terminology Reference as the coding conventions behind the outcome variables; RADAR Pull → REDCap Entry with its Imaging sibling; REDCap Tips as DAG and export administration. The two CNT-clinical pages and the migration changelog are consulted only when needed.


| Page | Rel. | Stale | New | Action | Note |
|---|---|---|---|---|---|
| [RADAR Pull → REDCap Entry](docs/redcap/clinical-data-pulls-ehr-redcap/radar-pull-redcap-entry.md) | core | 2 | 2 | rewrite | add: a three-line header — purpose (metadata for every clinical 3T/fMRI epilepsy patient), owner, cadence (yearly, triggered by the RADAR… |
| [IC-CoDE Neuropsych (RADAR)](docs/redcap/clinical-data-pulls-ehr-redcap/ic-code-neuropsych-radar.md) | retire | 1 | 0 | merge | cut: the page; move the DOI into RADAR Pull → REDCap Entry under 'Neuropsych variables' with one sentence on why it is cited |
| [Surgical Outcomes REDCap Project](docs/redcap/projects-and-data-entry/surgical-outcomes-redcap-project.md) | core | 1 | 1 | rewrite | rewrite as the project overview: name, PID, owner, DAGs, one line per instrument (what it holds, who fills it, when), and how RID links r… |
| [Messaging in PennChart](docs/redcap/projects-and-data-entry/messaging-in-pennchart.md) | clinical coverage | 2 | 2 | merge | cut: the generic eight-step 'how to send an In Basket message' (repeated by the Staff Msg steps) and one of the two identical screenshots |
| [REDCap Tips](docs/redcap/projects-and-data-entry/redcap-tips.md) | core | 1 | 1 | rewrite | rewrite the export tip: User Rights → the user's role → Data Export Rights; set the needed instruments to 'Full Data Set' (or 'De-Identif… |
| [Seizure Terminology Reference](docs/redcap/projects-and-data-entry/seizure-terminology-reference.md) | core | 1 | 2 | reframe-as-reference | merge the Engel→ILAE text list and the table image into one Markdown table with a Notes column; cite Engel (1993), ILAE/Wieser (2001) and… |
| [Triggering REDCap Scale Invites](docs/redcap/projects-and-data-entry/triggering-redcap-scale-invites.md) | clinical coverage | 3 | 1 | reframe-as-reference | cut: the broken nesting; rewrite as a seven-step numbered procedure with one screenshot per step |
| [Old → New REDCap Field Mapping](docs/redcap/projects-and-data-entry/old-new-redcap-field-mapping.md) | reference | 2 | 0 | reframe-as-reference | convert the Q&A into a table: modality / old value / new value / default rule / caveat / decided by / when |

## Operations

59 pages read in full. Relevance: 32 cnt-clinical, 12 shared-infra, 9 core, 2 reference-only, 4 retire. Action: 22 merge, 19 tighten, 6 rewrite, 6 retire, 4 reframe-as-reference, 2 keep.

**Five biggest problems for a newcomer.** First, the theme is written for a CNT clinical CRC: 32 of 59 pages cover consenting, scan trackers, ClinCard payments, CAMRIS and neuropsych testing, which nobody in NeuroBridge performs, while the two pages everyone needs, the onboarding and access checklists, assign every step to a first name (Josh, Gloria, Carolyn) and omit NeuroBridge's own systems (Slack, GitHub, Pennsieve, cnt1, Data Structure v1.0). Second, residue: the abstract of neuropsych-battery-materials.md still prints the flash-drive password (819126818407) above its "Credential removed" box; the contacts page carries personal mobile numbers for eight physicians; adding-a-non-penn-new-hire names the retired task tool, and its "personnel list" link (also on adding-personnel-to-an-irb-study) points to Mounting cnt-fs. Third, fragmentation: seven Greenphire pages are one BEN Helps form with different radio buttons, three CAMRIS pages share six identical steps, VPN/Citrix/Hayden Hall repeat one ticket flow, the 3T and 7T scripts differ by four parameters, and four PHI stubs say "ask the CRC lead" without naming system or lead. Fourth, no page states why, when, prerequisites or verification; nothing says IRB membership precedes cnt-fs or REDCap access, and front matter tags every access page for all five roles. Fifth, facts disagree: 7T compensation is $50 in the script and $90/$100 in Greenphire, MXene is 856681 on one page and 858681 on another, scripts promise a W-9/C-2 voucher while Greenphire pays by virtual card, and dated items (06/25/2026 roster, 7T end date 2/28/26) are already past.

**Merge or go.** Retire rppr-dates-targets, the three archive stubs, closing-an-irb-study and the scheduling-trackers index. Merge Greenphire seven into two, CAMRIS three into one, VPN + Citrix + Hayden Hall into one UPHS-ticket page, shared-drive + EMU mapping, 3T + 7T scripts, remote e-consent into e-consent, signed-ICF emails into contacting patients, Pavilion + PennChart into "Required trainings", the CRC access checklist into a rewritten onboarding matrix, and the contacts index into the Operations index.

**Missing pages a newcomer expects.** A role-based NeuroBridge onboarding matrix with an offboarding data handover; a protocol map (which IRB number grants which data); a required-trainings page (CITI, GCP, HIPAA, renewals); requesting cnt1/cnt-fs/BSC access (the Lab Manual flags it "not yet in the wiki"); a NeuroBridge directory and credentials policy.

**First-read order.** Operations index, the rewritten Onboarding & Offboarding Checklist, Adding Personnel to an IRB Study, Requesting a REDCap Account, UPHS VPN/Citrix (only if you need PennChart or the EMU drive), ieeg.org and Penn+Box access, the e-Regulatory Binder page (what documents you owe), then the emergency numbers. Clinical pages only when covering clinical duties.


| Page | Rel. | Stale | New | Action | Note |
|---|---|---|---|---|---|
| [CRC Access Checklist (systems, badges, trainings)](docs/operations/access-and-accounts/crc-access-checklist-systems-badges-trainings.md) | shared | 3 | 1 | merge | merge: into the onboarding matrix as a 'clinical coverage' column |
| [UPHS F5 VPN Access](docs/operations/access-and-accounts/uphs-f5-vpn-access.md) | shared | 2 | 2 | tighten | add: two sentences on UPHS VPN vs PMACS VPN vs SEAS access |
| [Citrix Remote Desktop Access](docs/operations/access-and-accounts/citrix-remote-desktop-access.md) | shared | 2 | 2 | merge | merge: with uphs-f5-vpn-access.md and remote-access-to-the-hayden-hall-uphs-computer.md into one 'UPHS IS tickets: VPN, Citrix app, share… |
| [Remote Access to the Hayden Hall UPHS Computer](docs/operations/access-and-accounts/remote-access-to-the-hayden-hall-uphs-computer.md) | shared | 3 | 1 | tighten | cut: the user roster |
| [Requesting Shared Drive Access (Penn Medicine ticket)](docs/operations/access-and-accounts/requesting-shared-drive-access-penn-medicine-ticket.md) | shared | 2 | 2 | merge | merge: with mapping-the-emu-shared-drive.md into one page 'EMU reports drive: request and map' |
| [Mapping the EMU Shared Drive](docs/operations/access-and-accounts/mapping-the-emu-shared-drive.md) | shared | 1 | 2 | merge | merge: into the shared-drive request page as step 2 |
| [PennKey & REDCap Access for External Guests](docs/operations/access-and-accounts/pennkey-and-redcap-access-for-external-guests.md) | core | 2 | 0 | rewrite | rewrite: transcribe the PDF into numbered steps with sponsor, form links and turnaround |
| [Requesting a REDCap Account](docs/operations/access-and-accounts/requesting-a-redcap-account.md) | core | 2 | 2 | tighten | fix: numbering and the triple-rendered link |
| [Adding Staff to the Penn+Box CNT Administration Folder](docs/operations/access-and-accounts/adding-staff-to-the-penn-box-cnt-administration-folder.md) | shared | 1 | 1 | merge | merge: with data/storage-locations/pennbox.md into one Penn+Box page covering access, folder map and what may live there |
| [Adding Users to the ieeg.org Portal](docs/operations/access-and-accounts/adding-users-to-the-ieeg-org-portal.md) | core | 1 | 2 | tighten | add: one line: ieeg.org is the de-identified iEEG portal; never PHI |
| [Path BioResource Manager Access](docs/operations/access-and-accounts/path-bioresource-manager-access.md) | clinical coverage | 2 | 1 | merge | merge: with adding-camris-users.md and updating-camris-user-access.md into one 'CAMRIS user access' page |
| [Adding CAMRIS Users](docs/operations/access-and-accounts/adding-camris-users.md) | clinical coverage | 2 | 2 | merge | merge: three CAMRIS pages into one with add / change / manager-access subsections |
| [Updating CAMRIS User Access](docs/operations/access-and-accounts/updating-camris-user-access.md) | clinical coverage | 2 | 2 | merge | duplicate of `adding-camris-users.md`; merge: into adding-camris-users.md as the 'change study access' subsection |
| [Onboarding & Offboarding Checklist](docs/operations/onboarding-and-offboarding/onboarding-and-offboarding-checklist.md) | core | 2 | 1 | rewrite | rewrite: as a role x system matrix (data RC / analyst / student / PI) with Owner-by-role, How-to-request, Verify, Offboard columns |
| [CNT Data & Computing Orientation](docs/operations/onboarding-and-offboarding/cnt-data-and-computing-orientation.md) | reference | 2 | 1 | reframe-as-reference | cut: the 2022 deck; archive the 2023 PDF under 'history' |
| [One HUP Pavilion Training](docs/operations/onboarding-and-offboarding/one-hup-pavilion-training.md) | clinical coverage | 2 | 1 | merge | merge: into one 'Required trainings' page (CITI, HIPAA, GCP, PennChart, Pavilion, 7T MRI safety) with who / when / renewal / where recorded |
| [PennChart Training](docs/operations/onboarding-and-offboarding/pennchart-training.md) | shared | 2 | 1 | merge | merge: into 'Required trainings' with the course list from the CRC checklist |
| [Adding Personnel to an IRB Study](docs/operations/regulatory-irb-and-reporting/adding-personnel-to-an-irb-study.md) | core | 2 | 2 | tighten | fix: the two personnel-list links; delete 'You do not have access to this Doc' |
| [Adding a Non-Penn / New Hire to a Study](docs/operations/regulatory-irb-and-reporting/adding-a-non-penn-new-hire-to-a-study.md) | core | 2 | 2 | rewrite | rewrite: remove the legacy tool name; point step 5 at the real personnel list |
| [Closing an IRB Study](docs/operations/regulatory-irb-and-reporting/closing-an-irb-study.md) | reference | 1 | 0 | retire | retire: move the link into the regulatory index; write local closure steps only when NeuroBridge closes a study |
| [eDOA REDCap Entry](docs/operations/regulatory-irb-and-reporting/edoa-redcap-entry.md) | clinical coverage | 2 | 1 | reframe-as-reference | fix: renumber responsibilities so the key matches |
| [e-Regulatory Binder & eDoA (Audit Prep)](docs/operations/regulatory-irb-and-reporting/e-regulatory-binder-and-edoa-audit-prep.md) | shared | 3 | 2 | tighten | cut: the duplicated document list; keep one table with expiry periods |
| [RPPR Demographic Tables](docs/operations/regulatory-irb-and-reporting/rppr-demographic-tables.md) | clinical coverage | 2 | 2 | reframe-as-reference | reframe: 'How to produce an NIH inclusion-enrollment table from a REDCap report', with the Davis reports as an example |
| [RPPR: Dates, Targets & Milestones](docs/operations/regulatory-irb-and-reporting/rppr-dates-targets-and-milestones.md) | retire | 3 | 0 | retire | retire: hand to the Davis lab; if kept, one sentence under the RPPR tables page |
| [Consent Signing Checklist](docs/operations/consenting/consent-signing-checklist.md) | clinical coverage | 1 | 2 | keep | add: the storage location and naming convention it alludes to |
| [3T Consent Script](docs/operations/consenting/3t-consent-script.md) | clinical coverage | 2 | 2 | merge | merge: with 7t-consent-script.md into one script with a 3T/7T parameter table (title, duration, payment, location) |
| [7T Consent Script](docs/operations/consenting/7t-consent-script.md) | clinical coverage | 2 | 2 | merge | duplicate of `3t-consent-script.md`; merge: into the single consent script page |
| [All Consent Forms (Box links)](docs/operations/consenting/all-consent-forms-box-links.md) | clinical coverage | 3 | 1 | reframe-as-reference | reframe: as a table protocol # -> form -> Box link -> version/date -> owner |
| [Consent Note Templates](docs/operations/consenting/consent-note-templates.md) | clinical coverage | 2 | 2 | tighten | fix: the 7T sentence |
| [How the e-Consent Form Works](docs/operations/consenting/how-the-e-consent-form-works.md) | clinical coverage | 2 | 2 | tighten | merge: remote-e-consent-procedure.md in as a 'remote variant' section |
| [Remote e-Consent Procedure](docs/operations/consenting/remote-e-consent-procedure.md) | clinical coverage | 2 | 2 | merge | merge: into how-the-e-consent-form-works.md |
| [Scan Scheduling Trackers (sEEG, 3T/fMRI, 7T)](docs/operations/scheduling-trackers/scan-scheduling-trackers-seeg-3t-fmri-7t.md) | clinical coverage | 2 | 0 | rewrite | rewrite: one page 'Clinical trackers: where they live and who grants access' with a table of the live tracker and three archives |
| [Archive: fMRI/3T Scans](docs/operations/scheduling-trackers/archive-fmri-3t-scans.md) | retire | 2 | 0 | retire | retire: fold the one-line description into the trackers page |
| [Archive: 7T Scans](docs/operations/scheduling-trackers/archive-7t-scans.md) | retire | 2 | 0 | retire | duplicate of `archive-fmri-3t-scans.md`; retire: fold into the trackers page |
| [Archive: sEEG Implants](docs/operations/scheduling-trackers/archive-seeg-implants.md) | retire | 2 | 0 | retire | duplicate of `archive-fmri-3t-scans.md`; retire: fold into the trackers page |
| [Greenphire ClinCard: Overview](docs/operations/participant-reimbursement-greenphire/greenphire-clincard-overview.md) | clinical coverage | 2 | 1 | merge | merge: seven pages into 'Greenphire: tickets (account, study access, new study, budget)' and 'Greenphire: paying a participant' |
| [Creating a Greenphire Account](docs/operations/participant-reimbursement-greenphire/creating-a-greenphire-account.md) | clinical coverage | 2 | 2 | merge | merge: into the Greenphire tickets page as one row of a ticket-type x field-value table |
| [Giving a User Study Access](docs/operations/participant-reimbursement-greenphire/giving-a-user-study-access.md) | clinical coverage | 1 | 2 | merge | duplicate of `creating-a-greenphire-account.md`; merge: one row in the ticket table |
| [Creating a New Study](docs/operations/participant-reimbursement-greenphire/creating-a-new-study.md) | clinical coverage | 1 | 2 | merge | merge: one row in the ticket table |
| [Increasing a Study Budget](docs/operations/participant-reimbursement-greenphire/increasing-a-study-budget.md) | clinical coverage | 2 | 2 | merge | duplicate of `creating-a-new-study.md`; merge: one row in the ticket table; keep the example screenshot only if it shows no staff data |
| [Ordering Physical Cards](docs/operations/participant-reimbursement-greenphire/ordering-physical-cards.md) | clinical coverage | 3 | 1 | merge | merge: the two useful facts (virtual-only; support links) into the Greenphire overview; delete the rest |
| [Reimbursing a Participant](docs/operations/participant-reimbursement-greenphire/reimbursing-a-participant.md) | clinical coverage | 2 | 2 | tighten | fix: finish or delete the truncated 'Adding a New Study' and empty 'parking' sections |
| [Postop Neuropsych Testing: Overview](docs/operations/postop-neuropsych-testing/postop-neuropsych-testing-overview.md) | clinical coverage | 2 | 1 | tighten | add: the three file paths |
| [Contacting & Scheduling Patients](docs/operations/postop-neuropsych-testing/contacting-and-scheduling-patients.md) | clinical coverage | 2 | 2 | tighten | merge: sending-the-signed-icf-and-attestation.md in as the follow-up step |
| [Sending the Signed ICF & Attestation](docs/operations/postop-neuropsych-testing/sending-the-signed-icf-and-attestation.md) | clinical coverage | 1 | 2 | merge | merge: into contacting-and-scheduling-patients.md |
| [Testing Battery](docs/operations/postop-neuropsych-testing/testing-battery.md) | clinical coverage | 2 | 2 | keep | fix: legend formatting |
| [Running the Test](docs/operations/postop-neuropsych-testing/running-the-test.md) | clinical coverage | 2 | 2 | tighten | fix: the three broken or misdirected links |
| [Scoring](docs/operations/postop-neuropsych-testing/scoring.md) | clinical coverage | 2 | 1 | tighten | add: the folder path once at the top |
| [Neuropsych Battery: Materials](docs/operations/postop-neuropsych-testing/neuropsych-battery-materials.md) | clinical coverage | 2 | 0 | rewrite | rewrite: strip the password from the abstract immediately; then reduce to a one-line pointer to the Box folder and the password manager, … |
| [Important Contacts & Emergency Numbers](docs/operations/contacts/important-contacts-and-emergency-numbers.md) | shared | 3 | 2 | rewrite | rewrite: split into (1) Emergency and safety (rapid response, interpreter, help desks) and (2) a role-based directory that includes Neuro… |

## Questions only the lab can answer

Collected from every page. Answering them is what turns the inherited text into NeuroBridge's own; the ones that recur across themes (which systems may hold identified data, who files account requests and under which sponsor and IRB, which named people now hold which roles, which REDCap projects and cloud accounts are the lab's) unblock the most pages.


### Data

- Is Data Structure v1.0 written down anywhere the index can link to?. *(Data)*
- Should site-delivered retrospective data (15+ sites) get its own section under Data?. *(Data)*
- Is Leif still in use, and for what?. *(Moving Data)*
- Does NeuroBridge archive to the Litt lab's cntlitt account or to its own storage account?. *(Archiving (Azure))*
- Who approves deleting raw data from cnt-fs after archiving?. *(Archiving (Azure))*
- Which platform is the lab's default for sharing: Pennsieve, ieeg.org, or both, and for which data types?. *(Sharing (Pennsieve & ieeg.org))*
- What is the lab's current de-identification standard (header fields, annotations, date shift, defacing)?. *(De-identification)*
- Who verifies de-identification before data leaves PMACS systems?. *(De-identification)*
- Is 'limited' data (RID numbers + dates of service) still permitted on Borel/Pioneer, or must everything on SEAS be fully anonymized?. *(Data Storage Locations)*
- Has the Borel sandbox move to BSC happened?. *(Data Storage Locations)*
- Is Pioneer still in service, and where do Leif and Finkel fit?. *(Data Storage Locations)*
- Which project directories (BSC, cnt-fs shares) belong to NeuroBridge and should a newcomer be added to?. *(Data Storage Locations)*
- Is 'pedro' still the 7T staging server, and who runs it?. *(Where 3T and 7T Scans Are Stored)*
- Does NeuroBridge run its own prospective 3T/7T scans, or only consume CNT's?. *(Where 3T and 7T Scans Are Stored)*
- Is sharing Penn+Box folders with personal box.com accounts permitted at all, and never for PHI?. *(PennBox)*
- What are the lab's Penn+Box folders and who owns them?. *(PennBox)*
- Do collaborating sites deliver retrospective data via Penn+Box, SFTP, or something else?. *(PennBox)*
- What is NeuroBridge's project directory on BSC (examples use davis_group_1)?. *(Moving Data Across cnt-fs, cnt1, BSC, Borel & Leif)*
- Does the lab use Leif, and what is its hostname and role?. *(Moving Data Across cnt-fs, cnt1, BSC, Borel & Leif)*
- May analysts rsync directly from cnt1 to Borel, or only from a de-identified staging area?. *(Moving Data Across cnt-fs, cnt1, BSC, Borel & Leif)*
- Is rclone still the sanctioned Box <-> cnt-fs path, or has PMACS provided an alternative (Box Drive on VDI, Globus)?. *(Transferring Files from Box to cnt-fs (rclone))*
- Where should site deliveries land on cnt-fs under Data Structure v1.0 (per-site _fs shares?). *(Transferring Files from Box to cnt-fs (rclone))*
- Does NeuroBridge archive to the Litt lab's cntlitt account or should it have its own storage account/container?. *(Archiving EEG Data to Azure)*
- Who at PMACS issues the SAS token, and has the 03/15/2026 token been renewed?. *(Archiving EEG Data to Azure)*
- Is there an inventory of what has been archived (HUPXXX list), and where is it kept?. *(Archiving EEG Data to Azure)*
- Who approves an unarchive request (it costs money), and is there a log of unarchive events?. *(cnt1 Scripts for Azure Archiving & Unarchiving)*
- Which IRB protocols cover NeuroBridge's data sharing, and who approves each Pennsieve release?. *(Pennsieve Data Access Rules)*
- Where is the RID/HUP <-> identity key kept, and who may hold it?. *(Pennsieve Data Access Rules)*
- How does this tree apply to retrospective data delivered by the 15+ sites under DUAs (consent waived)?. *(Pennsieve Data Access Rules)*
- Is 'controlled access' on Pennsieve actually in use, and what is the data request form?. *(Pennsieve Data Access Rules)*
- Which Pennsieve organization/workspace and datasets does NeuroBridge own (vs CNT/Litt)?. *(Uploading to Pennsieve Locally)*
- Has the Pennsieve API key printed on this page been rotated?. *(Uploading from cnt1 to Pennsieve)*
- Is 'module load pennsieve' still available on cnt1, and is bscsub -> cnt1 still the route?. *(Uploading from cnt1 to Pennsieve)*
- Where does pennsieve_downloader.py live (repo), and who maintains it?. *(Pennsieve Downloader)*
- Does the current Pennsieve agent's download command make this script unnecessary?. *(Pennsieve Downloader)*
- Does NeuroBridge upload to ieeg.org at all, and under whose uploader account/bucket?. *(AWS Bucket Numbers (ieeg.org / PREVeNT))*
- Is NeuroBridge involved in PREVeNT or TACERN, or is this roster purely CNT's?. *(AWS Bucket Numbers (ieeg.org / PREVeNT))*
- Which script is the lab standard: edf_deid_wrapper.sh (strips annotations) or anonymize_edfs.sh (headers + date shift, keeps annotations)?. *(De-Identifying EDFs)*
- Are annotations ever PHI in our EDFs (e.g., names typed by techs), and is stripping them the policy?. *(De-Identifying EDFs)*
- Is the lab still processing Mxene study EEG, or is that purely CNT?. *(De-Identifying EDF Headers)*
- Which anonymize script/version is current, and is it in a repo?. *(De-Identifying EDF Headers)*
- What exactly does deid_json.sh strip, and where does the script live now (heudiconv_3T vs deid_json)?. *(De-identifying NIfTI Headers)*
- Is defacing required before imaging leaves PMACS, or is header de-identification sufficient under the lab's protocols?. *(De-identifying NIfTI Headers)*

### Compute

- Which systems do NeuroBridge members actually hold accounts on today (Borel/Leif/Finkel, cnt1/cnt-fs, BSC, cntgpu1), and who in the lab requests them?. *(Compute)*
- Is 'share by HUP number, never RID' and the 2000-01-01 date shift still the lab's convention under Data Structure v1.0, and does it apply to non-Penn sites' data?. *(Overview of CNT Systems)*
- Who now grants cnt-fs user-group membership and upenn-ieeg / upenn-surgrec AWS access for NeuroBridge members?. *(Overview of CNT Systems)*
- Has the raw-Natus move to Azure completed (the Data › Archiving pages suggest yes)?. *(Overview of CNT Systems)*
- Does NeuroBridge use Persyst at all?. *(Overview of CNT Systems)*
- Is BSC a permitted location for identified data? This page and PMACS Overview say no; the lab-manual glossary says yes as of 2026-09-20. *(CNT Computing Schematic)*
- Which VPNs does a NeuroBridge member need by default: PMACS Ivanti, Penn GlobalProtect, UPHS F5 — all three?. *(CNT Computing Schematic)*
- What are NODDI and Surgrec in this table and are they still live?. *(CNT Computing Schematic)*
- Which cnt1 /projects directories does NeuroBridge use, and is the listing current?. *(VDI, cnt-fs and cnt1)*
- Does the lab have its own directory and user group on cnt1/cnt-fs, or does it work inside the Davis/Litt groups?. *(VDI, cnt-fs and cnt1)*
- Does anyone in NeuroBridge use the Hayden Hall UPHS desktops, or should this stay with CNT and leave the lab wiki?. *(Hayden Hall UPHS Computers)*
- Do NeuroBridge members get Borel/Leif/Finkel access through the CNT 'littuser/davisuser' groups, or does the lab have its own CETS group?. *(SEAS Servers: Borel, Leif, Pioneer)*
- Who is the lab's CETS sponsor for SEAS sponsored research accounts?. *(SEAS Servers: Borel, Leif, Pioneer)*
- Is the Fall 2023 CETS security deck still required reading?. *(SEAS Servers: Borel, Leif, Pioneer)*
- Which directory should NeuroBridge members use for project data on Borel (/projects/<lab>? /data/Human_Data?), and is there a lab group directory?. *(Accessing Borel over SSH)*
- Is Finkel still 2 x L40S with 8 shards, and is the 128 GB per-user memory limit on Borel/Pioneer in force?. *(Submitting Jobs with SLURM)*
- Does the lab standardise on conda or modules on Borel, and is there a shared environment path?. *(Submitting Jobs with SLURM)*
- Who in NeuroBridge raises SLURM configuration requests with CETS now?. *(SLURM on Finkel: Configuration & Limits)*
- Are these limits current, and as of when?. *(SLURM on Finkel: Configuration & Limits)*
- Is PHI allowed on BSC? The glossary says yes (2026-09-20); this page says no. *(PMACS Overview)*
- Does NeuroBridge use PMACS HPC at all, or only LPC/BSC?. *(PMACS Overview)*
- Who pays for NeuroBridge's LPC/HPC usage, and is there a lab allocation or project code?. *(PMACS Overview)*
- Which BSC /project directory and group does NeuroBridge use (davis_group_1? its own?), and who requests membership?. *(BSC Cluster)*
- May identified imaging data be processed on BSC (glossary says yes since 2026-09-20; CNT pages say no)?. *(BSC Cluster)*
- Are the 2022 queue limits still current?. *(BSC Cluster)*
- Does NeuroBridge have or need access to the cntgpu queue, and what hardware is behind cntgpu1?. *(cntgpu1 GPU Queue)*
- Which VPNs do NeuroBridge members need by default, and does DBEI/IBI issue PMACS accounts differently from CNT (Neurology-sponsored)?. *(PMACS VPN)*
- Does NeuroBridge have its own AWS @ Penn account for the cloud-infrastructure project, and who is the account owner?. *(Cloud (AWS))*
- Does NeuroBridge hold an AWS @ Penn account; if so, its name, owner, bucket, and whether a BAA covers any PHI?. *(AWS @ Penn: Getting Started)*
- Should the wiki host ISC's guide at all, or link to the source?. *(AWS @ Penn: Getting Started)*
- Is anyone in NeuroBridge expected to hold upenn-ieeg credentials as a backup for ieeg.org restarts?. *(Restarting the ieeg.org AWS Server)*
- What is the lab's standard analysis stack and GitHub organisation, and is there an environment file newcomers should install?. *(Software & Tools)*
- Is PortableGit on cnt-fs staff_admin reachable by non-staff NeuroBridge members, or should they be pointed to git on cnt1?. *(Git on the VDI & UPHS Computers)*
- Has anyone in the lab run BABS or ModelArray, and on which cluster? If not, should this page exist yet?. *(PennLINC BABS & ModelArray)*
- Which viewers and toolkits should newcomers install (EEG viewer, NIfTI viewer, dcm2niix, ITK-SNAP)?. *(Software Tools Index)*
- Who is NeuroBridge's designated systems contact who files access tickets, now that the 'Data & Systems Manager' in these pages is a CNT post?. *(Support & Tickets)*
- For NeuroBridge hires, who is the PMACS sponsor and department (Nishant Sinha / DBEI?) and which IRB protocols must they join before cnt1/cnt-fs access?. *(Submitting CETS & PMACS Helpdesk Tickets)*
- Who files PMACS 'Systems' tickets and CETS requests for the lab, and does that person hold 'Systems' permission in the PMACS portal?. *(Submitting CETS & PMACS Helpdesk Tickets)*
- Which SEAS usergroup should NeuroBridge members join (littuser/davisuser or a new one), and who is the SEAS sponsor?. *(Submitting CETS & PMACS Helpdesk Tickets)*
- Is the VDI still the required route to cnt1, or do PMACS-managed laptops or direct ssh over the PMACS VPN now suffice?. *(Submitting CETS & PMACS Helpdesk Tickets)*

### Imaging

- Which imaging workflows does NeuroBridge perform itself today: RADAR pulls, electrode reconstructions, DICOM-to-NIfTI, any scanner-day duties?. *(Imaging)*
- Does any NeuroBridge member hold scheduling duties under 819126 or 818407?. *(Scheduling & Visits)*
- Who in the shared CNT/NeuroBridge team now owns moving research scans into cnt-fs?. *(Post-scan Transfer)*
- Is there a BIDS (heudiconv) conversion SOP to publish next to the non-BIDS page? The NIfTI de-identification page already assumes an imaging_bids tree. *(Formatting)*
- Does NeuroBridge run reconstructions itself (for retrospective multi-site cohorts) or consume the CNT outputs?. *(Electrode Reconstruction)*
- Does anyone in NeuroBridge cover 3T scan visits under 819126, or should this live only under a 'CNT clinical (reference)' label?. *(Visit Checklist: 3T Study)*
- Is protocol version V5 (dated 7.21.25 on the fMRI page) still current?. *(Visit Checklist: 3T Study)*
- Is the CD step (tech burns CD, dropped to the PEC coordinator) still how 7T clinical copies reach PACS, or has Pedro replaced it?. *(Visit Checklist: 7T Study)*
- Who maintains the 7T physician-attendance roster now?. *(Visit Checklist: 7T Study)*
- Is all prospective imaging the lab touches under Davis 819126/818407, or does NeuroBridge hold any protocol of its own on which a research scan could be ordered?. *(3T Research Scans: Scheduling & Billing)*
- Is the 7T protocol (818407) still enrolling, and does any NeuroBridge staff member ever attend?. *(7T Research Scans: Logistics & Safety)*
- Will any NeuroBridge member ever run the clinical fMRI, or should this page move entirely under a CNT clinical reference label?. *(Running the fMRI)*
- Who owns the fMRI laptop and push-box now, and where are the current door codes kept?. *(Running the fMRI)*
- Is the REDCap Surgical Repository the same project the data RC pulls from, and does the data RC rely on the 'where was the scan saved' field?. *(REDCap Documentation at the Scanner)*
- Are 3T/7T subject numbers (e.g. 7T_C034) still assigned manually from the RPPR report?. *(REDCap Documentation at the Scanner)*
- Does any NeuroBridge protocol generate PennChart research charges that need review?. *(PennChart Research Billing Review)*
- How do 7T control scans now reach PACS for the neuroradiologist - hard drive, CD, or Pedro?. *(Control Scan Neuroradiologist Check)*
- Where is a failed control check recorded so the data RC can exclude the subject from curated datasets?. *(Control Scan Neuroradiologist Check)*
- Which VPN client is current for PMACS (BIG-IP Edge/F5 or Ivanti)?. *(Flywheel → cnt-fs (3T))*
- Does the data RC or the CNT CRC own moving 3T scans into cnt-fs now?. *(Flywheel → cnt-fs (3T))*
- How long does pedro keep 7T exports before purging?. *(Pedro → cnt-fs (7T))*
- Who is accountable for the 7T copy now that CNT coordinators are shared across groups?. *(Pedro → cnt-fs (7T))*
- Is the CD backlog finished? If not, who owns the remaining discs and where are the 'issue' CDs?. *(Uploading MRI CDs to cnt-fs)*
- Which cnt-fs mount path is canonical: smb://pmacs.upenn.edu/depts/NE-4322-Neurology/CNT or smb://172.16.50.149/CNT?. *(Uploading MRI CDs to cnt-fs)*
- Is /project/imaging_process/programs/run_dcm2niix still the lab's conversion path, or has heudiconv/BIDS replaced it?. *(DICOM → NIfTI (non-BIDS))*
- Which script and text file are canonical, and where does output land relative to imaging_bids?. *(DICOM → NIfTI (non-BIDS))*
- Are the T1 images in /mnt/leif/littlab/data/Human_Data/recon/BIDS_penn defaced before they reach Borel, given SEAS servers are never PHI locations?. *(Electrode Reconstruction: Prep & Software)*
- Is the Borel run_penn_recons.py route still supported, or is Docker/GUI the only sanctioned route?. *(Electrode Reconstruction: Prep & Software)*
- Does NeuroBridge staff hold UPHS/Sectra access to export clinical images, or does CNT do that step?. *(Electrode Reconstruction: Prep & Software)*
- Which ieeg-recon release (penn-cnt/ieeg-recon) is the lab standard, and who maintains it?. *(GUI/Docker Reconstruction Workflow)*
- Should reconstruction outputs for lab use be written to cnt-fs/BSC derivatives rather than to the clinical PennBox folder?. *(GUI/Docker Reconstruction Workflow)*
- Is the MUSC R01 collaboration active, and does the site-onboarding protocol make this the template for other sites' reconstructions?. *(MUSC Reconstruction)*
- Does the MUSC DUA permit their imaging on Borel/Leif and in a Penn Box folder?. *(MUSC Reconstruction)*
- Should reconstructions shared with clinicians be defaced, or is the Box folder treated as a clinical (PHI-permitted) location?. *(Opening ITK-SNAP Files from PennBox)*
- Does the lab still reconstruct grid/strip cases (retrospective or site data), or is this historical?. *(Grid Electrode Labeling Conventions)*
- Which IRB protocol(s) cover NeuroBridge's RADAR requests, and who is the lab's current RADAR contact?. *(RADAR Data Pulls)*
- Is MJ0HKNDA (or any UPHS workstation) still available to NeuroBridge staff for the fileshare step?. *(RADAR Data Pulls)*
- Where should RADAR DICOMs be archived now - Sauce/Borel or the Azure cold archive - and where do NIfTIs land under Data Structure v1.0?. *(RADAR Data Pulls)*

### Electrophysiology

- Does NeuroBridge's data RC run the sEEG -> ieeg.org pipeline today, or does CNT data staff run it and NeuroBridge consume the output?. *(Electrophysiology)*
- Is ieeg.org still the publication target for new patients, or is the BIDS Data Structure v1.0 / Pennsieve path replacing it?. *(Electrophysiology)*
- Who in NeuroBridge owns sEEG processing now, and does the one-week post-explant deadline still apply?. *(sEEG Phase II Processing: Overview & Timeline)*
- Does the lab still process the CCEPS, Gottfried and Gold research recordings, or only the clinical intracranial recording?. *(sEEG Phase II Processing: Overview & Timeline)*
- Who is 'Lisa' (role) and is she still the implant-map contact?. *(Setup for Processing)*
- Does the data RC receive the implant PowerPoint directly, and may it be handled on a personal laptop?. *(Setup for Processing)*
- Are both limited and anonymized versions still required, and who is allowed to see the limited one?. *(Setup for Processing)*
- Is the UNC path \\pmacs.upenn.edu\depts\NE-4322-Neurology\CNT still current, and should the raw IP be published at all?. *(Mounting cnt-fs)*
- Is natus2mef's natusdir format documented in the converter repo, so the template can be copied from source?. *(natusdir & Data Collection Files)*
- Who receives the 'ready to archive' hand-off now that it is no longer Josh A.?. *(The config Folder)*
- Who issues ieeg.org accounts and upload or admin rights for NeuroBridge members?. *(The ieeg.properties File)*
- Does any NeuroBridge member do EMU bedside testing or coordinate implants?. *(EMU Acquisition)*
- Is the Friday/Monday/Tuesday testing schedule still in force and who maintains it?. *(Implant Coordinator Email & EMU Testing Slots)*
- Should the NeuroBridge data RC be on the ecogresearch listserv?. *(Implant Coordinator Email & EMU Testing Slots)*
- Is the Gold lab audio task still being collected at HUP, and by whom?. *(Bedside Testing: Gold Audio Task)*
- If not, should this page and the Gold clipping and channel-map sections be retired together?. *(Bedside Testing: Gold Audio Task)*
- Does any NeuroBridge member hold Natus/VNC access, or is export always done by CNT staff?. *(Exporting from Natus)*
- Who holds Natus/VNC access for NeuroBridge today, and what is the current support route when the Natus PC locks?. *(Exporting Files from Natus)*
- Has the shared VNC password been rotated now that it sat in a wiki page and still sits in an abstract?. *(Exporting Files from Natus)*
- What does '(Pioneer)' refer to here - the SEAS server, a project name, or a person?. *(Exporting EEG from Natus via VNC (Pioneer))*
- Which research tasks still need clipping (Gold, Gottfried, CCEPS) and who clips them?. *(Clipping Gold Audio Task Files in Natus)*
- Is the 256/262 vs 128/134 DC channel ambiguity a headbox difference that can be stated as a rule?. *(Automated Channel Mapping)*
- Are the Gottfried and Gold research tasks still running; if not, drop those sections?. *(Automated Channel Mapping)*
- Is buildcm still needed for any case the automated script cannot handle, such as no exported recording yet?. *(Manual Channel Mapping (legacy))*
- Are CCEPS, Gottfried and Gold uploads still active, and who should be notified now?. *(Processing for ieeg.org (natus2mef -> validate -> upload))*
- Is the 'module load python/3.10' libpython error still current on cnt1?. *(Processing for ieeg.org (natus2mef -> validate -> upload))*
- Who administers the HUP_Intracranial_Data project on ieeg.org and grants NeuroBridge upload rights?. *(Processing for ieeg.org (natus2mef -> validate -> upload))*
- Is there a command-line way on cnt1 to read a Natus recording's sampling rate?. *(Troubleshooting Processing Errors)*
- Is the CNT AWS processing instance still in service, who owns the account, and may NeuroBridge staff start it?. *(The cnt-pipeline AWS Instance)*
- Should NeuroBridge uploads use '-q CNT' at all?. *(The cnt-pipeline AWS Instance)*
- Which EDF anonymizer is canonical now: edf_anonymize/anonymize_edfs.sh or the scripts on the Data pages?. *(Anonymize & Upload EDFs to ieeg.org)*
- Should scalp EDFs from collaborating sites go through this path or straight to BIDS?. *(Anonymize & Upload EDFs to ieeg.org)*
- What is the ieeg.org dataset-name convention for split recordings (HUPXXX_phaseII_D01?). *(Splitting Datasets)*
- Who may delete ieeg.org datasets uploaded by the lab?. *(Deleting a Dataset from ieeg.org)*
- Who administers the ieeg.org platform now, and where does a NeuroBridge member report an outage?. *(Restarting ieeg.org)*
- Which upload route is current after the May 2026 cnt1 crash: cnt2, cntgpu1, or neither?. *(Archiving ieeg Files)*
- Who owns the cntlitt Azure storage account and the restore budget, and may NeuroBridge staff write to it?. *(Archiving ieeg Files)*
- Can the original unarchiving SOP be recovered from the retired knowledge base or from Josh?. *(Unarchiving an ieeg Dataset)*
- Who is allowed to request a restore and what does it cost?. *(Unarchiving an ieeg Dataset)*
- Who handles restore tickets now?. *(Re-uploading Archived Datasets)*
- Does NeuroBridge run or only consume the scalp interictal pipeline?. *(Scalp EEG)*
- Who runs this pipeline today and how often; does NeuroBridge's data RC cover it?. *(EMU Interictal Scalp EEG Pipeline)*
- Which edit_studylist.py signature is current: with or without the admit_n and record_id arguments?. *(EMU Interictal Scalp EEG Pipeline)*
- Which edit_studylist.py calling convention is current?. *(EMU Interictal Scalp EEG Pipeline (duplicate - merge))*
- Which of Mxene, CHOP stim seizures and Epilog ESI are still active?. *(Special Protocols)*
- Is the Mxene electrode study still enrolling, and does NeuroBridge process its EEG?. *(Mxene EEG Processing & Upload)*
- Which ieeg.org project is correct: 'Mxene' or 'Mxene_Electrode'?. *(Mxene EEG Processing & Upload)*
- Is the CHOP stim-seizure collaboration active, and under what agreement does CHOP data sit on cnt-fs?. *(CHOP Stim Seizures EEG Processing)*
- Does the lab still send presurgical MRIs to Epilog for ESI, and who performs the export?. *(Epilog ESI Protocol)*
- Where is the EPILOG_# to patient mapping kept?. *(Epilog ESI Protocol)*

### REDCap & Clinical Metadata

- Which REDCap projects does NeuroBridge own or co-own versus only read from: CNT Surgical Repository, Multimodal Clinical 3T Repository (pid 42518), Quantitative MRI for Epilepsy Surgical Planning, EMU Scalp Interictal EEG?. *(REDCap & Clinical Metadata)*
- Who in NeuroBridge is the REDCap point of contact / project administrator?. *(REDCap & Clinical Metadata)*
- How should analysts obtain REDCap variables — personal API token, a periodic de-identified export by the data RC, or direct project access?. *(REDCap & Clinical Metadata)*
- Is the yearly RADAR metadata entry still performed, and by whom now (CNT CRC or NeuroBridge data RC)?. *(Clinical Data Pulls (EHR → REDCap))*
- Should 'Messaging in PennChart' stay in the REDCap theme or move to Operations?. *(Projects & Data Entry)*
- Is the yearly RADAR metadata entry now a NeuroBridge data-RC duty or still a CNT CRC duty?. *(RADAR Pull → REDCap Entry)*
- Do RADAR scans arrive de-identified (the imaging page names a 'mim_anon' share)? If not, why does this page name Borel as a destination?. *(RADAR Pull → REDCap Entry)*
- Which fields in pid 42518 are the analytically important ones (DRE, PNEE, lesion, laterality, Engel/ILAE) and are they QC'd before analysts use them?. *(RADAR Pull → REDCap Entry)*
- Who is the request contact for the pull if Joel Stein / Kate Davis are no longer the route for NeuroBridge?. *(RADAR Pull → REDCap Entry)*
- Is IC-CoDE applied to any REDCap neuropsych field, or was this only a reading reference for the CRC?. *(IC-CoDE Neuropsych (RADAR))*
- Is 'surgical outcomes project' the same REDCap project as the 'CNT Surgical Repository' / 'REDCap Surgical Repository' on other pages, and what is its PID?. *(Surgical Outcomes REDCap Project)*
- Who performs the yearly outcomes follow-up entry now — a CNT CRC, the NeuroBridge data RC, or nobody?. *(Surgical Outcomes REDCap Project)*
- Is this project the authoritative source of Engel/ILAE outcomes for NeuroBridge analyses, and how do analysts get a de-identified export?. *(Surgical Outcomes REDCap Project)*
- Does anyone in NeuroBridge still send these outcome requests, or is this entirely a CNT/PEC CRC task?. *(Messaging in PennChart)*
- Is 'on behalf of Kate Davis' still the correct authority if a NeuroBridge member sends it?. *(Messaging in PennChart)*
- Who in NeuroBridge holds User Rights admin on each REDCap project, and who approves identifier-level export rights?. *(REDCap Tips)*
- Should users from the collaborating sites ever have export rights beyond their own DAG?. *(REDCap Tips)*
- Who adjudicates ambiguous Engel→ILAE mappings now that 'flag these for me' no longer resolves to a person?. *(Seizure Terminology Reference)*
- Was the Engel→ILAE conversion applied retrospectively in the Surgical Repository, and should analyses use Engel, ILAE or both?. *(Seizure Terminology Reference)*
- Does anyone in NeuroBridge trigger these invites, or should the page live only in the CNT coordinator reference?. *(Triggering REDCap Scale Invites)*
- Which instrument names are current — prep_pre/prep_post or prep_epileptologists?. *(Triggering REDCap Scale Invites)*
- Do NeuroBridge analyses use the pre/post-conference scale data, and if so where is it exported to?. *(Triggering REDCap Scale Invites)*
- Which two REDCap projects are the 'old' and 'new' here, and is the migration finished?. *(Old → New REDCap Field Mapping)*
- Were the old-project records preserved so that 'non-lateralizing' can be recovered, and does any NeuroBridge analysis use the migrated fields?. *(Old → New REDCap Field Mapping)*
- Was the open iEEG interictal question ever resolved?. *(Old → New REDCap Field Mapping)*

### Operations

- Which Operations sections should NeuroBridge own, and which should link out to the CNT clinical team?. *(Operations)*
- Which system holds the live clinical trackers (REDCap, Box, SharePoint?) and who grants access?. *(Scheduling Trackers)*
- Which of these systems does a NeuroBridge data RC or analyst actually receive (SEAS email, Leif, Borel, PMACS VDI)?. *(CRC Access Checklist (systems, badges, trainings))*
- Who replaces 'Josh' as the IT/data-manager contact for NeuroBridge requests?. *(CRC Access Checklist (systems, badges, trainings))*
- Does anyone in NeuroBridge need CRMS, CAMRIS, Greenphire or Flywheel?. *(CRC Access Checklist (systems, badges, trainings))*
- Is Kristy Peters still the person who self-assigns F5 VPN requests?. *(UPHS F5 VPN Access)*
- Do NeuroBridge members file UPHS tickets themselves or through the data manager?. *(UPHS F5 VPN Access)*
- Does NeuroBridge still use MJ0HKNDA, and who holds its admin account now?. *(Remote Access to the Hayden Hall UPHS Computer)*
- Do collaborating sites enter data directly into NeuroBridge REDCap projects, or only Penn staff?. *(PennKey & REDCap Access for External Guests)*
- Who sponsors guest PennKeys for NeuroBridge collaborators?. *(PennKey & REDCap Access for External Guests)*
- Who owns NeuroBridge's REDCap projects and grants project-level access?. *(Requesting a REDCap Account)*
- Does NeuroBridge have its own Box root, and who owns it?. *(Adding Staff to the Penn+Box CNT Administration Folder)*
- Which ieeg.org projects and admins serve NeuroBridge?. *(Adding Users to the ieeg.org Portal)*
- Who in NeuroBridge owns onboarding now that the CNT data-manager role is shared?. *(Onboarding & Offboarding Checklist)*
- Which rows (Azure littlab, AWS upenn-ieeg, cntgpu1, Matlab) apply to NeuroBridge members?. *(Onboarding & Offboarding Checklist)*
- What is the offboarding rule for a departing trainee's data and code?. *(Onboarding & Offboarding Checklist)*
- Is the Summer 2025 deck shared with NeuroBridge members, and will NeuroBridge maintain its own deck?. *(CNT Data & Computing Orientation)*
- Does the NeuroBridge data RC hold PennChart access for retrospective pulls, or do pulls arrive via RADAR/honest broker only?. *(PennChart Training)*
- Where does NeuroBridge keep its study personnel list now that the old task-tool list is gone?. *(Adding Personnel to an IRB Study)*
- Which NeuroBridge protocols exist beyond the CNT ones, and who files their modifications?. *(Adding Personnel to an IRB Study)*
- What ORG code applies to NeuroBridge HSERA accounts?. *(Adding a Non-Penn / New Hire to a Study)*
- Where is the personnel list kept now?. *(Adding a Non-Penn / New Hire to a Study)*
- Are NeuroBridge trainees added to 821778, and who checks their binder folder?. *(e-Regulatory Binder & eDoA (Audit Prep))*
- Which NeuroBridge grants require inclusion-enrollment reporting, and from which REDCap project?. *(RPPR Demographic Tables)*
- Which 7T compensation figure is current: $50 (script) or $90/$100 (Greenphire page)?. *(7T Consent Script)*
- Which system now hosts the live trackers, and who is 'the CRC lead'?. *(Scan Scheduling Trackers (sEEG, 3T/fMRI, 7T))*
- MXene protocol number: 856681 or 858681?. *(Creating a Greenphire Account)*
- Where are participant payments logged for reconciliation?. *(Reimbursing a Participant)*
- Who in the lab is qualified to administer and score the battery, and who supervises?. *(Postop Neuropsych Testing: Overview)*
- Is initials+RID labelling of paper forms and photos approved under the protocol?. *(Running the Test)*
- Should the flash-drive password be rotated now that it was published? Is the drive still in use?. *(Neuropsych Battery: Materials)*
- Which contacts may appear in a GitHub-hosted wiki, and where should personal cells live instead?. *(Important Contacts & Emergency Numbers)*
- Who are the NeuroBridge-side contacts (data RC, cloud PM, regulatory)?. *(Important Contacts & Emergency Numbers)*
