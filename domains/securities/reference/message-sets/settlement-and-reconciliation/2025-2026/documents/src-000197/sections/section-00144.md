---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.3 SubBalance <SubBal>", "7.4.6.3.3 IntraPositionMovement <IntraPosMvmnt>", "7.4.6.3.3.8 AvailableDate <AvlblDt>"]
file_pages: [196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.3.3.8 AvailableDate <AvlblDt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 196 to 196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 196

```text
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
7.4.6.3.3.8  AvailableDate <AvlblDt>
Presence: [0..1]
Definition: Date/time securities become available for sale (if securities become unavailable, this
specifies the date/time at which they will become available again).
AvailableDate <AvlblDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
7.4.6.3.3.9  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 2185
7.4.6.3.3.10  CorporateActionEventType <CorpActnEvtTp>
Presence: [0..1]
Definition: Specifies the type of corporate event.
Impacted by: C13 "EventTypeRule"
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
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 196 March 2026
```

