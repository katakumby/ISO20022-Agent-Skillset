---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.2 PartyIdentification125Choice", "66.1.30.2.3 NameAndAddress <NmAndAdr>"]
file_pages: [4910, 4911]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.2.3 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4910 to 4911.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4910

```text
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.30.2.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
66.1.30.3  ExtendedParty15
Definition: Other type of party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExtendedPartyRole <XtndedPtyRole> [1..1] Text 4910
   OtherPartyDetails <OthrPtyDtls> [1..1] ± 4910
66.1.30.3.1  ExtendedPartyRole <XtndedPtyRole>
Presence: [1..1]
Definition: Other type of party's role.
Datatype: "Extended350Code" on page 5402
66.1.30.3.2  OtherPartyDetails <OthrPtyDtls>
Presence: [1..1]
Definition: Detailed ownership information about a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4910 May 2026
```

## File page 4911

```text
OtherPartyDetails <OthrPtyDtls> contains the following elements (see
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
Investment Funds - Maintenance 2025 - 2026 4911 May 2026
```

