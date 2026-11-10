---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.1 SecurityStatus <SctySts>"]
file_pages: [1119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.1 SecurityStatus <SctySts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1119 to 1119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1119

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1180
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1180
     PostalAddress <PstlAdr> [1..5] ± C10 1180
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1181
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1181
   UnderlyingRisk <UndrlygRsk> [0..1]  1182
     Name <Nm> [1..1] Text 1182
     Identification <Id> [0..1]  1183
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1183
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1183
     Purpose <Purp> [0..1] Text 1183
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1184
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1184
     RegistrationDate <RegnDt> [0..1] Date 1184
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1184
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1184
     PostalAddress <PstlAdr> [1..5] ± C10 1184
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1185
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1185
28.4.2.1.1.2.1  SecurityStatus <SctySts>
Presence: [0..1]
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1119
Or}   Proprietary <Prtry> [1..1] ± 1120
28.4.2.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Datatype: "SecurityStatus2Code" on page 3300
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1119 August 2026
```

