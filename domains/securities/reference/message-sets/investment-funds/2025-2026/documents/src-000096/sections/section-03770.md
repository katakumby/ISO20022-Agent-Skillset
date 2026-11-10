---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.4 PaymentInstrument16", "66.1.31.4.2 InstrumentType <InstrmTp>"]
file_pages: [5057]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.4.2 InstrumentType <InstrmTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5057 to 5057.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5057

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.31.4.2  InstrumentType <InstrmTp>
Presence: [1..1]
Definition: Payment instrument for the order type.
InstrumentType <InstrmTp> contains one of the following FundPaymentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5057
Or}   Proprietary <Prtry> [1..1] ± 5057
66.1.31.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of payment instrument expressed as a code.
Datatype: "FundPaymentType1Code" on page 5307
CodeName Name Definition
DRAF BankersDraft Payment instrument is a bankers draft.
CACC CashAccount Payment instrument is a cash account.
CHEQ Cheque Payment instrument is a cheque.
CRDT CreditTransfer Payment instrument is a credit transfer.
DDEB DirectDebit Payment instrument is a direct debit.
CARD PaymentCard Payment instrument is a payment card.
66.1.31.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of payment instrument expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5057 May 2026
```

