---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.7 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [1719, 1720]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.7 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1719 to 1720.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1719

```text
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
41.4.4.7  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class related to the order.
Impacted by: C21 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1719 May 2026
```

## File page 1720

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1721
{Or     ISIN <ISIN> [1..1] IdentifierSet 1721
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1722
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1722
Or     RIC <RIC> [1..1] IdentifierSet 1722
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1722
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1722
Or     CTA <CTA> [1..1] IdentifierSet 1722
Or     QUICK <QUICK> [1..1] IdentifierSet 1722
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1723
Or     Dutch <Dtch> [1..1] IdentifierSet 1723
Or     Valoren <Vlrn> [1..1] IdentifierSet 1723
Or     Sicovam <SCVM> [1..1] IdentifierSet 1723
Or     Belgian <Belgn> [1..1] IdentifierSet 1723
Or     Common <Cmon> [1..1] IdentifierSet 1723
Or     DTI <DTI> [1..1] IdentifierSet 1723
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1723
       Identification <Id> [1..1] Text 1724
       IdentificationSource <IdSrc> [1..1] ± 1724
   Name <Nm> [0..1] Text 1724
   ShortName <ShrtNm> [0..1] Text 1724
   SupplementaryIdentification <SplmtryId> [0..1] Text 1724
   ClassType <ClssTp> [0..1] Text 1724
   SecuritiesForm <SctiesForm> [0..1] CodeSet 1725
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1725
   ProductGroup <PdctGrp> [0..1] Text 1725
   SeriesIdentification <SrsId> [0..1]  C34 1725
     SeriesDate <SrsDt> [0..1] ± 1726
     SeriesName <SrsNm> [0..1] Text 1726
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1720 May 2026
```

