---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.80 AdditionalParameters24", "35.1.16.80.3 PreviousPartialConfirmationIdentification <PrvsPrtlConfId>"]
file_pages: [1628]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.80.3 PreviousPartialConfirmationIdentification <PrvsPrtlConfId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1628 to 1628.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1628

```text
Definition: Specifies partial settlement information.
Datatype: "PartialSettlement2Code" on page 2089
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
35.1.16.80.3  PreviousPartialConfirmationIdentification <PrvsPrtlConfId>
Presence: [0..1]
Definition: Identification of the confirmation previously sent to confirm the partial settlement of a
transaction.
Datatype: "Max35Text" on page 2192
35.1.16.81  UpdateType15Choice
Definition: Choice of format for the update information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1628
Or}   Proprietary <Prtry> [1..1] ± 1628
35.1.16.81.1  Code <Cd>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Datatype: "StatementUpdateType1Code" on page 2171
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
35.1.16.81.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1628 March 2026
```

