---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.1 SecurityStatus <SctySts>"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.1 SecurityStatus <SctySts>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 317
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 317
   UnderlyingRisk <UndrlygRsk> [0..1]  318
     Name <Nm> [1..1] Text 318
     Identification <Id> [0..1]  319
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 319
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 319
     Purpose <Purp> [0..1] Text 319
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 320
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 320
     RegistrationDate <RegnDt> [0..1] Date 320
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 320
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 320
     PostalAddress <PstlAdr> [1..5] ± C10 320
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 321
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 321
13.1.6.2.1  SecurityStatus <SctySts>
Presence: [0..1]
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 255
Or}   Proprietary <Prtry> [1..1] ± 256
13.1.6.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Datatype: "SecurityStatus2Code" on page 523
CodeName Name Definition
ACTV Active The status is active.
INAC Inactive The status is inactive.
SUSP Suspended The status is suspended.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 255 March 2024
```

