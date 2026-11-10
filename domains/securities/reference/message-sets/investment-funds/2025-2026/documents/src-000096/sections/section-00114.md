---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.4 FinancialInstrumentDetails <FinInstrmDtls>", "13.4.9.4.1 Identification <Id>"]
file_pages: [178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.4.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 178 to 178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 178

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SeriesName <SrsNm> [0..1] Text 183
Constraints
• FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
13.4.9.4.1  Identification <Id>
Presence: [1..10]
Definition: Identification of a security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 178
Or   SEDOL <SEDOL> [1..1] IdentifierSet 179
Or   CUSIP <CUSIP> [1..1] IdentifierSet 179
Or   RIC <RIC> [1..1] IdentifierSet 179
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 179
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 179
Or   CTA <CTA> [1..1] IdentifierSet 179
Or   QUICK <QUICK> [1..1] IdentifierSet 179
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 180
Or   Dutch <Dtch> [1..1] IdentifierSet 180
Or   Valoren <Vlrn> [1..1] IdentifierSet 180
Or   Sicovam <SCVM> [1..1] IdentifierSet 180
Or   Belgian <Belgn> [1..1] IdentifierSet 180
Or   Common <Cmon> [1..1] IdentifierSet 180
Or   DTI <DTI> [1..1] IdentifierSet 180
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  181
     Identification <Id> [1..1] Text 181
     IdentificationSource <IdSrc> [1..1] ± 181
13.4.9.4.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 178 May 2026
```

