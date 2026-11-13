---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.4 ExtendedParty14", "66.1.30.4.2 OtherPartyDetails <OthrPtyDtls>"]
file_pages: [4913, 4914]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.4.2 OtherPartyDetails <OthrPtyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4913 to 4914.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4913

```text
66.1.30.4.2  OtherPartyDetails <OthrPtyDtls>
Presence: [1..1]
Definition: Detailed ownership information about a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4913 May 2026
```

## File page 4914

```text
OtherPartyDetails <OthrPtyDtls> contains the following elements (see
"InvestmentAccountOwnershipInformation16" on page 4597 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  4599
{Or     Organisation <Org> [1..1] ± C24 4599
Or}     IndividualPerson <IndvPrsn> [1..1] ± 4600
   MoneyLaunderingCheck <MnyLndrgChck> [0..1] ± 4602
   InvestorProfileValidation <InvstrPrflVldtn> [0..*]  4602
     CertificationIndicator <CertfctnInd> [0..1] Indicator 4603
     ValidatingParty <VldtngPty> [0..1] Text 4603
     CheckingParty <ChckngPty> [0..1] Text 4603
     ResponsibleParty <RspnsblPty> [0..1] Text 4604
     CertificateType <CertTp> [0..1] ± 4604
     CheckingDate <ChckngDt> [0..1] Date 4604
     CheckingFrequency <ChckngFrqcy> [0..1] CodeSet 4604
     NextRevisionDate <NxtRvsnDt> [0..1] Date 4605
     SalaryRange <SlryRg> [0..1] Text 4605
     SourceOfWealth <SrcOfWlth> [0..1] Text 4605
     CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 4605
     RiskLevel <RskLvl> [0..1] ± 4605
     KnowYourCustomerCheckType
<KnowYourCstmrChckTp>
[0..1] ± 4605
     KnowYourCustomerDatabaseCheck
<KnowYourCstmrDBChck>
[0..1] ± 4606
   OwnershipBeneficiaryRate <OwnrshBnfcryRate> [0..1] ± C25 4606
   ClientIdentification <ClntId> [0..1] Text 4606
   FiscalExemption <FsclXmptn> [0..1] Indicator 4607
   SignatoryRightIndicator <SgntryRghtInd> [0..1] Indicator 4607
   MiFIDClassification <MiFIDClssfctn> [0..1] ± 4607
   Notification <Ntfctn> [0..*] ± 4607
   FATCAFormType <FATCAFormTp> [0..*] ± 4607
   FATCAStatus <FATCASts> [0..*] ± 4608
   FATCAReportingDate <FATCARptgDt> [0..1] Date 4608
   CRSFormType <CRSFormTp> [0..*] ± 4608
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4914 May 2026
```

