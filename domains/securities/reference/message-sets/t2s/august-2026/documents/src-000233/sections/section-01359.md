---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.18 Issuance <Issnc>", "32.4.3.1.1.3.18.1 IssuePlace <IssePlc>"]
file_pages: [1968]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.18.1 IssuePlace <IssePlc>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1968 to 1968.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1968

```text
Issuance <Issnc> contains the following Issuance6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 1968
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1969
   IssueDate <IsseDt> [0..1] Date 1969
   AnnouncementDate <AnncmntDt> [0..1] DateTime 1969
   IssuerOrganisation <IssrOrg> [0..1]  1969
     Name <Nm> [1..1] Text 1970
     Identification <Id> [0..1]  1970
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1970
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1971
     Purpose <Purp> [0..1] Text 1971
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1971
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1971
     RegistrationDate <RegnDt> [0..1] Date 1972
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1972
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1972
     PostalAddress <PstlAdr> [1..5] ± C10 1972
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1972
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1973
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1973
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1973
   IssueSize <IsseSz> [0..1] Quantity 1974
   IssuePrice <IssePric> [0..1] ± 1974
   IssuanceDistribution <IssncDstrbtn> [0..1]  1974
{Or     Code <Cd> [1..1] CodeSet 1975
Or}     Proprietary <Prtry> [1..1] ± 1975
   GoverningLaw <GovngLaw> [0..*]  1975
     Identification <Id> [0..1] Text 1975
     Country <Ctry> [0..1] CodeSet C4 1975
32.4.3.1.1.3.18.1  IssuePlace <IssePlc>
Presence: [0..1]
Definition: Indicates where the financial instrument was issued.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1968 August 2026
```

