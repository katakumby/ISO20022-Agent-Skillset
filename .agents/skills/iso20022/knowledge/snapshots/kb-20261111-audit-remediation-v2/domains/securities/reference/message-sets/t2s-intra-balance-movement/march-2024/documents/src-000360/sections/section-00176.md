---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.5 Movement <Mvmnt>", "10.4.4.1.5.11 MovementDetails <MvmntDtls>"]
file_pages: [216, 217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.5.11 MovementDetails <MvmntDtls>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 216 to 217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
10.4.4.1.5.11  MovementDetails <MvmntDtls>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
216 March 2024
```

## File page 217

```text
MovementDetails <MvmntDtls> contains the following IntraBalanceMovement6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [1..1]  218
     Type <Tp> [1..1]  218
{Or       Code <Cd> [1..1] CodeSet 219
Or}       Proprietary <Prtry> [1..1] ± 219
     QuantityBreakdown <QtyBrkdwn> [0..*]  219
       LotNumber <LotNb> [0..1] ± 219
       LotAmount <LotAmt> [0..1] ± 220
       LotQuantity <LotQty> [0..1] ± 220
       CashSubBalanceType <CshSubBalTp> [0..1] ± 220
   BalanceTo <BalTo> [1..1]  221
     Type <Tp> [1..1]  221
{Or       Code <Cd> [1..1] CodeSet 221
Or}       Proprietary <Prtry> [1..1] ± 221
     QuantityBreakdown <QtyBrkdwn> [0..*]  222
       LotNumber <LotNb> [0..1] ± 222
       LotAmount <LotAmt> [0..1] ± 222
       LotQuantity <LotQty> [0..1] ± 223
       CashSubBalanceType <CshSubBalTp> [0..1] ± 223
   SettlementAmount <SttlmAmt> [1..1] ± 223
   SettledAmount <SttldAmt> [0..1] ± 223
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 224
   RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 224
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 224
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 224
   StatusDate <StsDt> [0..1] DateTime 225
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 225
   Linkages <Lnkgs> [0..*]  225
     ProcessingPosition <PrcgPos> [0..1] ± C24 226
     MessageNumber <MsgNb> [0..1] ± C21 226
     Reference <Ref> [1..1]  227
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
217 March 2024
```

