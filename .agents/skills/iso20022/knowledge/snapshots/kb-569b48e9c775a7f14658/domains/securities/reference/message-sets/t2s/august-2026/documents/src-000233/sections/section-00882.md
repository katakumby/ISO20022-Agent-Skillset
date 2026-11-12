---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.2.2.1 SecurityStatus <SctySts>"]
file_pages: [1307]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.2.1 SecurityStatus <SctySts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1307 to 1307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1307

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1368
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1368
     PostalAddress <PstlAdr> [1..5] ± C10 1368
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1369
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1369
   UnderlyingRisk <UndrlygRsk> [0..1]  1370
     Name <Nm> [1..1] Text 1370
     Identification <Id> [0..1]  1371
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1371
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1371
     Purpose <Purp> [0..1] Text 1371
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1372
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1372
     RegistrationDate <RegnDt> [0..1] Date 1372
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1372
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1372
     PostalAddress <PstlAdr> [1..5] ± C10 1372
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1373
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1373
28.4.2.1.2.2.1  SecurityStatus <SctySts>
Presence: [0..1]
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1307
Or}   Proprietary <Prtry> [1..1] ± 1308
28.4.2.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Datatype: "SecurityStatus2Code" on page 3300
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1307 August 2026
```

