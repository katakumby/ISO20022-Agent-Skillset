---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.5 Movement <Mvmnt>", "17.4.4.1.5.11 MovementDetails <MvmntDtls>"]
file_pages: [407, 408]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.5.11 MovementDetails <MvmntDtls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 407 to 408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 407

```text
17.4.4.1.5.11  MovementDetails <MvmntDtls>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 407 August 2026
```

## File page 408

```text
MovementDetails <MvmntDtls> contains the following IntraBalanceMovement6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [1..1]  409
     Type <Tp> [1..1]  409
{Or       Code <Cd> [1..1] CodeSet 410
Or}       Proprietary <Prtry> [1..1] ± 410
     QuantityBreakdown <QtyBrkdwn> [0..*]  410
       LotNumber <LotNb> [0..1] ± 410
       LotAmount <LotAmt> [0..1] ± 411
       LotQuantity <LotQty> [0..1] ± 411
       CashSubBalanceType <CshSubBalTp> [0..1] ± 411
   BalanceTo <BalTo> [1..1]  412
     Type <Tp> [1..1]  412
{Or       Code <Cd> [1..1] CodeSet 412
Or}       Proprietary <Prtry> [1..1] ± 412
     QuantityBreakdown <QtyBrkdwn> [0..*]  413
       LotNumber <LotNb> [0..1] ± 413
       LotAmount <LotAmt> [0..1] ± 413
       LotQuantity <LotQty> [0..1] ± 414
       CashSubBalanceType <CshSubBalTp> [0..1] ± 414
   SettlementAmount <SttlmAmt> [1..1] ± 414
   SettledAmount <SttldAmt> [0..1] ± 414
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 415
   RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 415
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 415
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 415
   StatusDate <StsDt> [0..1] DateTime 416
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 416
   Linkages <Lnkgs> [0..*]  416
     ProcessingPosition <PrcgPos> [0..1] ± C24 417
     MessageNumber <MsgNb> [0..1] ± C21 417
     Reference <Ref> [1..1]  418
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 408 August 2026
```

