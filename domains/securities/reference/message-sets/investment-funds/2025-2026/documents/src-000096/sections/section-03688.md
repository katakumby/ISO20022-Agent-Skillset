---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.10 AccountParties17", "66.1.30.10.14 RegisteredShareholderName <RegdShrhldrNm>"]
file_pages: [4955]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.10.14 RegisteredShareholderName <RegdShrhldrNm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4955 to 4955.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4955

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
66.1.30.10.14  RegisteredShareholderName <RegdShrhldrNm>
Presence: [0..1]
Definition: Party that registers its name with the issuer and the name used for the registration.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4955 May 2026
```

