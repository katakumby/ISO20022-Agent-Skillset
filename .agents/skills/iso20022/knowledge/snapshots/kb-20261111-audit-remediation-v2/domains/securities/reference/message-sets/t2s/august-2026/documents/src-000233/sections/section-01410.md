---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.49 PayingAgent <PngAgt>", "32.4.3.1.1.3.49.2 Identification <Id>", "32.4.3.1.1.3.49.2.2 ProprietaryIdentification <PrtryId>"]
file_pages: [2019]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.49.2.2 ProprietaryIdentification <PrtryId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2019 to 2019.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2019

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
32.4.3.1.1.3.49.2.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
32.4.3.1.1.3.49.3  Purpose <Purp>
Presence: [0..1]
Definition: Purpose of the organisation, eg, charity.
Datatype: "Max35Text" on page 3328
32.4.3.1.1.3.49.4  TaxationCountry <TaxtnCtry>
Presence: [0..1]
Definition: Country of taxation of an organisation.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
32.4.3.1.1.3.49.5  RegistrationCountry <RegnCtry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2019 August 2026
```

