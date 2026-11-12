---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>", "64.4.3.8 InvestmentAccountDetails <InvstmtAcctDtls>", "64.4.3.8.7 SubAccountDetails <SubAcctDtls>"]
file_pages: [4295, 4296]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3.8.7 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4295 to 4296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4295

```text
CodeName Name Definition
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
64.4.3.8.7  SubAccountDetails <SubAcctDtls>
Presence: [0..1]
Definition: Sub-account of the master or omnibus account.
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount6" on
page 4642 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4642
   Name <Nm> [0..1] Text 4642
   Characteristic <Chrtc> [0..1] Text 4642
   AccountDesignation <AcctDsgnt> [0..1] Text 4642
64.4.3.8.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
64.4.3.9  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..1]
Definition: Financial instrument information of the individual order confirmation for which the status is
given.
Impacted by: C4 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4295 May 2026
```

## File page 4296

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4297
{Or     ISIN <ISIN> [1..1] IdentifierSet 4297
Or     SEDOL <SEDOL> [1..1] IdentifierSet 4298
Or     CUSIP <CUSIP> [1..1] IdentifierSet 4298
Or     RIC <RIC> [1..1] IdentifierSet 4298
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 4298
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 4298
Or     CTA <CTA> [1..1] IdentifierSet 4298
Or     QUICK <QUICK> [1..1] IdentifierSet 4298
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 4299
Or     Dutch <Dtch> [1..1] IdentifierSet 4299
Or     Valoren <Vlrn> [1..1] IdentifierSet 4299
Or     Sicovam <SCVM> [1..1] IdentifierSet 4299
Or     Belgian <Belgn> [1..1] IdentifierSet 4299
Or     Common <Cmon> [1..1] IdentifierSet 4299
Or     DTI <DTI> [1..1] IdentifierSet 4299
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  4299
       Identification <Id> [1..1] Text 4300
       IdentificationSource <IdSrc> [1..1] ± 4300
   Name <Nm> [0..1] Text 4300
   ShortName <ShrtNm> [0..1] Text 4300
   SupplementaryIdentification <SplmtryId> [0..1] Text 4300
   ClassType <ClssTp> [0..1] Text 4300
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4301
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4301
   ProductGroup <PdctGrp> [0..1] Text 4301
   SeriesIdentification <SrsId> [0..1]  C9 4301
     SeriesDate <SrsDt> [0..1] ± 4302
     SeriesName <SrsNm> [0..1] Text 4302
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4296 May 2026
```

