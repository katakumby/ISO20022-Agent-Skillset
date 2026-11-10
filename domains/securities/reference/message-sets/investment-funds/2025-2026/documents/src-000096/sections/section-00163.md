---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.4 FinancialInstrumentDetails <FinInstrmDtls>", "14.4.10.1.4.1 Identification <Id>"]
file_pages: [247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.4.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 247 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SeriesName <SrsNm> [0..1] Text 252
Constraints
• FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
14.4.10.1.4.1  Identification <Id>
Presence: [1..10]
Definition: Identification of a security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 247
Or   SEDOL <SEDOL> [1..1] IdentifierSet 248
Or   CUSIP <CUSIP> [1..1] IdentifierSet 248
Or   RIC <RIC> [1..1] IdentifierSet 248
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 248
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 248
Or   CTA <CTA> [1..1] IdentifierSet 248
Or   QUICK <QUICK> [1..1] IdentifierSet 248
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 249
Or   Dutch <Dtch> [1..1] IdentifierSet 249
Or   Valoren <Vlrn> [1..1] IdentifierSet 249
Or   Sicovam <SCVM> [1..1] IdentifierSet 249
Or   Belgian <Belgn> [1..1] IdentifierSet 249
Or   Common <Cmon> [1..1] IdentifierSet 249
Or   DTI <DTI> [1..1] IdentifierSet 249
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  250
     Identification <Id> [1..1] Text 250
     IdentificationSource <IdSrc> [1..1] ± 250
14.4.10.1.4.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 247 May 2026
```

