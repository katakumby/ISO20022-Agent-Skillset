---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.10 AccountParties17", "66.1.30.10.1 PrincipalAccountParty <PrncplAcctPty>"]
file_pages: [4925, 4926]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.10.1 PrincipalAccountParty <PrncplAcctPty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4925 to 4926.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4925

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PrincipalAccountParty <PrncplAcctPty> [1..1]  4925
{Or     PrimaryOwner <PmryOwnr> [1..1] ± 4925
Or     Trustee <Trstee> [1..5] ± 4927
Or     Nominee <Nmnee> [1..1] ± 4929
Or}     JointOwner <JntOwnr> [1..5] ± 4931
   SecondaryOwner <ScndryOwnr> [0..*] ± 4933
   Beneficiary <Bnfcry> [0..*] ± 4935
   PowerOfAttorney <PwrOfAttny> [0..*] ± 4937
   LegalGuardian <LglGuardn> [0..*] ± 4939
   CustodianForMinor <CtdnForMnr> [0..*] ± 4941
   SuccessorOnDeath <SucssrOnDth> [0..*] ± 4943
   Administrator <Admstr> [0..*] ± 4945
   OtherParty <OthrPty> [0..*] ± 4947
   Granter <Grntr> [0..*] ± 4947
   Settlor <Sttlr> [0..*] ± 4949
   SeniorManagingOfficial <SnrMggOffcl> [0..*] ± 4951
   Protector <Prtctr> [0..*] ± 4953
   RegisteredShareholderName <RegdShrhldrNm> [0..1] ± 4955
66.1.30.10.1  PrincipalAccountParty <PrncplAcctPty>
Presence: [1..1]
Definition: Main party associated with the account.
PrincipalAccountParty <PrncplAcctPty> contains one of the following AccountParties12Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PrimaryOwner <PmryOwnr> [1..1] ± 4925
Or   Trustee <Trstee> [1..5] ± 4927
Or   Nominee <Nmnee> [1..1] ± 4929
Or}   JointOwner <JntOwnr> [1..5] ± 4931
66.1.30.10.1.1  PrimaryOwner <PmryOwnr>
Presence: [1..1]
Definition: Single owner of the account or, when the ownership is split among several owners, the
primary owner is the one giving its address and account details for the registration.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4925 May 2026
```

## File page 4926

```text
PrimaryOwner <PmryOwnr> contains the following elements (see
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
Investment Funds - Maintenance 2025 - 2026 4926 May 2026
```

