---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.51 PayingAgent <PngAgt>"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.51 PayingAgent <PngAgt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress3" on page 491 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 491
   Phone <Phne> [0..1] Text 491
   Mobile <Mob> [0..1] Text 492
   FaxNumber <FaxNb> [0..1] Text 492
   TelexAddress <TlxAdr> [0..1] Text 492
   URLAddress <URLAdr> [0..1] Text 492
13.1.6.2.51  PayingAgent <PngAgt>
Presence: [0..1]
Definition: Additional party appointed to distribute payment or securities on behalf of the issuer.
PayingAgent <PngAgt> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 310
   Identification <Id> [0..1]  311
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 311
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 311
   Purpose <Purp> [0..1] Text 311
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 312
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 312
   RegistrationDate <RegnDt> [0..1] Date 312
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 312
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 312
   PostalAddress <PstlAdr> [1..5] ± C10 312
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 313
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 313
13.1.6.2.51.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 533
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 310 March 2024
```

