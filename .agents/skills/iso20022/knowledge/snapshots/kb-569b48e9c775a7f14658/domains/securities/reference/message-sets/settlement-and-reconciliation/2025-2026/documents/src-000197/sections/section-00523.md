---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.4 Message Building Blocks", "24.4.4 RequestDetails <ReqDtls>", "24.4.4.4 RetainIndicator <RtnInd>"]
file_pages: [792]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.4.4.4 RetainIndicator <RtnInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 792 to 792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 792

```text
AutomaticBorrowing <AutomtcBrrwg> contains one of the following elements (see
"AutomaticBorrowing7Choice" on page 1599 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1599
Or}   Proprietary <Prtry> [1..1] ± 1599
24.4.4.4  RetainIndicator <RtnInd>
Presence: [0..1]
Definition: Indicates whether the instruction due to expire is confirmed for settlement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
24.4.4.5  Linkage <Lkg>
Presence: [0..1]
Definition: Specifies the type of linkage requested.
Linkage <Lkg> contains one of the following elements (see "LinkageType3Choice" on page 1634 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1634
Or}   Proprietary <Prtry> [1..1] ± 1634
24.4.4.6  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 1541 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 1541
Or}   Proprietary <Prtry> [1..1] ± 1541
24.4.4.7  OtherProcessing <OthrPrcg>
Presence: [0..*]
Definition: Specifies another type of processing change request.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 792 March 2026
```

