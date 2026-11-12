---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.3 PaymentInstrument17", "66.1.31.3.5 DividendPaymentInstrument <DvddPmtInstrm>", "66.1.31.3.5.2 BankersDraftDetails <BkrsDrftDtls>"]
file_pages: [5053]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.3.5.2 BankersDraftDetails <BkrsDrftDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5053 to 5053.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5053

```text
ChequeDetails <ChqDtls> contains the following elements (see "Cheque4" on page 4453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayeeIdentification <PyeeId> [1..1] ± 4453
66.1.31.3.5.2  BankersDraftDetails <BkrsDrftDtls>
Presence: [1..1]
Definition: Settlement instructions for a payment by draft.
BankersDraftDetails <BkrsDrftDtls> contains the following elements (see "Cheque4" on page 4453
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayeeIdentification <PyeeId> [1..1] ± 4453
66.1.31.3.6  SavingsPlanPaymentInstrument <SvgsPlanPmtInstrm>
Presence: [0..1]
Definition: Instrument that has or represents monetary value and is used to process a payment
instruction for a savings plan payment.
SavingsPlanPaymentInstrument <SvgsPlanPmtInstrm> contains one of the following
PaymentInstrument24Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1] ± 5053
Or   DirectDebitDetails <DrctDbtDtls> [1..1] ± 5054
Or   Cheque <Chq> [1..1] Indicator 5054
Or}   BankersDraft <BkrsDrft> [1..1] Indicator 5055
66.1.31.3.6.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Settlement instructions for a payment by card.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5053 May 2026
```

