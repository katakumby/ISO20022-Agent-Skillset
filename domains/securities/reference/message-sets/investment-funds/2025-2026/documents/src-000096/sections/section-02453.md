---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "52.4.5.12.1 PaymentInstrument <PmtInstrm>", "52.4.5.12.1.1 PaymentCardDetails <PmtCardDtls>", "52.4.5.12.1.1.1 Type <Tp>"]
file_pages: [3438]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.12.1.1.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3438 to 3438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3438

```text
52.4.5.12.1.1.1  Type <Tp>
Presence: [1..1]
Definition: Type of card, for example, credit card.
Datatype: "CardType1Code" on page 5281
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
52.4.5.12.1.1.2  Number <Nb>
Presence: [1..1]
Definition: Number embossed on a card that links the card to the account owner and account servicer.
Datatype: "Max35Text" on page 5403
52.4.5.12.1.1.3  HolderName <HldrNm>
Presence: [1..1]
Definition: Party entitled by a card issuer to use a card.
Datatype: "Max35Text" on page 5403
52.4.5.12.1.1.4  StartDate <StartDt>
Presence: [0..1]
Definition: Year and month the card is available for use.
Datatype: "ISOYearMonth" on page 5406
52.4.5.12.1.1.5  ExpiryDate <XpryDt>
Presence: [1..1]
Definition: Year and month the card expires.
Datatype: "ISOYearMonth" on page 5406
52.4.5.12.1.1.6  CardIssuerName <CardIssrNm>
Presence: [0..1]
Definition: Party that issues a payment card, as expressed by a numeric identification of the card issuer
according to ISO/IEC 7812-1.
Datatype: "Max35Text" on page 5403
52.4.5.12.1.1.7  CardIssuerIdentification <CardIssrId>
Presence: [0..1]
Definition: Party that issues a payment card, as expressed by a numeric identification of the card issuer
according to ISO/IEC 7812-1.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3438 May 2026
```

