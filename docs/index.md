---
title: "Home"
hide:
  - navigation
  - toc
---

<section class="nb-banner" markdown="0">
  <div class="nb-banner__left">
    <h1>CNT Procedures Manual</h1>
    <p class="nb-banner__tag">Center for Neuroengineering &amp; Therapeutics, University of Pennsylvania</p>
    <div class="nb-banner__actions">
      <a class="nb-btn nb-btn--primary" href="about/roles/">Start with your role</a>
      <a class="nb-btn" href="map/">Map of the wiki</a>
    </div>
  </div>
  <p class="nb-banner__intro">This manual holds the standard operating procedures of the CNT research teams: clinical research coordinators, data staff and the people who keep the pipelines running. Procedures are grouped under six systems and cross-referenced by stage in the data lifecycle and by role. The manual contains no patient identifiers and no credentials. Anyone on the team can edit it.</p>
</section>

<div class="nb-grid" markdown="0">
  <section class="nb-card">
    <h2><a href="data/">Data</a></h2>
    <p>Where the lab's data is kept and how it is laid out, moved between servers, archived to Azure, shared through Pennsieve and ieeg.org, and de-identified.</p>
    <p class="nb-card__links"><a href="data/storage-locations/data-storage-locations/">Data storage locations</a> · <a href="data/moving-data/moving-data-across-cnt-fs-cnt1-bsc-borel-and-leif/">Moving data across servers</a> · <a href="data/de-identification/de-identifying-edfs/">De-identifying EDFs</a> · <a href="data/sharing-pennsieve-and-ieeg-org/uploading-from-cnt1-to-pennsieve/">Uploading to Pennsieve</a></p>
  </section>
  <section class="nb-card">
    <h2><a href="compute/">Compute</a></h2>
    <p>The servers, clusters and cloud accounts the lab computes on, the software installed on them, and how to obtain access.</p>
    <p class="nb-card__links"><a href="compute/overview/overview-of-cnt-systems/">Overview of CNT systems</a> · <a href="compute/seas-cets-servers/accessing-borel-over-ssh/">Accessing Borel over SSH</a> · <a href="compute/seas-cets-servers/submitting-jobs-with-slurm/">Submitting jobs with SLURM</a> · <a href="compute/pmacs-psom-systems/pmacs-vpn/">PMACS VPN</a></p>
  </section>
  <section class="nb-card">
    <h2><a href="imaging/">Imaging</a></h2>
    <p>MRI and CT, from scheduling a scan through the scanner session, transfer of the images, conversion to NIfTI and reconstruction of electrode positions.</p>
    <p class="nb-card__links"><a href="imaging/scheduling-and-visits/visit-checklist-3t-study/">Visit checklist for a 3T study</a> · <a href="imaging/at-the-scanner/running-the-7t/">Running the 7T</a> · <a href="imaging/post-scan-transfer/flywheel-cnt-fs-3t/">Flywheel to cnt-fs</a> · <a href="imaging/electrode-reconstruction/gui-docker-reconstruction-workflow/">Electrode reconstruction</a></p>
  </section>
  <section class="nb-card">
    <h2><a href="electrophysiology/">Electrophysiology</a></h2>
    <p>Scalp and intracranial EEG, from acquisition in the epilepsy monitoring unit through export from Natus, channel mapping and publication on ieeg.org.</p>
    <p class="nb-card__links"><a href="electrophysiology/exporting-from-natus/exporting-files-from-natus/">Exporting files from Natus</a> · <a href="electrophysiology/channel-mapping/automated-channel-mapping/">Automated channel mapping</a> · <a href="electrophysiology/processing-and-upload-to-ieeg-org/processing-for-ieeg-org-natus2mef-validate-upload/">Processing for ieeg.org</a> · <a href="electrophysiology/overview-and-setup/seeg-phase-ii-processing-overview-and-timeline/">Phase II timeline</a></p>
  </section>
  <section class="nb-card">
    <h2><a href="redcap/">REDCap &amp; Clinical Metadata</a></h2>
    <p>The REDCap projects that hold clinical variables, the conventions for entering data in them, and the pulls from the electronic health record that feed them.</p>
    <p class="nb-card__links"><a href="redcap/projects-and-data-entry/surgical-outcomes-redcap-project/">Surgical Outcomes project</a> · <a href="redcap/projects-and-data-entry/redcap-tips/">REDCap tips</a> · <a href="redcap/clinical-data-pulls-ehr-redcap/radar-pull-redcap-entry/">RADAR pull to REDCap</a> · <a href="redcap/projects-and-data-entry/seizure-terminology-reference/">Seizure terminology</a></p>
  </section>
  <section class="nb-card">
    <h2><a href="operations/">Operations</a></h2>
    <p>Accounts and access, onboarding and offboarding, IRB submissions, consent, scheduling, participant reimbursement, neuropsychological testing and contacts.</p>
    <p class="nb-card__links"><a href="operations/access-and-accounts/crc-access-checklist-systems-badges-trainings/">Access checklist</a> · <a href="operations/onboarding-and-offboarding/onboarding-and-offboarding-checklist/">Onboarding and offboarding</a> · <a href="operations/regulatory-irb-and-reporting/adding-personnel-to-an-irb-study/">Adding personnel to an IRB study</a> · <a href="operations/consenting/consent-signing-checklist/">Consent signing checklist</a></p>
  </section>
</div>

<div class="nb-columns" markdown="0">
  <section>
    <h2>Reading by role</h2>
    <p>Every procedure is tagged with the roles that perform it. Clinical research coordinators begin with Operations and Imaging; data staff with Data, Compute and Electrophysiology.</p>
    <ul>
      <li><a href="about/roles/">Roles</a>: what each role is expected to know</li>
      <li><a href="tags/">Tags</a>: every procedure listed under its stage and roles</li>
      <li><a href="map/">Map</a>: a graph of the procedures by system, by stage, or by role</li>
    </ul>
  </section>
  <section>
    <h2>Contributing</h2>
    <p>To correct a page, use the edit button at the top of it, or edit the Markdown in Obsidian and commit. See <a href="about/contributing/">how contributing works</a>, the <a href="about/style-guide/">style guide</a> and the <a href="about/sop-template/">SOP template</a>. Pages flagged by the October 2026 audit carry a banner; the full list is in <code>AUDIT.md</code> in the repository.</p>
  </section>
</div>
