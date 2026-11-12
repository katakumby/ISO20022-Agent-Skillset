---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.1 Party <Pty>"]
file_pages: [4577]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.1 Party <Pty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4577 to 4577.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4577

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
66.1.24.4.1  Party <Pty>
Presence: [1..1]
Definition: Information about the organisation or individual person.
Party <Pty> contains one of the following Party48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Organisation <Org> [1..1] ± C20 4577
Or}   IndividualPerson <IndvPrsn> [1..1] ± 4578
66.1.24.4.1.1  Organisation <Org>
Presence: [1..1]
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Impacted by: C20 "OrganisationElementRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4577 May 2026
```

