---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.5 RequestedFutureTradeDate <ReqdFutrTradDt>"]
file_pages: [2562, 2563]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.5 RequestedFutureTradeDate <ReqdFutrTradDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2562 to 2563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2562

```text
ExpiryDateTime <XpryDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
47.4.4.5  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed.
The specification of a requested future trade date is not allowed in some markets. The date must be a
date in the future.
Datatype: "ISODate" on page 5388
47.4.4.6  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
47.4.4.7  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class related to the order.
Impacted by: C21 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2562 May 2026
```

## File page 2563

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2564
{Or     ISIN <ISIN> [1..1] IdentifierSet 2564
Or     SEDOL <SEDOL> [1..1] IdentifierSet 2565
Or     CUSIP <CUSIP> [1..1] IdentifierSet 2565
Or     RIC <RIC> [1..1] IdentifierSet 2565
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 2565
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 2565
Or     CTA <CTA> [1..1] IdentifierSet 2565
Or     QUICK <QUICK> [1..1] IdentifierSet 2565
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 2566
Or     Dutch <Dtch> [1..1] IdentifierSet 2566
Or     Valoren <Vlrn> [1..1] IdentifierSet 2566
Or     Sicovam <SCVM> [1..1] IdentifierSet 2566
Or     Belgian <Belgn> [1..1] IdentifierSet 2566
Or     Common <Cmon> [1..1] IdentifierSet 2566
Or     DTI <DTI> [1..1] IdentifierSet 2566
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  2566
       Identification <Id> [1..1] Text 2567
       IdentificationSource <IdSrc> [1..1] ± 2567
   Name <Nm> [0..1] Text 2567
   ShortName <ShrtNm> [0..1] Text 2567
   SupplementaryIdentification <SplmtryId> [0..1] Text 2567
   ClassType <ClssTp> [0..1] Text 2567
   SecuritiesForm <SctiesForm> [0..1] CodeSet 2568
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2568
   ProductGroup <PdctGrp> [0..1] Text 2568
   SeriesIdentification <SrsId> [0..1]  C34 2568
     SeriesDate <SrsDt> [0..1] ± 2569
     SeriesName <SrsNm> [0..1] Text 2569
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2563 May 2026
```

