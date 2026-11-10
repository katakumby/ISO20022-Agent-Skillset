---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.46 ContactName <CtctNm>", "32.4.3.1.1.3.46.1 Name <Nm>"]
file_pages: [2006]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.46.1 Name <Nm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2006 to 2006.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2006

```text
ContactName <CtctNm> contains the following Organisation38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 2006
   Identification <Id> [0..1]  2006
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2006
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 2007
   Purpose <Purp> [0..1] Text 2007
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 2007
   RegistrationCountry <RegnCtry> [0..1] CodeSet C4 2007
   RegistrationDate <RegnDt> [0..1] Date 2008
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 2008
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 2008
   PostalAddress <PstlAdr> [1..5] ± C10 2008
   PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 2008
   SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 2009
32.4.3.1.1.3.46.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 3326
32.4.3.1.1.3.46.2  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 2006
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 2007
32.4.3.1.1.3.46.2.1  AnyBIC <AnyBIC>
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
Target2-Securities 2006 August 2026
```

