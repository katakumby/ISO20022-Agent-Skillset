---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>", "12.4.4.1.5 Modification <Mod>", "12.4.4.1.5.1 CashAccount <CshAcct>"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1.5.1 CashAccount <CshAcct>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         PoolIdentification <PoolId> [1..1] Text 276
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 276
       ReferenceOwner <RefOwnr> [0..1] ± 276
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 276
     SettlementAmount <SttlmAmt> [1..1] ± 278
     SettlementDate <SttlmDt> [1..1] ± 278
     BalanceFrom <BalFr> [1..1]  278
       Type <Tp> [1..1]  278
{Or         Code <Cd> [1..1] CodeSet 279
Or}         Proprietary <Prtry> [1..1] ± 279
       QuantityBreakdown <QtyBrkdwn> [0..*]  279
         LotNumber <LotNb> [0..1] ± 279
         LotAmount <LotAmt> [0..1] ± 280
         LotQuantity <LotQty> [0..1] ± 280
         CashSubBalanceType <CshSubBalTp> [0..1] ± 280
     BalanceTo <BalTo> [1..1]  281
       Type <Tp> [1..1]  281
{Or         Code <Cd> [1..1] CodeSet 281
Or}         Proprietary <Prtry> [1..1] ± 281
       QuantityBreakdown <QtyBrkdwn> [0..*]  282
         LotNumber <LotNb> [0..1] ± 282
         LotAmount <LotAmt> [0..1] ± 282
         LotQuantity <LotQty> [0..1] ± 283
         CashSubBalanceType <CshSubBalTp> [0..1] ± 283
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 283
     Priority <Prty> [0..1] ± 283
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 284
12.4.4.1.5.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C17 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
266 March 2024
```

