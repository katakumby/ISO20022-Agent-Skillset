---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.4 OrderType <OrdrTp>"]
file_pages: [3057, 3058]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.4 OrderType <OrdrTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3057 to 3058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3057

```text
50.4.4.9.4  OrderType <OrdrTp>
Presence: [0..10]
Definition: Category of the investment fund order.
OrderType <OrdrTp> contains one of the following elements (see "FundOrderType4Choice" on
page 4740 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
50.4.4.9.5  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class related to the order.
Impacted by: C21 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3057 May 2026
```

## File page 3058

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3059
{Or     ISIN <ISIN> [1..1] IdentifierSet 3059
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3060
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3060
Or     RIC <RIC> [1..1] IdentifierSet 3060
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3060
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3060
Or     CTA <CTA> [1..1] IdentifierSet 3060
Or     QUICK <QUICK> [1..1] IdentifierSet 3060
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3061
Or     Dutch <Dtch> [1..1] IdentifierSet 3061
Or     Valoren <Vlrn> [1..1] IdentifierSet 3061
Or     Sicovam <SCVM> [1..1] IdentifierSet 3061
Or     Belgian <Belgn> [1..1] IdentifierSet 3061
Or     Common <Cmon> [1..1] IdentifierSet 3061
Or     DTI <DTI> [1..1] IdentifierSet 3061
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3061
       Identification <Id> [1..1] Text 3062
       IdentificationSource <IdSrc> [1..1] ± 3062
   Name <Nm> [0..1] Text 3062
   ShortName <ShrtNm> [0..1] Text 3062
   SupplementaryIdentification <SplmtryId> [0..1] Text 3062
   ClassType <ClssTp> [0..1] Text 3062
   SecuritiesForm <SctiesForm> [0..1] CodeSet 3063
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3063
   ProductGroup <PdctGrp> [0..1] Text 3063
   SeriesIdentification <SrsId> [0..1]  C34 3063
     SeriesDate <SrsDt> [0..1] ± 3064
     SeriesName <SrsNm> [0..1] Text 3064
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3058 May 2026
```

