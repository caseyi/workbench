# Manual coverage backlog — author fresh, verify-first (old DRAFTs retired)

**Created:** 2026-06-30 · **From:** Manual navigation/overview thread · **Area:** @gallery / docs

## Context

The user manual is being rebuilt page-by-page from **verified live behavior** using the
`openelis-user-manual` skill (At-a-glance table → Overview → numbered steps each with one real
screenshot → field reference → notes) under the **Review gate**. The Environmental, Vector, and
Test Catalog workflows are done and navigable on Confluence:

- Environmental Surveillance — workflow overview: **1437466625** (6 child pages)
- Vector Surveillance — workflow overview: **1437532161** (5 child pages)
- Test Catalog Management — workflow overview: **1437270018** (14 child pages)
- Shared pages (under review parent 1189609473, linked from both): order wizard 1428881409, Label & store 1428684802, Complete QA review 1429176321
- Verified standalone: Electronic Signatures 1242759175, Adding a Patient 1418166310
- Held back for verify + nest under Test Catalog: Admin — Sample Type Management 1420853278

**Retired 2026-06-30** (deleted → Confluence trash, recoverable): the 4 old *combined* env/vector
pages (1420099592, 1421148161, 1420230657, 1420460034) **and** the 28 spec-era "DRAFT:" pages
below — none were good enough to rewrite from. The **topics** still need first-class, verify-first
pages; this is now a coverage backlog, not a rewrite list.

## Coverage backlog — topics still needing a verify-first manual page

For each: verify on a live instance → build with the `openelis-user-manual` skill + Review gate →
draft-first under 1189609473 → group into a workflow overview + two-way nav where it forms a
multi-page flow → gray-state/defer anything not actually built. Reuse the verified data models
already in memory for the admin topics (Application Properties, Site Information, Menu
Configuration, Validation Configuration, etc.).

**Operational / workflow**
- Results Entry — By Range, By Patient, By Order
- Validation Modes — By Order, By Range, By Date
- Patient Management — Search, Create, Edit & Merge
- Order Search & Lookup
- Sample Storage Management
- Aliquot Management
- Non-Conforming Events — Corrective Actions
- Electronic Lab Notebook

**Referrals** — single page (the old set had two overlapping drafts); reconcile against the shipped
referral redesign (in-transit signal = ReferralStatus; canonical view /SampleShipment/reference-lab-results)

**Dashboards / monitoring**
- Westgard Rules Dashboard
- Freezer Monitoring Dashboard
- Dashboard & KPI Cards

**Modules (verify built-state first)**
- External Quality Assurance (EQA) — EQA V2 specced but NOT built; gray-state/defer
- Reagent & Consumables Management — reagents exist but Test→Reagent linkage NOT built; defer that part

**Reports / export**
- Running Reports (How-To)
- Data Export — CSV, PDF & WHONET

**Reflex / Calculated** — one set of guides (old set had a March combined admin page + two April
standalone guides); author clean Calculated Value Tests + Reflex Testing pages

**Admin**
- Organization Management
- Lab Number, Program Entry & EQA Program Management
- Provider Management & Plugin Management
- General Configuration (Site, Branding & Workflow Settings)
- Language, Translation & Menu Configuration
- Notifications, Result Reporting & User Communication
- System Tools (Search Index, Logging & Audit Trail)

**Other**
- Language Switching & Session Management

## Next action

Pick the highest-traffic operational topics first — Results Entry, Validation Modes, Patient
Management — capture screenshots serialized on the Mac (openelis-screenshots harness), build with
the manual skill + Review gate, draft under 1189609473.
