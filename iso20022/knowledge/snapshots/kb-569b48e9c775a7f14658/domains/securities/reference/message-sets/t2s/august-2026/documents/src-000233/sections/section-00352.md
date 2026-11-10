---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.1 CashAccount <CshAcct>"]
file_pages: [457]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.1 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 457 to 457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 457

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         PoolIdentification <PoolId> [1..1] Text 467
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 467
       ReferenceOwner <RefOwnr> [0..1] ± 467
   UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 467
     SettlementAmount <SttlmAmt> [1..1] ± 469
     SettlementDate <SttlmDt> [1..1] ± 469
     BalanceFrom <BalFr> [1..1]  469
       Type <Tp> [1..1]  469
{Or         Code <Cd> [1..1] CodeSet 470
Or}         Proprietary <Prtry> [1..1] ± 470
       QuantityBreakdown <QtyBrkdwn> [0..*]  470
         LotNumber <LotNb> [0..1] ± 470
         LotAmount <LotAmt> [0..1] ± 471
         LotQuantity <LotQty> [0..1] ± 471
         CashSubBalanceType <CshSubBalTp> [0..1] ± 471
     BalanceTo <BalTo> [1..1]  472
       Type <Tp> [1..1]  472
{Or         Code <Cd> [1..1] CodeSet 472
Or}         Proprietary <Prtry> [1..1] ± 472
       QuantityBreakdown <QtyBrkdwn> [0..*]  473
         LotNumber <LotNb> [0..1] ± 473
         LotAmount <LotAmt> [0..1] ± 473
         LotQuantity <LotQty> [0..1] ± 474
         CashSubBalanceType <CshSubBalTp> [0..1] ± 474
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 474
     Priority <Prty> [0..1] ± 474
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 475
19.4.4.1.5.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C17 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 457 August 2026
```

