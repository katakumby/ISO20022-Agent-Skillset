---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.5 ModifiedInvestmentAccount <ModfdInvstmtAcct>"]
file_pages: [66, 67, 68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.5 ModifiedInvestmentAccount <ModfdInvstmtAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 66 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
OtherAccountSelectionData <OthrAcctSelctnData> contains the following elements (see
"InvestmentAccount76" on page 4633 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4634
   Designation <Dsgnt> [0..1] Text 4634
   FundType <FndTp> [0..1] Text 4634
   FundFamilyName <FndFmlyNm> [0..1] Text 4634
   SecurityDetails <SctyDtls> [0..1]  C15 4634
     Identification <Id> [1..1] ± 4635
     Name <Nm> [0..1] Text 4636
     ShortName <ShrtNm> [0..1] Text 4636
     SupplementaryIdentification <SplmtryId> [0..1] Text 4636
     ClassType <ClssTp> [0..1] Text 4637
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4637
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4637
     ProductGroup <PdctGrp> [0..1] Text 4637
   AccountOwner <AcctOwnr> [0..1]  4637
{Or     IndividualOwnerIdentification <IndvOwnrId> [1..1]  4638
{Or       IdentificationNumber <IdNb> [1..1] ± 4638
Or}       PersonName <PrsnNm> [1..1] ± 4638
Or}     OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± C21 4639
   Intermediary <Intrmy> [0..*] ± 4639
   AccountServicer <AcctSvcr> [0..1] ± 4640
Constraints
• AccountDataElementRule
One of the elements (Name, Designation, FundType, FundFamilyName, SecurityDetails,
AccountOwner, Intermediary, Account Servicer) must be present.
4.4.5 ModifiedInvestmentAccount <ModfdInvstmtAcct>
Presence: [0..1]
Definition: Information related to general characteristics of the account to be inserted, updated or
deleted.
Impacted by: C2 "AccountElementRule", C17 "IncomePreferenceReinvestmentRule", C29
"ReinvestmentPercentageRule", C12 "FinancialInstrumentDetailsGuideline"
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 66 May 2026
```

## File page 67

```text
ModifiedInvestmentAccount <ModfdInvstmtAcct> contains the following elements (see
"InvestmentAccount75" on page 4645 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountStatusUpdateInstruction <AcctStsUpdInstr> [0..1] ± 4647
   Name <Nm> [0..1] Text 4648
   Designation <Dsgnt> [0..1] Text 4648
   Type <Tp> [0..1] ± 4648
   OwnershipType <OwnrshTp> [0..1] ± 4649
   TaxExemption <TaxXmptn> [0..1] ± 4649
   StatementFrequency <StmtFrqcy> [0..1] ± 4649
   ReferenceCurrency <RefCcy> [0..1] CodeSet C1 4649
   Language <Lang> [0..1] CodeSet C34 4650
   IncomePreference <IncmPref> [0..1] CodeSet 4650
   ReinvestmentDetails <RinvstmtDtls> [0..*] ± 4650
   TaxWithholdingMethod <TaxWhldgMtd> [0..1] CodeSet 4650
   TaxReporting <TaxRptg> [0..*] ± 4651
   LetterIntentDetails <LttrInttDtls> [0..1] ± 4652
   AccumulationRightReference <AcmltnRghtRef> [0..1] Text 4653
   RequiredSignatoriesNumber <ReqrdSgntriesNb> [0..1] Quantity 4653
   FundFamilyName <FndFmlyNm> [0..1] Text 4653
   ModifiedFinancialInstrumentDetails
<ModfdFinInstrmDtls>
[0..*]  4653
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4653
     FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C20 4654
   RoundingDetails <RndgDtls> [0..1] ± 4655
   AccountServicer <AcctSvcr> [0..1] ± 4655
   BlockedStatus <BlckdSts> [0..1] ± 4655
   AccountUsageType <AcctUsgTp> [0..1] ± 4656
   ForeignStatusCertification <FrgnStsCertfctn> [0..1] CodeSet 4656
   AccountSignatureDateTime <AcctSgntrDtTm> [0..1] ± 4656
   TransactionChannelType <TxChanlTp> [0..1] ± 4657
   InvestmentAccountCategory <InvstmtAcctCtgy> [0..1] ± 4657
   Pledging <Pldgg> [0..1] CodeSet 4657
   Collateral <Coll> [0..1] CodeSet 4657
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 67 May 2026
```

## File page 68

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ThirdPartyRights <ThrdPtyRghts> [0..1] ± 4658
   PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> [0..1] ± 4658
   AccountingStatus <AcctgSts> [0..1] ± 4658
   OpeningDate <OpngDt> [0..1] ± 4659
   ClosingDate <ClsgDt> [0..1] ± 4659
   NegativeIndicator <NegInd> [0..1] Indicator 4659
   ProcessingOrder <PrcgOrdr> [0..1] CodeSet 4659
   Liability <Lblty> [0..1] ± 4659
   ModifiedInvestorProfile <ModfdInvstrPrfl> [0..*]  4660
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4660
     InvestorProfile <InvstrPrfl> [1..1] ± 4660
   FiscalYear <FsclYr> [0..1] ± 4661
Constraints
• AccountElementRule
One of the elements (AccountStatusUpdateInstruction, Name, Designation, Type, OwnershipType,
TaxExemption, StatementFrequency, ReferenceCurrency, Language, IncomePreference,
ReinvestmentDetails, TaxWithholdingMethod, TaxReporting, LetterIntentDetails,
AccumulationRightReference, RequiredSignatoriesNumber, FundFamilyName,
ModifiedFinancialInstrumentDetails, RoundingDetails, Account Servicer, BlockedStatus,
AccountUsageType, ForeignStatusCertification, AccountSignatureDateTime,
TransactionChannelType, InvestmentAccountCategory, Pledging, Collateral, ThirdPartyRights,
PowerOfAttorneyLevelOfControl, AccountingStatus, OpeningDate, ClosingDate, NegativeIndicator,
ProcessingOrder, Liability, ModifiedInvestorProfile, FiscalYear) must be present.
• FinancialInstrumentDetailsGuideline
ModifiedFinancialInstrumentDetails/FinancialInstrumentDetails may be present if a single investment
fund is associated to the investment account. If several investment funds are associated to the
investment account, the FundFamilyName only should be specified.
• IncomePreferenceReinvestmentRule
If IncomePreference is CASH (Cash), then ReinvestmentDetails is not allowed.
On Condition
    /IncomePreference is equal to value 'Cash'
Following Must be True
    /ReinvestmentDetails[*] Must be absent
• ReinvestmentPercentageRule
Sum of all occurrences of ReinvestmentDetails/ReinvestmentPercentage must not be greater than
100.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 68 May 2026
```

