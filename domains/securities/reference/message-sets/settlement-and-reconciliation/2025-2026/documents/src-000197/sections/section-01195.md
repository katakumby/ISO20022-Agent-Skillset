---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.95 Linkages73"]
file_pages: [1646]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.95 Linkages73

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1646 to 1646.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1646

```text
CorporateActionEventType <CorpActnEvtTp> contains one of the following elements (see
"CorporateActionEventType110Choice" on page 1651 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1651
Or}   Proprietary <Prtry> [1..1] ± 1658
Constraints
• EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event triggers a
securities movement as per the Event Interpretation Grid published by the Securities Market Practice
Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is decided
by the issuer and not by the holders.
35.1.16.95  Linkages73
Definition: Information related to a linked transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C11 1646
   MessageNumber <MsgNb> [0..1] ± C20 1647
   Reference <Ref> [1..1] ± 1647
   ReferenceOwner <RefOwnr> [0..1] ± 1648
35.1.16.95.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: Specifies when the transaction is to be executed relative to a linked transaction.
Impacted by: C11 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition8Choice" on page 1597 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1597
Or}   Proprietary <Prtry> [1..1] ± 1598
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1646 March 2026
```

