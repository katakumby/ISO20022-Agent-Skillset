---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.4 OrderDateTime <OrdrDtTm>"]
file_pages: [1928, 1929]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.4 OrderDateTime <OrdrDtTm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1928 to 1929.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1928

```text
PlaceOfTrade <PlcOfTrad> contains one of the following elements (see
"PlaceOfTradeIdentification4Choice" on page 4808 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C12 4809
Or   Exchange <Xchg> [1..1] IdentifierSet 4809
Or   Party <Pty> [1..1] IdentifierSet C4 4809
Or}   OverTheCounter <OverTheCntr> [1..1] Text 4809
43.4.5.4  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Definition: Date and time at which the order was placed by the investor or its agent.
Datatype: "ISODateTime" on page 5388
43.4.5.5  ReceivedDateTime <RcvdDtTm>
Presence: [0..1]
Definition: Date and time the order was received by the executing party, for example, the transfer agent.
Datatype: "ISODateTime" on page 5388
43.4.5.6  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed.
The specification of a requested future trade date is not allowed in some markets. The date must be a
date in the future.
Datatype: "ISODate" on page 5388
43.4.5.7  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
43.4.5.8  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the investment fund order execution is related.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1928 May 2026
```

## File page 1929

```text
Impacted by: C20 "IdentificationGuideline"
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1930
{Or     ISIN <ISIN> [1..1] IdentifierSet 1930
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1931
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1931
Or     RIC <RIC> [1..1] IdentifierSet 1931
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1931
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1931
Or     CTA <CTA> [1..1] IdentifierSet 1931
Or     QUICK <QUICK> [1..1] IdentifierSet 1931
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1932
Or     Dutch <Dtch> [1..1] IdentifierSet 1932
Or     Valoren <Vlrn> [1..1] IdentifierSet 1932
Or     Sicovam <SCVM> [1..1] IdentifierSet 1932
Or     Belgian <Belgn> [1..1] IdentifierSet 1932
Or     Common <Cmon> [1..1] IdentifierSet 1932
Or     DTI <DTI> [1..1] IdentifierSet 1932
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1932
       Identification <Id> [1..1] Text 1933
       IdentificationSource <IdSrc> [1..1] ± 1933
   Name <Nm> [0..1] Text 1933
   ShortName <ShrtNm> [0..1] Text 1933
   SupplementaryIdentification <SplmtryId> [0..1] Text 1933
   ClassType <ClssTp> [0..1] Text 1933
   SecuritiesForm <SctiesForm> [0..1] CodeSet 1934
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1934
   ProductGroup <PdctGrp> [0..1] Text 1934
   SeriesIdentification <SrsId> [0..1]  C36 1934
     SeriesDate <SrsDt> [0..1] ± 1935
     SeriesName <SrsNm> [0..1] Text 1935
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1929 May 2026
```

