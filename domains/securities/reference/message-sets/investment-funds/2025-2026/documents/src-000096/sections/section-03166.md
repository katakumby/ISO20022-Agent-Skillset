---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.10 AggregateBalanceInformation3", "66.1.5.10.11 ForeignExchangeDetails <FXDtls>"]
file_pages: [4396]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.10.11 ForeignExchangeDetails <FXDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4396 to 4396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4396

```text
PriceDetails <PricDtls> contains the following elements (see "PriceInformation2" on page 5118 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 5118
   ValueType <ValTp> [0..1] CodeSet 5118
{Or   Type <Tp> [1..1] CodeSet 5119
Or}   ExtendedType <XtndedTp> [1..1] Text 5120
   SourceOfPrice <SrcOfPric> [0..1]  5120
{Or     LocalMarketPlace <LclMktPlc> [1..1] IdentifierSet 5120
Or     NonLocalMarketPlace <NonLclMktPlc> [1..1] ± 5120
Or}     PlaceAsDSS <PlcAsDSS> [1..1] ± 5121
   QuotationDate <QtnDt> [0..1] ± 5121
   Yielded <Yldd> [0..1] Indicator 5121
Constraints
• ValueRule
If Type is not MRKT, then Value may not be expressed with UnknownIndicator.
66.1.5.10.11  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Currency exchange related to a securities order.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms6"
on page 4530 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C2 4531
   QuotedCurrency <QtdCcy> [1..1] CodeSet C2 4531
   ExchangeRate <XchgRate> [1..1] Rate 4531
   QuotationDate <QtnDt> [0..1] DateTime 4531
   QuotingInstitution <QtgInstn> [0..1] ± 4531
66.1.5.10.12  BalanceBreakdownDetails <BalBrkdwnDtls>
Presence: [0..*]
Definition: Net position of a segregated holding of a single security within the overall position held in a
securities account, eg, sub-balance per status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4396 May 2026
```

