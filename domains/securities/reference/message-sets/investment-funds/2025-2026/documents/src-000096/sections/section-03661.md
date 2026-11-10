---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.4 ExtendedParty14"]
file_pages: [4912]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.4 ExtendedParty14

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4912 to 4912.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4912

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FATCAReportingDate <FATCARptgDt> [0..1] Date 4587
   CRSFormType <CRSFormTp> [0..*] ± 4587
   CRSStatus <CRSSts> [0..*] ± 4587
   CRSReportingDate <CRSRptgDt> [0..1] Date 4588
   OtherIdentification <OthrId> [0..*] ± 4588
   TaxExemption <TaxXmptn> [0..1] ± 4589
   TaxReporting <TaxRptg> [0..*] ± 4589
   Language <Lang> [0..1] CodeSet C34 4590
   MailType <MailTp> [0..1] ± 4591
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 4591
   MonetaryWealth <MntryWlth> [0..1] ± 4591
   EquityValue <EqtyVal> [0..1] ± 4591
   WorkingCapital <WorkgCptl> [0..1] ± 4592
   CompanyLink <CpnyLk> [0..1] ± 4592
   ElectronicMailingServiceReference <ElctrncMlngSvcRef> [0..1] Text 4592
   PrimaryCommunicationAddress <PmryComAdr> [0..*] ± 4592
   SecondaryCommunicationAddress <ScndryComAdr> [0..*] ± 4593
   AdditionalRegulatoryInformation <AddtlRgltryInf> [0..1] ± 4593
   AccountingStatus <AcctgSts> [0..1] ± 4594
   AdditionalInformation <AddtlInf> [0..*] ± 4594
   ControllingParty <CtrlgPty> [0..1] Indicator 4595
66.1.30.4  ExtendedParty14
Definition: Party and account information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExtendedPartyRole <XtndedPtyRole> [1..1] Text 4912
   OtherPartyDetails <OthrPtyDtls> [1..1] ± 4913
66.1.30.4.1  ExtendedPartyRole <XtndedPtyRole>
Presence: [1..1]
Definition: Other type of party's role.
Datatype: "Extended350Code" on page 5402
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4912 May 2026
```

