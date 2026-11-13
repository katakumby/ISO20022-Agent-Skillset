---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.50 PrincipalPayingAgent <PrncplPngAgt>"]
file_pages: [1546]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.50 PrincipalPayingAgent <PrncplPngAgt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1546 to 1546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1546

```text
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress3" on page 3100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
28.4.2.1.3.2.50  PrincipalPayingAgent <PrncplPngAgt>
Presence: [0..1]
Definition: Main party appointed to distribute payment or securities on behalf of the issuer.
PrincipalPayingAgent <PrncplPngAgt> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1546
   Identification <Id> [0..1]  1547
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1547
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1547
   Purpose <Purp> [0..1] Text 1547
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1548
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1548
   RegistrationDate <RegnDt> [0..1] Date 1548
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 1548
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1548
   PostalAddress <PstlAdr> [1..5] ± C10 1548
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1549
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1549
28.4.2.1.3.2.50.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1546 August 2026
```

