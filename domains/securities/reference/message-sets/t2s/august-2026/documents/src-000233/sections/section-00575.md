---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.1 SecurityStatus <SctySts>"]
file_pages: [759]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.1 SecurityStatus <SctySts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 759 to 759.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 759

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 819
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 819
   UnderlyingRisk <UndrlygRsk> [0..1]  820
     Name <Nm> [1..1] Text 820
     Identification <Id> [0..1]  821
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 821
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 821
     Purpose <Purp> [0..1] Text 821
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 822
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 822
     RegistrationDate <RegnDt> [0..1] Date 822
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 822
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 822
     PostalAddress <PstlAdr> [1..5] ± C10 822
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 823
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 823
27.4.2.3.1  SecurityStatus <SctySts>
Presence: [0..1]
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 759
Or}   Proprietary <Prtry> [1..1] ± 760
27.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Datatype: "SecurityStatus2Code" on page 3300
CodeName Name Definition
ACTV Active The status is active.
INAC Inactive The status is inactive.
SUSP Suspended The status is suspended.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 759 August 2026
```

