---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.48 ContactName <CtctNm>"]
file_pages: [298]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.48 ContactName <CtctNm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 298 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
LegalForm <LglForm> contains one of the following elements (see "FormOfSecurity8Choice" on
page 482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 482
Or}   Proprietary <Prtry> [1..1] ± 482
13.1.6.2.48  ContactName <CtctNm>
Presence: [0..1]
Definition: Details (name, e-mail address and/or telephone number) of the person requesting the
allocation of the ISIN used as a point of reference in case further clarifications are required.
ContactName <CtctNm> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 298
   Identification <Id> [0..1]  298
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 299
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 299
   Purpose <Purp> [0..1] Text 299
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 299
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 300
   RegistrationDate <RegnDt> [0..1] Date 300
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 300
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 300
   PostalAddress <PstlAdr> [1..5] ± C10 300
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 301
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 301
13.1.6.2.48.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 533
13.1.6.2.48.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 298 March 2024
```

