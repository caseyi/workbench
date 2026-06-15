# Tasks

<!-- Areas (context clusters): @micro @catalog @vector @results @reports @pathology
     @referrals @strategy @jira-admin @gallery @admin @design-system
     Item format: - [ ] **Title** - context #type @area (from: thread) (touched: YYYY-MM-DD)
     Resume pointer: end the context with what a cold start needs — branch/PR, key file path,
     ticket id, and the NEXT concrete action. Big context -> handoffs/<file>.md, linked with →.
     Items are grouped by area within each section so related work sits together. -->

## Inbox

## Active

- [ ] **Decide Catalog Subscription epic questions** - create epic + relate to OGC-782 and Test Catalog v2.5; keep OGC-447, close OGC-442 as dup #jira @catalog @micro (from: AMR review workflow UX) (touched: 2026-06-12)
- [ ] **Write breakpoint-source decision to Confluence** - research done (AMR R package, GPL-2.0, CLSI/EUCAST), page never written #design @micro (from: AMR review workflow UX) (touched: 2026-06-12)
- [ ] **Build Sync 6/7 PR from clean worktree** - 7 overwritten FRSes staged in upload/, instructions in gallery-registration.md #design @micro @gallery (from: AMR review workflow UX) (touched: 2026-06-12)
- [ ] **Reconcile stranded design/micro-m10-m12-prototypes branch** - ledger says OPEN but no live PR, prototypes not on main #design @micro @gallery (from: Design folder cleanup + OpenELIS gallery) (touched: 2026-06-12)
- [ ] **Spec post-MVP test-rules features** - MVP fully in Jira (OGC-730 + children 731–735); §10.1/§10.2 buckets have no FRS or mockup yet; run /specify on simulator+validation tests, multi-step calc, algorithm-as-graph (canvas preview exists), templates+conflict-detection before any new Jira #design #jira @catalog → handoffs/2026-05-29-test-rules-post-mvp-spec.md (from: Calculated values & reflex tests) (touched: 2026-05-29)
- [ ] **Finish scheduling OGC-361 into ENV S2** - blocked on issue type flipping Sub-task → Story, then one-shot sprint+due-date edit #jira @vector @jira-admin (from: PNG work plan) (touched: 2026-06-12)
- [ ] **Open/merge v2-mockups PR** - design/v2-mockups-uncertainty-and-trap-details pushed, PR never created; gallery permalinks live only after merge #design @vector @gallery (from: Vector & env mockups) (touched: 2026-06-12)
- [ ] **Merge s06-v2-lhu-rewrite FRS PR** - separate still-open PR #design @vector @gallery (from: Vector & env mockups) (touched: 2026-06-12)
- [ ] **Open PR for design/results-validation-v4 branch** - branch pushed (v3 retirement + print queue), PR never opened, not in PENDING-PRS ledger #design @results @gallery (from: OpenELIS gallery) (touched: 2026-06-12)
- [ ] **Walk orphan-design review list (Register vs Archive)** - 26 unregistered files across 16 features triaged, each needs a keep-or-archive call #design @gallery (from: Design folder cleanup) (touched: 2026-06-12)
- [ ] **Triage seven most-stale Jira tickets** - OGC-19/21/22/23/7/18 + OEDIGI-31 untouched 1+ year; keep vs close #jira @jira-admin (from: December features review) (touched: 2026-06-12)
- [ ] **Resolve Jira workflow open decisions + Phase 2 admin setup** - DECISIONS RESOLVED (3 adopted: Cloud-native automation in place of post-functions, Contract as custom single-select field, per-Component acceptance owners + column WIP limits) + full critique folded in -> v2 doc `OpenELIS Feature Design/OGC-Jira-Reorg-Proposal-v2.docx`. OGC confirmed company-managed Jira Cloud (uwdigi). #digi-devs summary staged as DRAFT (not sent). Phase 1 label sweep DONE via connector: 154 ACTIVE issues normalized (case-conflict caps->lowercase, qa-release retired into qa-menu, SILNAS/silnas->indonesia; Done issues untouched; verified qa-release=0 active). NEXT: Phase 2 structural config is admin-console/Chrome (connector cannot do admin) - create OGC Lean workflow + Acceptance status, 'Rejection reason' required transition-screen field, Reject Count number field + Automation increment rule, Contract single-select field, Tech Debt issue type, 12 Components+leads, board WIP limits, doc-subtask Automation (trigger=In Review), saved filters. Then Phase 3 contract sweep + Phase 4 components/tech-debt (connector-automatable once fields/components exist). #jira @jira-admin (from: Jira statuses) (touched: 2026-06-14)
- [ ] **Answer roadmap scoping questions** - synthesis (incl. two-web-properties finding) blocked on two questions that never got answered #openelis @strategy (from: Roadmap priorities) (touched: 2026-06-12)

## Waiting On

- [ ] **M-10 AMR-delta extension stories** - drafting deferred until Catalog Subscription epic exists #jira @micro @catalog (from: AMR review workflow UX) (since: 2026-06-12)
- [ ] **Gallery: retire v3 results-validation entries** - handoff staged at upload/gallery-handoff-retire-v3-results-validation.md (9 files), gallery thread must run it #design @results @gallery (from: Results entry handoff) (since: 2026-06-12)
- [ ] **Gallery: register report-print-queue slug** - edit staged in upload/REGISTER-report-print-queue.md; until run, mockup permalink + OGC-1031..1043 links 404 #design @reports @gallery (from: Report print queue) (since: 2026-06-12)
- [ ] **Reagan re: OGC-779 Program-pattern architecture** - Vector Field Survey mockup blocked on his confirmation #design @vector (from: Vector & env mockups) (since: 2026-06-12)
- [ ] **Herbert re: OGC-267 direction** - comment posted with 3 paths (refocus / close as superseded / continue selectively); ping him directly #jira @pathology (from: Cytology revision) (since: 2026-06-12)
- [ ] **Referral redesign feedback** - Confluence page created + Slack ping sent, no visible response; check thread and page #design @referrals (from: Referral redesign) (since: 2026-06-12)
- [ ] **Create Jira Fix Version "PNG / CPHL Phase II"** - doesn't exist in OGC project settings; needed for epic/story completion rollup #jira @jira-admin (from: Report print queue) (since: 2026-06-12)

## Someday

- [ ] **Mockup OGC-776 LHU amendment dialog** - flagged as obvious next candidate, small and self-contained #design @vector (from: Vector & env mockups) (touched: 2026-06-12)
- [ ] **Plain-English lab-usage summary on OGC-552** - optional, offer stands #jira @vector (from: Vector & env mockups) (touched: 2026-06-12)
- [ ] **Accessibility audit of v4 results/validation surfaces** - flagged as the one open recommendation before build #qa #design @results (from: Results entry handoff) (touched: 2026-06-12)
- [ ] **Start P0 auto-verify (result-release pipeline) FRS** - top of P0–P12 stack, natural follow-on from QC engine #design @results (from: Competitor comparison) (touched: 2026-06-12)
- [ ] **Validate 93 "Open" Crosswalk backlog rows** - classification never human-reviewed #openelis @strategy (from: Competitor comparison) (touched: 2026-06-12)
- [ ] **Sanity-check Crosswalk Scope Decisions tab** - 3 judgment calls invited pushback: Epic/Cerner connectors punt, patient portal punt, AI/ML to 2027 #openelis @strategy (from: Competitor comparison) (touched: 2026-06-12)
- [ ] **Run /breakdown on OGC-266 v2** - epic description includes suggested 3-version breakdown, never executed #design @pathology (from: Cytology revision) (touched: 2026-06-12)
- [ ] **Decide if Unarchive needs its own permission** - v1 reuses Admin bundle for Archive + Unarchive; noted but not pursued #design @admin (from: Equipment & Crit Ack) (touched: 2026-06-12)
- [ ] **Finish style-guide v2 patterns inventory** - content refreshed and PR'd, audit coverage table still incomplete #design @design-system (from: Design folder cleanup) (touched: 2026-06-12)

## Done
