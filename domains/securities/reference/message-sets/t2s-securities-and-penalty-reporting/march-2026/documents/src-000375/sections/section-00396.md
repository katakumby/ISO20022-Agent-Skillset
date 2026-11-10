---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.29 Transaction Type", "7.1.29.2 TradeTransactionCondition5Choice", "7.1.29.2.2 Proprietary <Prtry>"]
file_pages: [489]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.29.2.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 489 to 489.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 489

```text
CodeName Name Definition
MAPR MarketPrice Trade was executed at market price.
NEGO NegotiatedTrade Trade for which the price is not the one
quoted but an improved one, that is, the
negotiated price.
NMPR NonMarketPrice Trade was executed outside of normal
market conditions, for example, in the
case of an iceberg order.
BCPD DeliverCountryIncorporation Place of delivery, in country of
incorporation when unset (UK specific).
7.1.29.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.2 Message Datatypes
7.2.1 Amount
7.2.1.1  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 492
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 489 March 2026
```

