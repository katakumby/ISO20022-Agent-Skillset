---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.1 OrderReference <OrdrRef>"]
file_pages: [2149, 2150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.1 OrderReference <OrdrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2149 to 2150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2149

```text
 And    /SettlementAmount is present
Following Must be True
    /RequestedSettlementCurrency Must be equal to /SettlementAmount/
attribute::Currency
44.4.4.9.1  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
44.4.4.9.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
44.4.4.9.3  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
44.4.4.9.4  OrderType <OrdrTp>
Presence: [0..10]
Definition: Category of the investment fund order.
OrderType <OrdrTp> contains one of the following elements (see "FundOrderType4Choice" on
page 4740 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
44.4.4.9.5  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class related to the order.
Impacted by: C21 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2149 May 2026
```

## File page 2150

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2151
{Or     ISIN <ISIN> [1..1] IdentifierSet 2151
Or     SEDOL <SEDOL> [1..1] IdentifierSet 2152
Or     CUSIP <CUSIP> [1..1] IdentifierSet 2152
Or     RIC <RIC> [1..1] IdentifierSet 2152
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 2152
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 2152
Or     CTA <CTA> [1..1] IdentifierSet 2152
Or     QUICK <QUICK> [1..1] IdentifierSet 2152
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 2153
Or     Dutch <Dtch> [1..1] IdentifierSet 2153
Or     Valoren <Vlrn> [1..1] IdentifierSet 2153
Or     Sicovam <SCVM> [1..1] IdentifierSet 2153
Or     Belgian <Belgn> [1..1] IdentifierSet 2153
Or     Common <Cmon> [1..1] IdentifierSet 2153
Or     DTI <DTI> [1..1] IdentifierSet 2153
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  2153
       Identification <Id> [1..1] Text 2154
       IdentificationSource <IdSrc> [1..1] ± 2154
   Name <Nm> [0..1] Text 2154
   ShortName <ShrtNm> [0..1] Text 2154
   SupplementaryIdentification <SplmtryId> [0..1] Text 2154
   ClassType <ClssTp> [0..1] Text 2154
   SecuritiesForm <SctiesForm> [0..1] CodeSet 2155
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2155
   ProductGroup <PdctGrp> [0..1] Text 2155
   SeriesIdentification <SrsId> [0..1]  C34 2155
     SeriesDate <SrsDt> [0..1] ± 2156
     SeriesName <SrsNm> [0..1] Text 2156
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2150 May 2026
```

