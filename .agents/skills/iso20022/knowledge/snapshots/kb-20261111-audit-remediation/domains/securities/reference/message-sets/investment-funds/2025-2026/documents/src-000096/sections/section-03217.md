---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.4 ChargePaymentMethod1Choice"]
file_pages: [4453]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.4 ChargePaymentMethod1Choice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4453 to 4453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4453

```text
66.1.8.4  ChargePaymentMethod1Choice
Definition: Choice of formats for the specification of the charge payment method.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4453
Or}   Proprietary <Prtry> [1..1] ± 4453
66.1.8.4.1  Code <Cd>
Presence: [1..1]
Definition: Charge payment method expressed as a code.
Datatype: "ChargePaymentMethod1Code" on page 5282
CodeName Name Definition
CASH Cash Payment is with cash.
UNIT Unit Units are redeemed to cover payment.
66.1.8.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Charge payment method expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.9 Cheque
66.1.9.1  Cheque4
Definition: Set of characteristics related to a cheque instruction, such as cheque type or cheque
number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayeeIdentification <PyeeId> [1..1] ± 4453
66.1.9.1.1  PayeeIdentification <PyeeId>
Presence: [1..1]
Definition: Party to which a cheque is made payable.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4453 May 2026
```

