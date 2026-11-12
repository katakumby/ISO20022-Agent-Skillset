---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.2 PaymentCard29", "66.1.31.2.2 Number <Nb>"]
file_pages: [5047]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.2.2 Number <Nb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5047 to 5047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5047

```text
CodeName Name Definition
CRDT CreditCard Card where the holder has been granted
a line of credit. The card enables the
holder to make purchases and withdraw
cash up to a pre-arranged ceiling.
DBIT DebitCard Card enabling the holder to have its
purchases directly charged to its
account. The card may also combine
other functions, for example, cash card
or cheque guaranteed card.
66.1.31.2.2  Number <Nb>
Presence: [1..1]
Definition: Number embossed on a card that links the card to the account owner and account servicer.
Datatype: "Max35Text" on page 5403
66.1.31.2.3  HolderName <HldrNm>
Presence: [1..1]
Definition: Party entitled by a card issuer to use a card.
Datatype: "Max35Text" on page 5403
66.1.31.2.4  StartDate <StartDt>
Presence: [0..1]
Definition: Year and month the card is available for use.
Datatype: "ISOYearMonth" on page 5406
66.1.31.2.5  ExpiryDate <XpryDt>
Presence: [1..1]
Definition: Year and month the card expires.
Datatype: "ISOYearMonth" on page 5406
66.1.31.2.6  CardIssuerName <CardIssrNm>
Presence: [0..1]
Definition: Party that issues a payment card, as expressed by a numeric identification of the card issuer
according to ISO/IEC 7812-1.
Datatype: "Max35Text" on page 5403
66.1.31.2.7  CardIssuerIdentification <CardIssrId>
Presence: [0..1]
Definition: Party that issues a payment card, as expressed by a numeric identification of the card issuer
according to ISO/IEC 7812-1.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5047 May 2026
```

