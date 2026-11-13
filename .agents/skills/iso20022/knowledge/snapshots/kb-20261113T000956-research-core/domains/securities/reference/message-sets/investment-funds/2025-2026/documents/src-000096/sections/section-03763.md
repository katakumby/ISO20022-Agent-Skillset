---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.3 PaymentInstrument17", "66.1.31.3.2 DividendPercentage <DvddPctg>"]
file_pages: [5050]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.3.2 DividendPercentage <DvddPctg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5050 to 5050.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5050

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.31.3.2  DividendPercentage <DvddPctg>
Presence: [0..1]
Definition: Percentage of the dividend payment not to be reinvested, that is, to be paid in cash.
Datatype: "PercentageBoundedRate" on page 5401
66.1.31.3.3  SubscriptionPaymentInstrument <SbcptPmtInstrm>
Presence: [0..1]
Definition: Instrument that has or represents monetary value and is used to process a payment
instruction for a subscription payment.
SubscriptionPaymentInstrument <SbcptPmtInstrm> contains one of the following
PaymentInstrument24Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1] ± 5050
Or   DirectDebitDetails <DrctDbtDtls> [1..1] ± 5050
Or   Cheque <Chq> [1..1] Indicator 5051
Or}   BankersDraft <BkrsDrft> [1..1] Indicator 5051
66.1.31.3.3.1  PaymentCardDetails <PmtCardDtls>
Presence: [1..1]
Definition: Settlement instructions for a payment by card.
PaymentCardDetails <PmtCardDtls> contains the following elements (see "PaymentCard29" on
page 5046 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 5046
   Number <Nb> [1..1] Text 5047
   HolderName <HldrNm> [1..1] Text 5047
   StartDate <StartDt> [0..1] YearMonth 5047
   ExpiryDate <XpryDt> [1..1] YearMonth 5047
   CardIssuerName <CardIssrNm> [0..1] Text 5047
   CardIssuerIdentification <CardIssrId> [0..1] ± 5047
   SecurityCode <SctyCd> [0..1] Text 5048
   SequenceNumber <SeqNb> [0..1] Text 5048
66.1.31.3.3.2  DirectDebitDetails <DrctDbtDtls>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5050 May 2026
```

