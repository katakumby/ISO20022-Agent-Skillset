---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.10 AccountParties17", "66.1.30.10.9 OtherParty <OthrPty>"]
file_pages: [4947, 4948]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.10.9 OtherParty <OthrPty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4947 to 4948.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4947

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CRSStatus <CRSSts> [0..*] ± 4608
   CRSReportingDate <CRSRptgDt> [0..1] Date 4609
   OtherIdentification <OthrId> [0..*] ± 4609
   TaxExemption <TaxXmptn> [0..1] ± 4610
   TaxReporting <TaxRptg> [0..*] ± 4610
   Language <Lang> [0..1] CodeSet C34 4611
   MailType <MailTp> [0..1] ± 4612
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 4612
   MonetaryWealth <MntryWlth> [0..1] ± 4612
   EquityValue <EqtyVal> [0..1] ± 4612
   WorkingCapital <WorkgCptl> [0..1] ± 4613
   CompanyLink <CpnyLk> [0..1] ± 4613
   ElectronicMailingServiceReference <ElctrncMlngSvcRef> [0..1] Text 4613
   PrimaryCommunicationAddress <PmryComAdr> [0..*] ± 4613
   SecondaryCommunicationAddress <ScndryComAdr> [0..*] ± 4614
   AdditionalRegulatoryInformation <AddtlRgltryInf> [0..1] ± 4614
   AccountingStatus <AcctgSts> [0..1] ± 4615
   AdditionalInformation <AddtlInf> [0..*] ± 4615
   ControllingParty <CtrlgPty> [0..1] Indicator 4616
66.1.30.10.9  OtherParty <OthrPty>
Presence: [0..*]
Definition: Other type of party.
OtherParty <OthrPty> contains the following elements (see "ExtendedParty14" on page 4912 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExtendedPartyRole <XtndedPtyRole> [1..1] Text 4912
   OtherPartyDetails <OthrPtyDtls> [1..1] ± 4913
66.1.30.10.10  Granter <Grntr>
Presence: [0..*]
Definition: Granter role in the hedge funds industry.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4947 May 2026
```

## File page 4948

```text
Granter <Grntr> contains the following elements (see "InvestmentAccountOwnershipInformation16" on
page 4597 for details)
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
Investment Funds - Maintenance 2025 - 2026 4948 May 2026
```

