# Migration to-do

Generated 2026-10-05 after the import from the lab's previous knowledge base. Tick items off as they are done; delete this file when it is empty.

## Attachments

All attachments were downloaded and reviewed for patient identifiers; 153 were committed under `docs/assets/<theme>/<page>/`. The rest are listed here.

**Screenshots withheld after PHI review** (each shows as a red 🚫 note on its page; replace with a de-identified capture):

- [ ] **Flywheel → cnt-fs (3T)** (`docs/imaging/post-scan-transfer/flywheel-cnt-fs-3t.md`) — Real coded research subjects (sub-RID0985, RID983, etc., plus ex723011331) paired with exact scan dates/times; acquisition dates visible
- [ ] **Opening ITK-SNAP Files from PennBox** (`docs/imaging/electrode-reconstruction/opening-itk-snap-files-from-pennbox.md`) — Non-defaced MRI: sagittal view shows facial soft-tissue profile (nose, lips, chin) of a real coded subject
- [ ] **Opening ITK-SNAP Files from PennBox** (`docs/imaging/electrode-reconstruction/opening-itk-snap-files-from-pennbox.md`) — Non-defaced MRI: sagittal view shows facial soft-tissue profile of a real coded subject
- [ ] **Seizure Terminology Reference** (`docs/redcap/projects-and-data-entry/seizure-terminology-reference.md`) — Open patient chart tab 'Collins, Maurice' visible in Epic header; patient name on a hospital record screen (staff user Gabriela Bustamante also shown)

**Screen recordings kept out of Git** (GitHub's 100 MB file limit; stored outside Git by the NeuroBridge Lab for now and referenced from the page; move them to a CNT location):

- [ ] **Grid Electrode Labeling Conventions** (`docs/imaging/electrode-reconstruction/grid-electrode-labeling-conventions.md`) — video1338425901.mp4
- [ ] **RPPR Demographic Tables** (`docs/operations/regulatory-irb-and-reporting/rppr-demographic-tables.md`) — RPPR_Demographic_Table_Video_Tutorial.mov
- [ ] Decide whether recordings should move to Penn+Box or Git LFS; update the links on those pages accordingly.

## Pages that need a human pass

- [ ] Reshape migrated pages into the house template (Purpose / Scope / Prerequisites / Procedure / Troubleshooting / Notes), one theme at a time; a page counts as verified once someone has followed it and committed the fixes (git keeps the date and the name).
- [ ] Merge the duplicate scalp-EEG pipeline page and delete the copy.
- [ ] Pages whose original held a password (now removed): confirm the credential is in the password manager, then remove the warning box.
- [ ] Write the gap pages: Data › Standards (the Data Structure v1.0 specification), Data › Site intake protocol, Data › Inventory, REDCap › Overview, Compute › Environments (conda / modules).
- [ ] Bring over the three pages still marked *(not yet in the wiki)*: Data Structure v1.0, Sites, Access CNT1 and CNT-fs.
- [ ] Add the first stroke / neuromodulation and TBI procedures and introduce a `program:` front-matter field so the Map can show a per-program view.
- [ ] One retired page was not imported: the procedure for importing REDCap reports into the old task tracker (obsolete with the tracker).
- [ ] Replace the placeholder handles in `CODEOWNERS`; set `site_url` in `mkdocs.yml` if the site is ever hosted.
