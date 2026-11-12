---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.5 ReceivedDateTime <RcvdDtTm>"]
file_pages: [2806, 2807]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.5 ReceivedDateTime <RcvdDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2806 to 2807.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2806

```text
Datatype: "ISODateTime" on page 5388
49.4.5.5  ReceivedDateTime <RcvdDtTm>
Presence: [0..1]
Definition: Date and time the order was received by the executing party, for example, the transfer agent.
Datatype: "ISODateTime" on page 5388
49.4.5.6  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed.
The specification of a requested future trade date is not allowed in some markets. The date must be a
date in the future.
Datatype: "ISODate" on page 5388
49.4.5.7  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
49.4.5.8  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the investment fund order execution is related.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2806 May 2026
```

## File page 2807

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2808
{Or     ISIN <ISIN> [1..1] IdentifierSet 2808
Or     SEDOL <SEDOL> [1..1] IdentifierSet 2809
Or     CUSIP <CUSIP> [1..1] IdentifierSet 2809
Or     RIC <RIC> [1..1] IdentifierSet 2809
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 2809
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 2809
Or     CTA <CTA> [1..1] IdentifierSet 2809
Or     QUICK <QUICK> [1..1] IdentifierSet 2809
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 2810
Or     Dutch <Dtch> [1..1] IdentifierSet 2810
Or     Valoren <Vlrn> [1..1] IdentifierSet 2810
Or     Sicovam <SCVM> [1..1] IdentifierSet 2810
Or     Belgian <Belgn> [1..1] IdentifierSet 2810
Or     Common <Cmon> [1..1] IdentifierSet 2810
Or     DTI <DTI> [1..1] IdentifierSet 2810
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  2810
       Identification <Id> [1..1] Text 2811
       IdentificationSource <IdSrc> [1..1] ± 2811
   Name <Nm> [0..1] Text 2811
   ShortName <ShrtNm> [0..1] Text 2811
   SupplementaryIdentification <SplmtryId> [0..1] Text 2811
   ClassType <ClssTp> [0..1] Text 2811
   SecuritiesForm <SctiesForm> [0..1] CodeSet 2812
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2812
   ProductGroup <PdctGrp> [0..1] Text 2812
   SeriesIdentification <SrsId> [0..1]  C36 2812
     SeriesDate <SrsDt> [0..1] ± 2813
     SeriesName <SrsNm> [0..1] Text 2813
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2807 May 2026
```

