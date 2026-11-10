---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.5 PriceInformation20", "7.1.22.5.3 ValueType <ValTp>"]
file_pages: [448]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.5.3 ValueType <ValTp>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 448 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 448

```text
Value <Val> contains one of the following elements (see "PriceRateOrAmountOrUnknown2Choice" on
page 449 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 449
Or   Amount <Amt> [1..1] Amount C2 449
Or}   UnknownIndicator <UknwnInd> [1..1] Indicator 449
7.1.22.5.3  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
ValueType <ValTp> contains one of the following elements (see "YieldedOrValueType1Choice" on
page 385 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 385
Or}   ValueType <ValTp> [1..1] CodeSet 385
7.1.22.5.4  SourceOfPrice <SrcOfPric>
Presence: [0..1]
Definition: Place from which the price was obtained.
SourceOfPrice <SrcOfPric> contains the following elements (see "MarketIdentification89" on
page 354 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 354
   Type <Tp> [1..1]  355
{Or     Code <Cd> [1..1] CodeSet 355
Or}     Proprietary <Prtry> [1..1] ± 355
7.1.22.5.5  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date on which the price is obtained. With an investment fund, this is as stated in the
prospectus.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 448 March 2026
```

