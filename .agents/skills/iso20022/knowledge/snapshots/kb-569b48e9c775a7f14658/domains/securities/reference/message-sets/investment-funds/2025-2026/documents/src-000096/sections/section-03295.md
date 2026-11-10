---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.21 Foreign Exchange", "66.1.21.3 ForeignExchangeTerms37"]
file_pages: [4532]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.21.3 ForeignExchangeTerms37

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4532 to 4532.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4532

```text
QuotingInstitution <QtgInstn> contains one of the following elements (see
"PartyIdentification2Choice" on page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.21.3  ForeignExchangeTerms37
Definition: Information needed to process a currency exchange or conversion.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ToAmount <ToAmt> [0..1] Amount C1, C13 4532
   FromAmount <FrAmt> [0..1] Amount C1, C13 4532
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4533
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4533
   ExchangeRate <XchgRate> [1..1] Rate 4534
   QuotationDate <QtnDt> [0..1] DateTime 4534
   QuotingInstitution <QtgInstn> [0..1] ± 4534
66.1.21.3.1  ToAmount <ToAmt>
Presence: [0..1]
Definition: Cash amount resulting from a foreign exchange trade.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.21.3.2  FromAmount <FrAmt>
Presence: [0..1]
Definition: Cash amount for which a foreign exchange is required.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4532 May 2026
```

