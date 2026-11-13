---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.47 ContactName <CtctNm>"]
file_pages: [800]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.47 ContactName <CtctNm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 800 to 800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 800

```text
LegalForm <LglForm> contains one of the following elements (see "FormOfSecurity8Choice" on
page 3032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3032
Or}   Proprietary <Prtry> [1..1] ± 3032
27.4.2.3.47  ContactName <CtctNm>
Presence: [0..1]
Definition: Details (name, e-mail address and/or telephone number) of the person requesting the
allocation of the ISIN used as a point of reference in case further clarifications are required.
ContactName <CtctNm> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 800
   Identification <Id> [0..1]  800
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 801
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 801
   Purpose <Purp> [0..1] Text 801
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 801
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 802
   RegistrationDate <RegnDt> [0..1] Date 802
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 802
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 802
   PostalAddress <PstlAdr> [1..5] ± C10 802
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 803
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 803
27.4.2.3.47.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
27.4.2.3.47.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 800 August 2026
```

