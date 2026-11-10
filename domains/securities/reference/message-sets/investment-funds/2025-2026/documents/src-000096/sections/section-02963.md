---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.10 OrderData <OrdrData>", "56.4.3.2.10.1 InvestmentAccountDetails <InvstmtAcctDtls>", "56.4.3.2.10.1.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [4157, 4158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.10.1.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4157 to 4158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4157

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
56.4.3.2.10.1.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
56.4.3.2.10.2  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..1]
Definition: Financial instrument information of the individual order instruction for which the status is
given.
Impacted by: C13 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4157 May 2026
```

## File page 4158

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4159
{Or     ISIN <ISIN> [1..1] IdentifierSet 4159
Or     SEDOL <SEDOL> [1..1] IdentifierSet 4160
Or     CUSIP <CUSIP> [1..1] IdentifierSet 4160
Or     RIC <RIC> [1..1] IdentifierSet 4160
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 4160
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 4160
Or     CTA <CTA> [1..1] IdentifierSet 4160
Or     QUICK <QUICK> [1..1] IdentifierSet 4160
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 4161
Or     Dutch <Dtch> [1..1] IdentifierSet 4161
Or     Valoren <Vlrn> [1..1] IdentifierSet 4161
Or     Sicovam <SCVM> [1..1] IdentifierSet 4161
Or     Belgian <Belgn> [1..1] IdentifierSet 4161
Or     Common <Cmon> [1..1] IdentifierSet 4161
Or     DTI <DTI> [1..1] IdentifierSet 4161
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  4161
       Identification <Id> [1..1] Text 4162
       IdentificationSource <IdSrc> [1..1] ± 4162
   Name <Nm> [0..1] Text 4162
   ShortName <ShrtNm> [0..1] Text 4162
   SupplementaryIdentification <SplmtryId> [0..1] Text 4162
   ClassType <ClssTp> [0..1] Text 4162
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4163
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4163
   ProductGroup <PdctGrp> [0..1] Text 4163
   SeriesIdentification <SrsId> [0..1]  C19 4163
     SeriesDate <SrsDt> [0..1] ± 4164
     SeriesName <SrsNm> [0..1] Text 4164
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4158 May 2026
```

