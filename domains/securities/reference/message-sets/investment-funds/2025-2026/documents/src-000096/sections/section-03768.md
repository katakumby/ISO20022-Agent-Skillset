---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.3 PaymentInstrument17", "66.1.31.3.6 SavingsPlanPaymentInstrument <SvgsPlanPmtInstrm>", "66.1.31.3.6.4 BankersDraft <BkrsDrft>"]
file_pages: [5055]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.3.6.4 BankersDraft <BkrsDrft>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5055 to 5055.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5055

```text
• Meaning When True: Yes
• Meaning When False: No
66.1.31.3.6.4  BankersDraft <BkrsDrft>
Presence: [1..1]
Definition: Indicates whether the payment is done via draft.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.31.3.7  InterestPaymentInstrument <IntrstPmtInstrm>
Presence: [0..1]
Definition: Instrument that has or represents monetary value and is used to process a payment
instruction for an interest payment.
InterestPaymentInstrument <IntrstPmtInstrm> contains one of the following
PaymentInstrument19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ChequeDetails <ChqDtls> [1..1] ± 5055
Or}   BankersDraftDetails <BkrsDrftDtls> [1..1] ± 5055
66.1.31.3.7.1  ChequeDetails <ChqDtls>
Presence: [1..1]
Definition: Settlement instructions for a payment by cheque.
ChequeDetails <ChqDtls> contains the following elements (see "Cheque4" on page 4453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayeeIdentification <PyeeId> [1..1] ± 4453
66.1.31.3.7.2  BankersDraftDetails <BkrsDrftDtls>
Presence: [1..1]
Definition: Settlement instructions for a payment by draft.
BankersDraftDetails <BkrsDrftDtls> contains the following elements (see "Cheque4" on page 4453
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayeeIdentification <PyeeId> [1..1] ± 4453
66.1.31.4  PaymentInstrument16
Definition: Payment instrument for a type of order.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5055 May 2026
```

