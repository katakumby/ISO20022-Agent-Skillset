---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.18 Issuance <Issnc>", "13.1.6.3.18.1 IssuePlace <IssePlc>"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.18.1 IssuePlace <IssePlc>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
Issuance <Issnc> contains the following Issuance6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 337
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 338
   IssueDate <IsseDt> [0..1] Date 338
   AnnouncementDate <AnncmntDt> [0..1] DateTime 338
   IssuerOrganisation <IssrOrg> [0..1]  338
     Name <Nm> [1..1] Text 339
     Identification <Id> [0..1]  339
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 339
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 340
     Purpose <Purp> [0..1] Text 340
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 340
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 340
     RegistrationDate <RegnDt> [0..1] Date 341
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 341
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 341
     PostalAddress <PstlAdr> [1..5] ± C10 341
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 341
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 342
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 342
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 342
   IssueSize <IsseSz> [0..1] Quantity 343
   IssuePrice <IssePric> [0..1] ± 343
   IssuanceDistribution <IssncDstrbtn> [0..1]  343
{Or     Code <Cd> [1..1] CodeSet 344
Or}     Proprietary <Prtry> [1..1] ± 344
   GoverningLaw <GovngLaw> [0..*]  344
     Identification <Id> [0..1] Text 344
     Country <Ctry> [0..1] CodeSet C4 344
13.1.6.3.18.1  IssuePlace <IssePlc>
Presence: [0..1]
Definition: Indicates where the financial instrument was issued.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 337 March 2024
```

