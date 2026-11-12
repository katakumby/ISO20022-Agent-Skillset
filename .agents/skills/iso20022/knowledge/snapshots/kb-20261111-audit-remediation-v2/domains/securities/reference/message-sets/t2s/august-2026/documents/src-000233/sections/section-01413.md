---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.50 Depository <Dpstry>", "32.4.3.1.1.3.50.1 Name <Nm>"]
file_pages: [2022]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.50.1 Name <Nm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2022 to 2022.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2022

```text
Depository <Dpstry> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 2022
   Identification <Id> [0..1]  2022
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2022
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 2023
   Purpose <Purp> [0..1] Text 2023
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2023
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2023
   RegistrationDate <RegnDt> [0..1] Date 2024
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 2024
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2024
   PostalAddress <PstlAdr> [1..5] ± C10 2024
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2024
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 2025
32.4.3.1.1.3.50.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
32.4.3.1.1.3.50.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2022
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 2023
32.4.3.1.1.3.50.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2022 August 2026
```

