---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.3 StatusAndReason <StsAndRsn>", "72.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>"]
file_pages: [2519]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2519 to 2519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2519

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus32Choice" on page 3118 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  3119
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3120
Or}     Reason <Rsn> [1..*]  3120
       Code <Cd> [1..1]  3120
{Or         Code <Cd> [1..1] CodeSet 3120
Or}         Proprietary <Prtry> [1..1] ± 3123
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3124
Or   Failing <Flng> [1..1]  3124
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3124
Or}     Reason <Rsn> [1..*]  3124
       Code <Cd> [1..1]  3125
{Or         Code <Cd> [1..1] CodeSet 3125
Or}         Proprietary <Prtry> [1..1] ± 3128
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3129
Or}   Proprietary <Prtry> [1..1] ± 3129
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
72.4.3.4.3.4  InstructionProcessingStatus <InstrPrcgSts>
Presence: [0..1]
Definition: Provides the status of an instruction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2519 August 2026
```

