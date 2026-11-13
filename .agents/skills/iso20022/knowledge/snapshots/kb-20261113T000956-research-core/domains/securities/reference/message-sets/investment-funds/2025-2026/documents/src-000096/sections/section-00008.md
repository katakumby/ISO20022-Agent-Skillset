---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks", "2.4.4 InstructionDetails <InstrDtls>", "2.4.4.5 ExistingAccountIdentification <ExstgAcctId>"]
file_pages: [27, 28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4.4.5 ExistingAccountIdentification <ExstgAcctId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 27 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference13"
on page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
2.4.4.5  ExistingAccountIdentification <ExstgAcctId>
Presence: [0..*]
Definition: Account to which the account opening is related.
ExistingAccountIdentification <ExstgAcctId> contains the following elements (see "Account23" on
page 4325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4325
   RelatedAccountDetails <RltdAcctDtls> [0..1] ± 4325
2.4.5 InvestmentAccount <InvstmtAcct>
Presence: [1..1]
Definition: Detailed information about the account to be opened.
Impacted by: C13 "IncomePreferenceReinvestment1Rule", C23 "ReinvestmentPercentage1Rule", C9
"FinancialInstrumentDetailsGuideline"
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 27 May 2026
```

## File page 28

```text
InvestmentAccount <InvstmtAcct> contains the following elements (see "InvestmentAccount73" on
page 4618 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4620
   Name <Nm> [0..1] Text 4620
   Designation <Dsgnt> [0..1] Text 4620
   Type <Tp> [0..1] ± 4621
   OwnershipType <OwnrshTp> [1..1] ± 4621
   TaxExemption <TaxXmptn> [0..1] ± 4621
   StatementFrequency <StmtFrqcy> [0..1] ± 4621
   ReferenceCurrency <RefCcy> [0..1] CodeSet C1 4622
   Language <Lang> [0..1] CodeSet C34 4622
   IncomePreference <IncmPref> [0..1] CodeSet 4622
   ReinvestmentDetails <RinvstmtDtls> [0..*] ± 4622
   TaxWithholdingMethod <TaxWhldgMtd> [0..1] CodeSet 4623
   TaxReporting <TaxRptg> [0..*] ± 4623
   LetterIntentDetails <LttrInttDtls> [0..1] ± 4624
   AccumulationRightReference <AcmltnRghtRef> [0..1] Text 4625
   RequiredSignatoriesNumber <ReqrdSgntriesNb> [0..1] Quantity 4625
   FundFamilyName <FndFmlyNm> [0..1] Text 4625
   FinancialInstrumentDetails <FinInstrmDtls> [0..*] ± C20 4625
   RoundingDetails <RndgDtls> [0..1] ± 4626
   AccountServicer <AcctSvcr> [0..1] ± 4627
   BlockedStatus <BlckdSts> [0..1] ± 4627
   AccountUsageType <AcctUsgTp> [0..1] ± 4628
   ForeignStatusCertification <FrgnStsCertfctn> [0..1] CodeSet 4628
   AccountSignatureDateTime <AcctSgntrDtTm> [0..1] ± 4628
   TransactionChannelType <TxChanlTp> [0..1] ± 4628
   InvestmentAccountCategory <InvstmtAcctCtgy> [0..1] ± 4628
   Pledging <Pldgg> [0..1] CodeSet 4629
   Collateral <Coll> [0..1] CodeSet 4629
   ThirdPartyRights <ThrdPtyRghts> [0..1] ± 4629
   PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> [0..1] ± 4630
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 28 May 2026
```

