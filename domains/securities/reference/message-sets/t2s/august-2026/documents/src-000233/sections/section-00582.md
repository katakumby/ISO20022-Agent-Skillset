---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.20 Issuance <Issnc>", "27.4.2.3.20.6 IssuerOrganisation <IssrOrg>", "27.4.2.3.20.6.1 Name <Nm>"]
file_pages: [767]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.20.6.1 Name <Nm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 767 to 767.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 767

```text
IssuerOrganisation <IssrOrg> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 767
   Identification <Id> [0..1]  767
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 767
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 768
   Purpose <Purp> [0..1] Text 768
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 768
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 768
   RegistrationDate <RegnDt> [0..1] Date 769
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 769
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 769
   PostalAddress <PstlAdr> [1..5] ± C10 769
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 769
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 770
27.4.2.3.20.6.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
27.4.2.3.20.6.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 767
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 768
27.4.2.3.20.6.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 767 August 2026
```

