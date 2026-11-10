---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.3 StatusAndReason <StsAndRsn>", "4.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.3.4.3 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [108]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.3.4.3 AcknowledgedAccepted <AckdAccptd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 108 to 108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 108

```text
CancellationRequested <CxlReqd> contains the following elements (see "ProprietaryReason4" on
page 470 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 470
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 470
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
4.4.3.3.4.3  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 481
Or}   Reason <Rsn> [1..*] ± 482
4.4.3.3.4.4  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus24Choice" on
page 471 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 471
Or}   Reason <Rsn> [1..*]  471
     Code <Cd> [1..1]  471
{Or       Code <Cd> [1..1] CodeSet 472
Or}       Proprietary <Prtry> [1..1] ± 472
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 472
4.4.3.3.4.5  Generated <Gnrtd>
Presence: [1..1]
Definition: Transaction was created by the account servicer or a third party. It was not instructed directly
by the account owner.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 108 March 2026
```

