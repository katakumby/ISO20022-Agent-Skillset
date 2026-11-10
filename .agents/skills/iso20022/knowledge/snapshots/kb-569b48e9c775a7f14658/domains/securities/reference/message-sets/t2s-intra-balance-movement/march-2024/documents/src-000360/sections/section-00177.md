---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.5 Movement <Mvmnt>", "10.4.4.1.5.11 MovementDetails <MvmntDtls>", "10.4.4.1.5.11.1 BalanceFrom <BalFr>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.5.11.1 BalanceFrom <BalFr>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 227
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 227
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 228
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 228
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 228
Or       PoolIdentification <PoolId> [1..1] Text 228
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 228
     ReferenceOwner <RefOwnr> [0..1] ± 228
   Priority <Prty> [0..1] ± 229
   MessageOriginator <MsgOrgtr> [0..1] ± 229
   CreationDateTime <CreDtTm> [1..1] DateTime 229
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 229
   SupplementaryData <SplmtryData> [0..*] ± C23 229
10.4.4.1.5.11.1  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  218
{Or     Code <Cd> [1..1] CodeSet 219
Or}     Proprietary <Prtry> [1..1] ± 219
   QuantityBreakdown <QtyBrkdwn> [0..*]  219
     LotNumber <LotNb> [0..1] ± 219
     LotAmount <LotAmt> [0..1] ± 220
     LotQuantity <LotQty> [0..1] ± 220
     CashSubBalanceType <CshSubBalTp> [0..1] ± 220
10.4.4.1.5.11.1.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
218 March 2024
```

