---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.13 Financial Instrument Quantity", "7.1.13.2 Quantity6Choice", "7.1.13.2.2 OriginalAndCurrentFace <OrgnlAndCurFace>"]
file_pages: [343]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.13.2.2 OriginalAndCurrentFace <OrgnlAndCurFace>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 343 to 343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 343

```text
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
7.1.13.2.2  OriginalAndCurrentFace <OrgnlAndCurFace>
Presence: [1..1]
Definition: Original and current value of an asset-back instrument.
OriginalAndCurrentFace <OrgnlAndCurFace> contains the following elements (see
"OriginalAndCurrentQuantities1" on page 454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 454
   AmortisedValue <AmtsdVal> [1..1] Amount 454
7.1.14 Foreign Exchange
7.1.14.1  ForeignExchangeTerms34
Definition: Information needed to process a currency exchange or conversion.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C2 343
   QuotedCurrency <QtdCcy> [1..1] CodeSet C2 344
   ExchangeRate <XchgRate> [1..1] Rate 344
   QuotationDate <QtnDt> [0..1] DateTime 344
   QuotingInstitution <QtgInstn> [0..1] ± 344
7.1.14.1.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 492
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 343 March 2026
```

