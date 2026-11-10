---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.2.2.48 ContactName <CtctNm>"]
file_pages: [1350]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.2.48 ContactName <CtctNm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1350 to 1350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1350

```text
LegalForm <LglForm> contains one of the following elements (see "FormOfSecurity8Choice" on
page 3032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3032
Or}   Proprietary <Prtry> [1..1] ± 3032
28.4.2.1.2.2.48  ContactName <CtctNm>
Presence: [0..1]
Definition: Details (name, e-mail address and/or telephone number) of the person requesting the
allocation of the ISIN used as a point of reference in case further clarifications are required.
ContactName <CtctNm> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1350
   Identification <Id> [0..1]  1350
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1351
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1351
   Purpose <Purp> [0..1] Text 1351
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1351
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1352
   RegistrationDate <RegnDt> [0..1] Date 1352
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 1352
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1352
   PostalAddress <PstlAdr> [1..5] ± C10 1352
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1353
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1353
28.4.2.1.2.2.48.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
28.4.2.1.2.2.48.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1350 August 2026
```

