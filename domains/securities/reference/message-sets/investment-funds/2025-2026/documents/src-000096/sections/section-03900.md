---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.18 CancellationReason31Choice", "66.1.45.18.2 Proprietary <Prtry>"]
file_pages: [5191]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.18.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5191 to 5191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5191

```text
CodeName Name Definition
SETS IncorrectSettlementMethod Confirmation is cancelled because the
settlement method is incorrect.
DDEA IncorrectTradeDate Confirmation is cancelled because the
trade date is incorrect.
REFE InvalidReference Confirmation contains an invalid
business reference.
66.1.45.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Confirmation cancellation reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.45.19  ConfirmationRejectedStatus2
Definition: Rejection of a confirmation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  5191
{Or     Code <Cd> [1..1] CodeSet 5192
Or}     Proprietary <Prtry> [1..1] ± 5194
   AdditionalInformation <AddtlInf> [0..1] Text 5194
Constraints
• ReasonElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
66.1.45.19.1  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following ConfirmationRejectedReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5192
Or}   Proprietary <Prtry> [1..1] ± 5194
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5191 May 2026
```

