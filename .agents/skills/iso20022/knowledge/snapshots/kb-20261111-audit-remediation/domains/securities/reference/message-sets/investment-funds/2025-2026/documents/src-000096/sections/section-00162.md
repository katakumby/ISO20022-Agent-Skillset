---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.1 Identification <Id>"]
file_pages: [245, 246]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 245 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 245

```text
If SuspendedIndicator is "false" or "0" (No), and if FinancialInstrumentDetails /DualFundIndicator is
"false" or "0" (No), then PriceDetails must be present at least once.
If SuspendedIndicator is "false" or "0" (No), and if FinancialInstrumentDetails /DualFundIndicator is
"true" or "1" (Yes), then PriceDetails must be present two or more times and PriceDetails/Type must
be present with the values "BIDE" and "OFFR".
14.4.10.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique technical identifier for an instance of a price valuation within a price report, as
assigned by the issuer of the report.
Datatype: "Max35Text" on page 5403
14.4.10.1.2  ValuationDateTime <ValtnDtTm>
Presence: [0..1]
Definition: Date and time of the price valuation for the investment fund/fund class.
ValuationDateTime <ValtnDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
14.4.10.1.3  NAVDateTime <NAVDtTm>
Presence: [1..1]
Definition: Date and time at which a price is applied, according to the terms stated in the prospectus.
The NAV date is also known as the trade date. The NAV date becomes the trade date in an order.
NAVDateTime <NAVDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
14.4.10.1.4  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class for which the net asset value is calculated.
Impacted by: C17 "FinancialInstrumentIdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 245 May 2026
```

## File page 246

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument106
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..10]  247
{Or     ISIN <ISIN> [1..1] IdentifierSet 247
Or     SEDOL <SEDOL> [1..1] IdentifierSet 248
Or     CUSIP <CUSIP> [1..1] IdentifierSet 248
Or     RIC <RIC> [1..1] IdentifierSet 248
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 248
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 248
Or     CTA <CTA> [1..1] IdentifierSet 248
Or     QUICK <QUICK> [1..1] IdentifierSet 248
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 249
Or     Dutch <Dtch> [1..1] IdentifierSet 249
Or     Valoren <Vlrn> [1..1] IdentifierSet 249
Or     Sicovam <SCVM> [1..1] IdentifierSet 249
Or     Belgian <Belgn> [1..1] IdentifierSet 249
Or     Common <Cmon> [1..1] IdentifierSet 249
Or     DTI <DTI> [1..1] IdentifierSet 249
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  250
       Identification <Id> [1..1] Text 250
       IdentificationSource <IdSrc> [1..1] ± 250
   Name <Nm> [0..1] Text 250
   ShortName <ShrtNm> [0..1] Text 250
   SupplementaryIdentification <SplmtryId> [0..1] Text 250
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 251
   ClassType <ClssTp> [0..1] Text 251
   SecuritiesForm <SctiesForm> [0..1] CodeSet 251
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 251
   DualFundIndicator <DualFndInd> [1..1] Indicator 252
   ProductGroup <PdctGrp> [0..1] Text 252
   SeriesIdentification <SrsId> [0..1]  C21 252
     SeriesDate <SrsDt> [0..1] ± 252
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 246 May 2026
```

