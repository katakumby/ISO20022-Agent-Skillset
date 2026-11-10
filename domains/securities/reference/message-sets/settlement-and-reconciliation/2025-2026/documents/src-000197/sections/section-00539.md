---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.5 RequestDetails <ReqDtls>", "25.4.5.3 AutomaticBorrowing <AutomtcBrrwg>"]
file_pages: [809]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.5.3 AutomaticBorrowing <AutomtcBrrwg>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 809 to 809.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 809

```text
RestrictionReference <RstrctnRef> contains the following elements (see "RestrictionIdentification1"
on page 1589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 1589
   Identification <Id> [1..1] Text 1590
25.4.5.3  AutomaticBorrowing <AutomtcBrrwg>
Presence: [0..1]
Definition: Condition for automatic borrowing.
AutomaticBorrowing <AutomtcBrrwg> contains one of the following elements (see
"AutomaticBorrowing7Choice" on page 1599 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1599
Or}   Proprietary <Prtry> [1..1] ± 1599
25.4.5.4  RetainIndicator <RtnInd>
Presence: [0..1]
Definition: Indicates whether the instruction due to expire is confirmed for settlement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
25.4.5.5  Linkage <Lkg>
Presence: [0..1]
Definition: Specifies the type of linkage requested.
Linkage <Lkg> contains one of the following elements (see "LinkageType3Choice" on page 1634 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1634
Or}   Proprietary <Prtry> [1..1] ± 1634
25.4.5.6  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 809 March 2026
```

