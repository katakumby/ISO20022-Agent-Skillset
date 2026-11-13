---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.49 PayingAgent <PngAgt>", "13.1.6.3.49.1 Name <Nm>"]
file_pages: [387]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.49.1 Name <Nm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 387 to 387.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 387

```text
PayingAgent <PngAgt> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 387
   Identification <Id> [0..1]  387
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 387
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 388
   Purpose <Purp> [0..1] Text 388
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 388
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 388
   RegistrationDate <RegnDt> [0..1] Date 389
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 389
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 389
   PostalAddress <PstlAdr> [1..5] ± C10 389
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 389
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 390
13.1.6.3.49.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 533
13.1.6.3.49.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 387
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 388
13.1.6.3.49.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 530
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 387 March 2024
```

