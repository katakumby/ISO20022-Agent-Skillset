---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.2 Warrant <Warrt>", "28.4.2.1.3.1.2.4 WarrantAgent <WarrtAgt>", "28.4.2.1.3.1.2.4.1 Name <Nm>"]
file_pages: [1406]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.2.4.1 Name <Nm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1406 to 1406.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1406

```text
WarrantAgent <WarrtAgt> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1406
   Identification <Id> [0..1]  1406
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1406
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1407
   Purpose <Purp> [0..1] Text 1407
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1407
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1407
   RegistrationDate <RegnDt> [0..1] Date 1408
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 1408
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1408
   PostalAddress <PstlAdr> [1..5] ± C10 1408
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1408
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1409
28.4.2.1.3.1.2.4.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
28.4.2.1.3.1.2.4.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1406
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1407
28.4.2.1.3.1.2.4.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1406 August 2026
```

