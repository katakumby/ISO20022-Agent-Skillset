---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.30 CorporateActionEventStageFormat13Choice"]
file_pages: [931]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.30 CorporateActionEventStageFormat13Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 931 to 931.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 931

```text
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.15.30  CorporateActionEventStageFormat13Choice
Definition: Choice between a standard code or proprietary code to specify the event stage type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 931
Or}   Proprietary <Prtry> [1..1] ± 932
16.1.15.30.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the stage of the corporate action event.
Datatype: "CorporateActionEventStage3Code" on page 1168
CodeName Name Definition
APPD Approved Approved at the relevant meeting, for
example, dividend.
CLDE Deactivated Offer is closed for acceptance.
FULL CancellationAndReRun Cancellation and re-run of an original
lottery or an original and supplemental
lottery. A subsequent lottery will be
performed under a new event.
LAPS Lapsed Event/offer conditions have not been met
and the event/offer is terminated or
lapsed.
PART SupplementalCancellationAndReRun Cancellation and re-run of a
supplemental lottery only. A subsequent
new supplemental lottery will be
performed under the original event.
PWAL ActionPeriod Open for acceptance until the next
specified deadline in the announcement
(if any).
RESC SupplementalCancellation A supplemental lottery is being cancelled
by the issuer. No subsequent lottery will
be performed.
SUAP SubjectToApproval Subject to approval at the relevant
meeting, for example, dividend.
UNAC UnconditionalAsToAcceptance The required level of acceptances
specified in the terms of the offer has
been achieved but there are still
outstanding conditions to fulfil.
WHOU WhollyUnconditional Wholly unconditional; all conditions
specified in the offer document have
been satisfied.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 931 February 2026
```

