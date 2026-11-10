---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.2 ClientReference <ClntRef>"]
file_pages: [2363, 2364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.2 ClientReference <ClntRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2363 to 2364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2363

```text
46.4.5.10.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
46.4.5.10.3  DealReference <DealRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
46.4.5.10.4  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
46.4.5.10.5  OrderType <OrdrTp>
Presence: [0..10]
Definition: Category of the investment fund order.
OrderType <OrdrTp> contains one of the following elements (see "FundOrderType4Choice" on
page 4740 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
46.4.5.10.6  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the investment fund order execution is related.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2363 May 2026
```

## File page 2364

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2365
{Or     ISIN <ISIN> [1..1] IdentifierSet 2365
Or     SEDOL <SEDOL> [1..1] IdentifierSet 2366
Or     CUSIP <CUSIP> [1..1] IdentifierSet 2366
Or     RIC <RIC> [1..1] IdentifierSet 2366
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 2366
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 2366
Or     CTA <CTA> [1..1] IdentifierSet 2366
Or     QUICK <QUICK> [1..1] IdentifierSet 2366
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 2367
Or     Dutch <Dtch> [1..1] IdentifierSet 2367
Or     Valoren <Vlrn> [1..1] IdentifierSet 2367
Or     Sicovam <SCVM> [1..1] IdentifierSet 2367
Or     Belgian <Belgn> [1..1] IdentifierSet 2367
Or     Common <Cmon> [1..1] IdentifierSet 2367
Or     DTI <DTI> [1..1] IdentifierSet 2367
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  2367
       Identification <Id> [1..1] Text 2368
       IdentificationSource <IdSrc> [1..1] ± 2368
   Name <Nm> [0..1] Text 2368
   ShortName <ShrtNm> [0..1] Text 2368
   SupplementaryIdentification <SplmtryId> [0..1] Text 2368
   ClassType <ClssTp> [0..1] Text 2368
   SecuritiesForm <SctiesForm> [0..1] CodeSet 2369
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2369
   ProductGroup <PdctGrp> [0..1] Text 2369
   SeriesIdentification <SrsId> [0..1]  C38 2369
     SeriesDate <SrsDt> [0..1] ± 2370
     SeriesName <SrsNm> [0..1] Text 2370
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2364 May 2026
```

