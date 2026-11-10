---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>", "56.4.3.3.8.5 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [4195, 4196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8.5 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4195 to 4196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4195

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
56.4.3.3.8.5  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..1]
Definition: Financial instrument identification of the switch leg that is rejected or repaired.
Impacted by: C13 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4195 May 2026
```

## File page 4196

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4197
{Or     ISIN <ISIN> [1..1] IdentifierSet 4197
Or     SEDOL <SEDOL> [1..1] IdentifierSet 4198
Or     CUSIP <CUSIP> [1..1] IdentifierSet 4198
Or     RIC <RIC> [1..1] IdentifierSet 4198
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 4198
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 4198
Or     CTA <CTA> [1..1] IdentifierSet 4198
Or     QUICK <QUICK> [1..1] IdentifierSet 4198
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 4199
Or     Dutch <Dtch> [1..1] IdentifierSet 4199
Or     Valoren <Vlrn> [1..1] IdentifierSet 4199
Or     Sicovam <SCVM> [1..1] IdentifierSet 4199
Or     Belgian <Belgn> [1..1] IdentifierSet 4199
Or     Common <Cmon> [1..1] IdentifierSet 4199
Or     DTI <DTI> [1..1] IdentifierSet 4199
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  4199
       Identification <Id> [1..1] Text 4200
       IdentificationSource <IdSrc> [1..1] ± 4200
   Name <Nm> [0..1] Text 4200
   ShortName <ShrtNm> [0..1] Text 4200
   SupplementaryIdentification <SplmtryId> [0..1] Text 4200
   ClassType <ClssTp> [0..1] Text 4200
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4201
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4201
   ProductGroup <PdctGrp> [0..1] Text 4201
   SeriesIdentification <SrsId> [0..1]  C19 4201
     SeriesDate <SrsDt> [0..1] ± 4202
     SeriesName <SrsNm> [0..1] Text 4202
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4196 May 2026
```

