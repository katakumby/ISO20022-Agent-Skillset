---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.4 Message Building Blocks", "65.4.2 RequestDetails <ReqDtls>", "65.4.2.3 OrderReference <OrdrRef>", "65.4.2.3.7 InvestmentAccountDetails <InvstmtAcctDtls>", "65.4.2.3.7.7 SubAccountDetails <SubAcctDtls>"]
file_pages: [4315, 4316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.4.2.3.7.7 SubAccountDetails <SubAcctDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4315 to 4316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4315

```text
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
the protections afforded by conduct of
business rules defined under MiFID.
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
65.4.2.3.7.7  SubAccountDetails <SubAcctDtls>
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
65.4.2.3.7.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
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
65.4.2.3.8  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..1]
Definition: Financial instrument information of the individual order or individual order cancellation
request for which the status is requested.
Impacted by: C4 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4315 May 2026
```

## File page 4316

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4317
{Or     ISIN <ISIN> [1..1] IdentifierSet 4317
Or     SEDOL <SEDOL> [1..1] IdentifierSet 4318
Or     CUSIP <CUSIP> [1..1] IdentifierSet 4318
Or     RIC <RIC> [1..1] IdentifierSet 4318
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 4318
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 4318
Or     CTA <CTA> [1..1] IdentifierSet 4318
Or     QUICK <QUICK> [1..1] IdentifierSet 4318
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 4319
Or     Dutch <Dtch> [1..1] IdentifierSet 4319
Or     Valoren <Vlrn> [1..1] IdentifierSet 4319
Or     Sicovam <SCVM> [1..1] IdentifierSet 4319
Or     Belgian <Belgn> [1..1] IdentifierSet 4319
Or     Common <Cmon> [1..1] IdentifierSet 4319
Or     DTI <DTI> [1..1] IdentifierSet 4319
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  4319
       Identification <Id> [1..1] Text 4320
       IdentificationSource <IdSrc> [1..1] ± 4320
   Name <Nm> [0..1] Text 4320
   ShortName <ShrtNm> [0..1] Text 4320
   SupplementaryIdentification <SplmtryId> [0..1] Text 4320
   ClassType <ClssTp> [0..1] Text 4320
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4321
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4321
   ProductGroup <PdctGrp> [0..1] Text 4321
   SeriesIdentification <SrsId> [0..1]  C9 4321
     SeriesDate <SrsDt> [0..1] ± 4322
     SeriesName <SrsNm> [0..1] Text 4322
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4316 May 2026
```

