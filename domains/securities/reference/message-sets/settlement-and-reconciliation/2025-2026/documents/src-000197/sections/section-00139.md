---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks", "7.4.6 FinancialInstrument <FinInstrm>", "7.4.6.3 SubBalance <SubBal>", "7.4.6.3.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7.4.6.3.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 191 to 191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 191

```text
SubBalance <SubBal> contains the following IntraPositionDetails66 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [0..1] ± 191
   BalanceFrom <BalFr> [1..1] ± 192
   IntraPositionMovement <IntraPosMvmnt> [1..*]  C4 192
     Identification <Id> [0..1] ± 193
     SettledQuantity <SttldQty> [1..1] ± C12 194
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C12 194
     RemainingToBeSettledQuantity
<RmngToBeSttldQty>
[0..1] ± C12 194
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 195
     BalanceTo <BalTo> [1..1] ± 195
     SettlementDate <SttlmDt> [1..1] ± 195
     AvailableDate <AvlblDt> [0..1] ± 196
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 196
     CorporateActionEventType <CorpActnEvtTp> [0..1] ± C13 196
     CollateralMonitorAmount <CollMntrAmt> [0..1] ± 197
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 197
     SupplementaryData <SplmtryData> [0..*] ± C22 197
Constraints
• BalanceFromToRule2
BalanceFrom/Code must be different from the IntraPositionMovement/BalanceTo/Code.
On Condition
    /IntraPositionMovement[*]/BalanceTo/Code is present
 And    /BalanceFrom/Code is present
Following Must be True
    /IntraPositionMovement[*]/BalanceTo/Code Must be different from /BalanceFrom/
Code
7.4.6.3.1  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 191 March 2026
```

