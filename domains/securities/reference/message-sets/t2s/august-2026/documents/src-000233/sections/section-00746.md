---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.20 Issuance <Issnc>", "28.4.2.1.1.2.20.6 IssuerOrganisation <IssrOrg>", "28.4.2.1.1.2.20.6.1 Name <Nm>"]
file_pages: [1127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.20.6.1 Name <Nm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1127 to 1127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1127

```text
IssuerOrganisation <IssrOrg> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1127
   Identification <Id> [0..1]  1127
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1127
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1128
   Purpose <Purp> [0..1] Text 1128
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1128
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1128
   RegistrationDate <RegnDt> [0..1] Date 1129
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 1129
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1129
   PostalAddress <PstlAdr> [1..5] ± C10 1129
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1129
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1130
28.4.2.1.1.2.20.6.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
28.4.2.1.1.2.20.6.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1127
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1128
28.4.2.1.1.2.20.6.2.1  AnyBIC <AnyBIC>
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
Target2-Securities 1127 August 2026
```

