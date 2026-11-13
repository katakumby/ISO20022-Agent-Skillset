---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.4 CorporateActionEventProcessingStatus <CorpActnEvtPrcgSts>", "35.1.29.22.4.2 Proprietary <Prtry>"]
file_pages: [1909]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.4.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1909 to 1909.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1909

```text
35.1.29.22.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Status of a corporate action or the status of a payment expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.5  CorporateActionEventStage <CorpActnEvtStag>
Presence: [1..1]
Definition: Stage in the corporate action event life cycle.
CorporateActionEventStage <CorpActnEvtStag> contains one of the following
CorporateActionEventStage3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1909
Or}   Proprietary <Prtry> [1..1] ± 1910
35.1.29.22.5.1  Code <Cd>
Presence: [1..1]
Definition: Corporate action event stage expressed as an ISO 20022 code.
Datatype: "CorporateActionEventStage2Code" on page 2050
CodeName Name Definition
PWAL ActionPeriod Open for acceptance until the next
specified deadline in the announcement
(if any).
SUAP SubjectToApproval Subject to approval at the relevant
meeting, eg, dividend.
APPD Approved Approved at the relevant meeting, eg,
dividend.
UNAC UnconditionalAsToAcceptance The required level of acceptances
specified in the terms of the offer has
been achieved but there are still
outstanding conditions to fulfil.
WHOU WhollyUnconditional Wholly unconditional; all conditions
specified in the offer document have
been satisfied.
CLDE Deactivated The offer is closed for acceptance.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1909 March 2026
```

