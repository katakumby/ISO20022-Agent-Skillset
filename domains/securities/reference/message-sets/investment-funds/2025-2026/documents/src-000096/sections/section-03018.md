---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.2 IndividualCancellationStatusReport <IndvCxlStsRpt>", "57.4.3.2.8 InvestmentAccountDetails <InvstmtAcctDtls>", "57.4.3.2.8.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [4224, 4225]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.2.8.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4224 to 4225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4224

```text
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount6" on
page 4642 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4642
   Name <Nm> [0..1] Text 4642
   Characteristic <Chrtc> [0..1] Text 4642
   AccountDesignation <AcctDsgnt> [0..1] Text 4642
57.4.3.2.8.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
57.4.3.2.9  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..1]
Definition: Financial instrument information of the individual order cancellation for which the status is
given.
Impacted by: C4 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4224 May 2026
```

## File page 4225

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4226
{Or     ISIN <ISIN> [1..1] IdentifierSet 4226
Or     SEDOL <SEDOL> [1..1] IdentifierSet 4227
Or     CUSIP <CUSIP> [1..1] IdentifierSet 4227
Or     RIC <RIC> [1..1] IdentifierSet 4227
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 4227
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 4227
Or     CTA <CTA> [1..1] IdentifierSet 4227
Or     QUICK <QUICK> [1..1] IdentifierSet 4227
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 4228
Or     Dutch <Dtch> [1..1] IdentifierSet 4228
Or     Valoren <Vlrn> [1..1] IdentifierSet 4228
Or     Sicovam <SCVM> [1..1] IdentifierSet 4228
Or     Belgian <Belgn> [1..1] IdentifierSet 4228
Or     Common <Cmon> [1..1] IdentifierSet 4228
Or     DTI <DTI> [1..1] IdentifierSet 4228
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  4228
       Identification <Id> [1..1] Text 4229
       IdentificationSource <IdSrc> [1..1] ± 4229
   Name <Nm> [0..1] Text 4229
   ShortName <ShrtNm> [0..1] Text 4229
   SupplementaryIdentification <SplmtryId> [0..1] Text 4229
   ClassType <ClssTp> [0..1] Text 4229
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4230
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4230
   ProductGroup <PdctGrp> [0..1] Text 4230
   SeriesIdentification <SrsId> [0..1]  C9 4230
     SeriesDate <SrsDt> [0..1] ± 4231
     SeriesName <SrsNm> [0..1] Text 4231
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4225 May 2026
```

