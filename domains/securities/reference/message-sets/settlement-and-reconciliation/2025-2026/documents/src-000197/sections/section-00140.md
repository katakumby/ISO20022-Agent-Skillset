---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.3 SubBalance <SubBal>", "7.4.6.3.2 BalanceFrom <BalFr>"]
file_pages: [192]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.3.2 BalanceFrom <BalFr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 192 to 192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 192

```text
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat41Choice" on page 1648 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1649
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1649
     Identification <Id> [0..1] Text 1649
Or   Country <Ctry> [1..1] CodeSet C7 1649
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1650
Or   TypeAndIdentification <TpAndId> [1..1]  1650
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1650
     Identification <Id> [1..1] IdentifierSet C5 1650
Or}   Proprietary <Prtry> [1..1] ± 1651
7.4.6.3.2  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the securities were moved.
BalanceFrom <BalFr> contains one of the following elements (see "SecuritiesBalanceType6Choice"
on page 1427 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1427
Or}   Proprietary <Prtry> [1..1] ± 1429
7.4.6.3.3  IntraPositionMovement <IntraPosMvmnt>
Presence: [1..*]
Definition: Intra-position movement(s) having been performed.
Impacted by: C4 "AdditionalDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 192 March 2026
```

