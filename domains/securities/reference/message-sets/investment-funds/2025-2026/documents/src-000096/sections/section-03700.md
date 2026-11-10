---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.19 AccountParties18", "66.1.30.19.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [4969, 4970]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.19.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4969 to 4970.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4969

```text
LegalGuardian/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
SuccessorOnDeath/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Administrator/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
OtherParty/OtherPartyDetails/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Granter/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
Settlor/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
SeniorManagingOfficial/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Protector/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet).
66.1.30.19.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.30.19.2  PrincipalAccountParty <PrncplAcctPty>
Presence: [0..1]
Definition: Main party associated with the account.
PrincipalAccountParty <PrncplAcctPty> contains one of the following AccountParties13Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PrimaryOwner <PmryOwnr> [1..1] ± 4969
Or   Trustee <Trstee> [1..5] ± 4971
Or   Nominee <Nmnee> [1..1] ± 4973
Or}   JointOwner <JntOwnr> [1..5] ± 4975
66.1.30.19.2.1  PrimaryOwner <PmryOwnr>
Presence: [1..1]
Definition: Single owner of the investment account or, when the ownership is split among several
owners, the primary owner is the one giving its address and account details for the registration.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4969 May 2026
```

## File page 4970

```text
PrimaryOwner <PmryOwnr> contains the following elements (see
"InvestmentAccountOwnershipInformation17" on page 4575 for details)
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4970 May 2026
```

