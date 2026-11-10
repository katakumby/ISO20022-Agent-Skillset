---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.4 Message Building Blocks", "9.4.6 IntraBalance <IntraBal>", "9.4.6.1 SettledAmount <SttldAmt>"]
file_pages: [141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 9.4.6.1 SettledAmount <SttldAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 141 to 141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
IntraBalance <IntraBal> contains the following IntraBalance6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettledAmount <SttldAmt> [0..1] ± 141
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 142
   RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 142
   SettlementDate <SttlmDt> [1..1] ± 142
   BalanceFrom <BalFr> [1..1]  142
     Type <Tp> [1..1]  143
{Or       Code <Cd> [1..1] CodeSet 143
Or}       Proprietary <Prtry> [1..1] ± 143
     QuantityBreakdown <QtyBrkdwn> [0..*]  144
       LotNumber <LotNb> [0..1] ± 144
       LotAmount <LotAmt> [0..1] ± 144
       LotQuantity <LotQty> [0..1] ± 144
       CashSubBalanceType <CshSubBalTp> [0..1] ± 145
   BalanceTo <BalTo> [1..1]  145
     Type <Tp> [1..1]  145
{Or       Code <Cd> [1..1] CodeSet 146
Or}       Proprietary <Prtry> [1..1] ± 146
     QuantityBreakdown <QtyBrkdwn> [0..*]  146
       LotNumber <LotNb> [0..1] ± 146
       LotAmount <LotAmt> [0..1] ± 147
       LotQuantity <LotQty> [0..1] ± 147
       CashSubBalanceType <CshSubBalTp> [0..1] ± 147
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 148
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 148
9.4.6.1  SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Amount of money effectively settled and which will be credited to/debited from the account
owner's cash account. It may differ from the instructed settlement amount based on market tolerance
level.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 141 August 2026
```

