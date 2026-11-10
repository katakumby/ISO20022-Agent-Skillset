---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.5 Movement <Mvmnt>", "17.4.4.1.5.11 MovementDetails <MvmntDtls>", "17.4.4.1.5.11.1 BalanceFrom <BalFr>"]
file_pages: [409]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.5.11.1 BalanceFrom <BalFr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 409 to 409.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 409

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 418
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 418
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 419
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 419
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 419
Or       PoolIdentification <PoolId> [1..1] Text 419
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 419
     ReferenceOwner <RefOwnr> [0..1] ± 419
   Priority <Prty> [0..1] ± 420
   MessageOriginator <MsgOrgtr> [0..1] ± 420
   CreationDateTime <CreDtTm> [1..1] DateTime 420
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 420
   SupplementaryData <SplmtryData> [0..*] ± C23 420
17.4.4.1.5.11.1  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
BalanceFrom <BalFr> contains the following CashSubBalanceTypeAndQuantityBreakdown3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  409
{Or     Code <Cd> [1..1] CodeSet 410
Or}     Proprietary <Prtry> [1..1] ± 410
   QuantityBreakdown <QtyBrkdwn> [0..*]  410
     LotNumber <LotNb> [0..1] ± 410
     LotAmount <LotAmt> [0..1] ± 411
     LotQuantity <LotQty> [0..1] ± 411
     CashSubBalanceType <CshSubBalTp> [0..1] ± 411
17.4.4.1.5.11.1.1  Type <Tp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 409 August 2026
```

