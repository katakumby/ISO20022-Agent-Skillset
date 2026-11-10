---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.3 StatusAndReason <StsAndRsn>", "72.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>", "72.4.3.4.3.4.3 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [2524]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.3.4.3 AcknowledgedAccepted <AckdAccptd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2524 to 2524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2524

```text
CancellationRequested <CxlReqd> contains the following elements (see "ProprietaryReason4" on
page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
72.4.3.4.3.4.3  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 3172 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3173
Or}   Reason <Rsn> [1..*] ± 3173
72.4.3.4.3.4.4  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus24Choice" on
page 3149 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3150
Or}   Reason <Rsn> [1..*]  3150
     Code <Cd> [1..1]  3150
{Or       Code <Cd> [1..1] CodeSet 3150
Or}       Proprietary <Prtry> [1..1] ± 3151
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3151
72.4.3.4.3.4.5  Generated <Gnrtd>
Presence: [1..1]
Definition: Transaction was created by the account servicer or a third party. It was not instructed directly
by the account owner.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2524 August 2026
```

