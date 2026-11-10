---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17"]
file_pages: [4575, 4576]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4 InvestmentAccountOwnershipInformation17

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4575 to 4576.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4575

```text
FiscalYear <FsclYr> contains one of the following elements (see "FiscalYear1Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StartDate <StartDt> [1..1] Date 4467
Or}   EndDate <EndDt> [1..1] Date 4468
66.1.24.4  InvestmentAccountOwnershipInformation17
Definition: Characteristics of the ownership of an investment account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4575 May 2026
```

## File page 4576

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  4577
{Or     Organisation <Org> [1..1] ± C20 4577
Or}     IndividualPerson <IndvPrsn> [1..1] ± 4578
   MoneyLaunderingCheck <MnyLndrgChck> [0..1] ± 4580
   ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn> [0..*]  4580
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4581
     InvestorProfileValidation <InvstrPrflVldtn> [1..1]  4581
       CertificationIndicator <CertfctnInd> [0..1] Indicator 4582
       ValidatingParty <VldtngPty> [0..1] Text 4582
       CheckingParty <ChckngPty> [0..1] Text 4582
       ResponsibleParty <RspnsblPty> [0..1] Text 4583
       CertificateType <CertTp> [0..1] ± 4583
       CheckingDate <ChckngDt> [0..1] Date 4583
       CheckingFrequency <ChckngFrqcy> [0..1] CodeSet 4583
       NextRevisionDate <NxtRvsnDt> [0..1] Date 4584
       SalaryRange <SlryRg> [0..1] Text 4584
       SourceOfWealth <SrcOfWlth> [0..1] Text 4584
       CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 4584
       RiskLevel <RskLvl> [0..1] ± 4584
       KnowYourCustomerCheckType
<KnowYourCstmrChckTp>
[0..1] ± 4584
       KnowYourCustomerDatabaseCheck
<KnowYourCstmrDBChck>
[0..1] ± 4585
   OwnershipBeneficiaryRate <OwnrshBnfcryRate> [0..1] ± C25 4585
   ClientIdentification <ClntId> [0..1] Text 4585
   FiscalExemption <FsclXmptn> [0..1] Indicator 4586
   SignatoryRightIndicator <SgntryRghtInd> [0..1] Indicator 4586
   MiFIDClassification <MiFIDClssfctn> [0..1] ± 4586
   Notification <Ntfctn> [0..*] ± 4586
   FATCAFormType <FATCAFormTp> [0..*] ± 4586
   FATCAStatus <FATCASts> [0..*] ± 4587
   FATCAReportingDate <FATCARptgDt> [0..1] Date 4587
   CRSFormType <CRSFormTp> [0..*] ± 4587
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4576 May 2026
```

