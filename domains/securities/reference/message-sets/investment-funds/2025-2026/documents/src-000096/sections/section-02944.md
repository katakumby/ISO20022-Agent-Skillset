---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>", "56.4.3.1.2 OrderStatus <OrdrSts>", "56.4.3.1.2.2 Cancelled <Canc>"]
file_pages: [4130]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.1.2.2 Cancelled <Canc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4130 to 4130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4130

```text
CodeName Name Definition
IACO InvalidAgentConfirmation Order confirmation received from agent
is invalid.
56.4.3.1.2.2  Cancelled <Canc>
Presence: [1..1]
Definition: Status of all the orders in the order message is cancelled. This status is used for orders that
have been accepted or that have been entered in an order book but that can not be executed.
Impacted by: C3 "AdditionaInformationRule", C5 "CancelledElementRule"
Cancelled <Canc> contains the following elements (see "CancelledStatusReason16" on page 5200 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  5200
{Or     Code <Cd> [1..1] CodeSet 5200
Or     Proprietary <Prtry> [1..1] ± 5201
Or}     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5201
   AdditionalInformation <AddtlInf> [0..1] Text 5201
Constraints
• AdditionaInformationRule
The AdditionalInformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
• CancelledElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
56.4.3.1.2.3  ConditionallyAccepted <CondlyAccptd>
Presence: [1..1]
Definition: Status of all the orders in the order message is conditionally accepted.
ConditionallyAccepted <CondlyAccptd> contains one of the following elements (see
"ConditionallyAcceptedStatus3Choice" on page 5209 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5209
Or}   ReasonDetails <RsnDtls> [1..5]  5209
     Reason <Rsn> [1..1]  5209
{Or       Code <Cd> [1..1] CodeSet 5210
Or}       Proprietary <Prtry> [1..1] ± 5210
     AdditionalInformation <AddtlInf> [0..1] Text 5210
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4130 May 2026
```

