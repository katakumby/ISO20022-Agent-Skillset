---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 camt.068.001.02 IntraBalanceMovementConfirmationV02", "4.4 Message Building Blocks", "4.4.6 IntraBalance <IntraBal>", "4.4.6.1 SettledAmount <SttldAmt>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 4.4.6.1 SettledAmount <SttldAmt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
IntraBalance <IntraBal> contains the following IntraBalance6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettledAmount <SttldAmt> [0..1] ± 58
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 59
   RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 59
   SettlementDate <SttlmDt> [1..1] ± 59
   BalanceFrom <BalFr> [1..1]  59
     Type <Tp> [1..1]  60
{Or       Code <Cd> [1..1] CodeSet 60
Or}       Proprietary <Prtry> [1..1] ± 60
     QuantityBreakdown <QtyBrkdwn> [0..*]  61
       LotNumber <LotNb> [0..1] ± 61
       LotAmount <LotAmt> [0..1] ± 61
       LotQuantity <LotQty> [0..1] ± 61
       CashSubBalanceType <CshSubBalTp> [0..1] ± 62
   BalanceTo <BalTo> [1..1]  62
     Type <Tp> [1..1]  62
{Or       Code <Cd> [1..1] CodeSet 63
Or}       Proprietary <Prtry> [1..1] ± 63
     QuantityBreakdown <QtyBrkdwn> [0..*]  63
       LotNumber <LotNb> [0..1] ± 63
       LotAmount <LotAmt> [0..1] ± 64
       LotQuantity <LotQty> [0..1] ± 64
       CashSubBalanceType <CshSubBalTp> [0..1] ± 64
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 65
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 65
4.4.6.1  SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Amount of money effectively settled and which will be credited to/debited from the account
owner's cash account. It may differ from the instructed settlement amount based on market tolerance
level.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
58 March 2024
```

