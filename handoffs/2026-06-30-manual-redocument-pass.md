# Re-document pass — older user-manual DRAFT pages

**Created:** 2026-06-30 · **From:** Manual navigation/overview thread · **Area:** @gallery / docs

## Context

The user manual is being rebuilt page-by-page from **verified live behavior** using the
`openelis-user-manual` skill (At-a-glance table → Overview → numbered steps each with one real
screenshot → field reference → notes) under the **Review gate**. The Environmental, Vector, and
Test Catalog workflows are done and now navigable on Confluence:

- Environmental Surveillance — workflow overview: **1437466625** (6 child pages)
- Vector Surveillance — workflow overview: **1437532161** (5 child pages)
- Test Catalog Management — workflow overview: **1437270018** (14 child pages)
- Shared pages (under review parent, linked from both): order wizard 1428881409, Label & store 1428684802, Complete QA review 1429176321
- Verified standalone: Electronic Signatures 1242759175, Adding a Patient 1418166310

**Retired 2026-06-30** (deleted → Confluence trash, recoverable): the 4 old *combined* env/vector
pages superseded by the granular set — 1420099592, 1421148161, 1420230657, 1420460034.

## The re-document queue — older spec-derived DRAFTs still under review parent 1189609473

These were authored from specs **before** the verify-first process. Each needs: verify on a live
instance → rewrite with the `openelis-user-manual` skill + Review gate → draft-first under
1189609473 → group into a workflow overview + two-way nav where it forms a multi-page flow →
gray-state/defer anything not actually built.

**Operational / workflow**
- Results Entry — By Range, By Patient, By Order — 1189380105
- Validation Modes — By Order, By Range, By Date — 1189707840
- Patient Management — Search, Create, Edit & Merge — 1189642248
- Order Search & Lookup — 1189543945
- Sample Storage Management — 1189281794
- Aliquot Management — 1189543964
- Non-Conforming Events — Corrective Actions — 1188593667
- Electronic Lab Notebook — 1188560901

**Referrals (collapse the duplicate)**
- Sample Shipment & Referral Management — 1188462607
- Referral — Sending Samples to External Labs — 1188626437
- → merge into one; reconcile against the shipped referral redesign (in-transit signal = ReferralStatus; canonical view /SampleShipment/reference-lab-results)

**Dashboards / monitoring**
- Westgard Rules Dashboard — 1188429833
- Freezer Monitoring Dashboard — 1188855815
- Dashboard & KPI Cards — 1189740580

**Modules (verify built-state first)**
- External Quality Assurance (EQA) Module — 1189773314 — EQA V2 specced but NOT built; gray-state/defer
- Reagent & Consumables Management — 1189675014 — reagents exist but Test→Reagent linkage NOT built; defer that part

**Reports / export**
- Running Reports (How-To Guide) — 1188528150
- Data Export — CSV, PDF & WHONET — 1189576725

**Reflex / Calculated (collapse the duplicate)**
- Admin — Reflex Tests & Calculated Value Tests — 1189707859 (March, combined)
- Calculated Value Tests — User Guide — 1211695123 (April, standalone)
- Reflex Testing — User Guide — 1211400207 (April, standalone)
- → the two April standalone guides likely supersede the combined March admin page; reconcile/retire

**Admin set**
- Admin — Organization Management — 1188790284
- Admin — Lab Number, Program Entry & EQA Program Management — 1188462628
- Admin — Provider Management & Plugin Management — 1188724740
- Admin — General Configuration (Site, Branding & Workflow Settings) — 1188757510
- Admin — Language, Translation & Menu Configuration — 1188397063
- Admin — Notifications, Result Reporting & User Communication — 1189380143
- Admin — System Tools (Search Index, Logging & Audit Trail) — 1188397085

**Other**
- Language Switching & Session Management — 1188429853
- Admin — Sample Type Management (draft — verify) — 1420853278 — newer-style; verify + likely nest under Test Catalog overview

## Next action

Triage this list with Casey into **retire-more / merge / verify-and-rewrite**, then start the
verify+rewrite with the highest-traffic operational pages (Results Entry, Validation Modes,
Patient Management). Capture screenshots serialized on the Mac (openelis-screenshots harness).
Several admin pages map to the verified data models already in memory (Application Properties,
Site Information, Menu Configuration, Validation Configuration, etc.) — reuse those.
