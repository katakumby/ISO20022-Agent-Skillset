---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.39 InitialPhysicalForm <InitlPhysForm>", "13.1.6.2.39.1 Code <Cd>"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.39.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
13.1.6.2.39.1  Code <Cd>
Presence: [1..1]
Definition: Initial physical form expressed as an ISO 20022 code.
Datatype: "InitialPhysicalForm1Code" on page 516
CodeName Name Definition
GTGT GT Initial Physical Form is GT.
GPGP GP Initial Physical Form is GP.
DERN Definitive Initial Physical Form is definitive.
13.1.6.2.39.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Initial physical form expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.2.40  AfterExchangePhysicalForm <AftrXchgPhysForm>
Presence: [0..1]
Definition: Indicates the physical form of the securities after the exchange of the initial certificate issued
on the closing date.
AfterExchangePhysicalForm <AftrXchgPhysForm> contains one of the following
InitialPhysicalForm3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 285
Or}   Proprietary <Prtry> [1..1] ± 286
13.1.6.2.40.1  Code <Cd>
Presence: [1..1]
Definition: Initial physical form expressed as an ISO 20022 code.
Datatype: "InitialPhysicalForm2Code" on page 516
CodeName Name Definition
GPGP GP Initial Physical Form is GP.
DERN Definitive Initial Physical Form is definitive.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 285 March 2024
```

