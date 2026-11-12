---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.47 ContactName <CtctNm>"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.47 ContactName <CtctNm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
LegalForm <LglForm> contains one of the following elements (see "FormOfSecurity8Choice" on
page 482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 482
Or}   Proprietary <Prtry> [1..1] ± 482
13.1.6.4.47  ContactName <CtctNm>
Presence: [0..1]
Definition: Details (name, e-mail address and/or telephone number) of the person requesting the
allocation of the ISIN used as a point of reference in case further clarifications are required.
ContactName <CtctNm> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 450
   Identification <Id> [0..1]  450
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 451
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 451
   Purpose <Purp> [0..1] Text 451
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 451
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 452
   RegistrationDate <RegnDt> [0..1] Date 452
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 452
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 452
   PostalAddress <PstlAdr> [1..5] ± C10 452
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 453
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 453
13.1.6.4.47.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 533
13.1.6.4.47.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 450 March 2024
```

