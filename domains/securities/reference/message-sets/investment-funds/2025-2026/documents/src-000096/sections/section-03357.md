---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.1 Party <Pty>"]
file_pages: [4599]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.1 Party <Pty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4599 to 4599.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4599

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
66.1.24.7.1  Party <Pty>
Presence: [1..1]
Definition: Information about the organisation or individual person.
Party <Pty> contains one of the following Party47Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Organisation <Org> [1..1] ± C24 4599
Or}   IndividualPerson <IndvPrsn> [1..1] ± 4600
66.1.24.7.1.1  Organisation <Org>
Presence: [1..1]
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Impacted by: C24 "OrganisationElementRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4599 May 2026
```

