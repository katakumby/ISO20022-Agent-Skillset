---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.8 AdditionalInformation15"]
file_pages: [4508]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.8 AdditionalInformation15

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4508 to 4508.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4508

```text
66.1.18.8  AdditionalInformation15
Definition: Additional information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.18.8.1  InformationType <InfTp>
Presence: [1..1]
Definition: Type of additional information.
InformationType <InfTp> contains the following elements (see "GenericIdentification36" on page 4549
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.18.8.2  InformationValue <InfVal>
Presence: [1..1]
Definition: Value of the additional information.
Datatype: "Max350Text" on page 5403
66.1.18.9  GovernanceProcess1Choice
Definition: Choice of formats for a type of governance process.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4508
Or}   Proprietary <Prtry> [1..1] ± 4509
66.1.18.9.1  Code <Cd>
Presence: [1..1]
Definition: Type of governance process expressed as a code.
Datatype: "GovernanceProcessType1Code" on page 5309
CodeName Name Definition
BMIF ComparibleMiFID Product governance procedure is
comparable to MiFID II.
NINF NoInformation No information is requested from the
issuer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4508 May 2026
```

