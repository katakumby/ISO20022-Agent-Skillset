---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.39 InitialPhysicalForm <InitlPhysForm>", "28.4.2.1.1.2.39.1 Code <Cd>"]
file_pages: [1149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.39.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1149 to 1149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1149

```text
28.4.2.1.1.2.39.1  Code <Cd>
Presence: [1..1]
Definition: Initial physical form expressed as an ISO 20022 code.
Datatype: "InitialPhysicalForm1Code" on page 3255
CodeName Name Definition
GTGT GT Initial Physical Form is GT.
GPGP GP Initial Physical Form is GP.
DERN Definitive Initial Physical Form is definitive.
28.4.2.1.1.2.39.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Initial physical form expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.1.2.40  AfterExchangePhysicalForm <AftrXchgPhysForm>
Presence: [0..1]
Definition: Indicates the physical form of the securities after the exchange of the initial certificate issued
on the closing date.
AfterExchangePhysicalForm <AftrXchgPhysForm> contains one of the following
InitialPhysicalForm3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1149
Or}   Proprietary <Prtry> [1..1] ± 1150
28.4.2.1.1.2.40.1  Code <Cd>
Presence: [1..1]
Definition: Initial physical form expressed as an ISO 20022 code.
Datatype: "InitialPhysicalForm2Code" on page 3255
CodeName Name Definition
GPGP GP Initial Physical Form is GP.
DERN Definitive Initial Physical Form is definitive.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1149 August 2026
```

