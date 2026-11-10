---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.6 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [3305, 3306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.6 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3305 to 3306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3305

```text
OrderType <OrdrTp> contains one of the following elements (see "FundOrderType4Choice" on
page 4740 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
52.4.5.10.6  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the investment fund order execution is related.
Impacted by: C23 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3305 May 2026
```

## File page 3306

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3307
{Or     ISIN <ISIN> [1..1] IdentifierSet 3307
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3308
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3308
Or     RIC <RIC> [1..1] IdentifierSet 3308
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3308
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3308
Or     CTA <CTA> [1..1] IdentifierSet 3308
Or     QUICK <QUICK> [1..1] IdentifierSet 3308
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3309
Or     Dutch <Dtch> [1..1] IdentifierSet 3309
Or     Valoren <Vlrn> [1..1] IdentifierSet 3309
Or     Sicovam <SCVM> [1..1] IdentifierSet 3309
Or     Belgian <Belgn> [1..1] IdentifierSet 3309
Or     Common <Cmon> [1..1] IdentifierSet 3309
Or     DTI <DTI> [1..1] IdentifierSet 3309
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3309
       Identification <Id> [1..1] Text 3310
       IdentificationSource <IdSrc> [1..1] ± 3310
   Name <Nm> [0..1] Text 3310
   ShortName <ShrtNm> [0..1] Text 3310
   SupplementaryIdentification <SplmtryId> [0..1] Text 3310
   ClassType <ClssTp> [0..1] Text 3310
   SecuritiesForm <SctiesForm> [0..1] CodeSet 3311
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3311
   ProductGroup <PdctGrp> [0..1] Text 3311
   SeriesIdentification <SrsId> [0..1]  C39 3311
     SeriesDate <SrsDt> [0..1] ± 3312
     SeriesName <SrsNm> [0..1] Text 3312
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3306 May 2026
```

