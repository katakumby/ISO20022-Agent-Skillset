---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.37 Report Parameter", "66.1.37.1 FrequencyCodeAndDSSCode1Choice", "66.1.37.1.2 FrequencyAsDSS <FrqcyAsDSS>"]
file_pages: [5130]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.37.1.2 FrequencyAsDSS <FrqcyAsDSS>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5130 to 5130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5130

```text
CodeName Name Definition
ADHO Adhoc Event takes place as necessary.
INDA IntraDay Event takes place several times a day.
OVNG Overnight Event takes place overnight.
ONDE OnDemand Event takes place on demand.
66.1.37.1.2  FrequencyAsDSS <FrqcyAsDSS>
Presence: [1..1]
Definition: Frequency expressed as a data source scheme and a code used within the data source
scheme.
FrequencyAsDSS <FrqcyAsDSS> contains the following elements (see "GenericIdentification7" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4539
   Information <Inf> [1..1] Text 4539
66.1.37.2  DataFormat2Choice
Definition: Choice between the specification of the data in a structured or unstructured form.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Structured <Strd> [1..1] ± 5130
Or}   Unstructured <Ustrd> [1..1] Text 5130
66.1.37.2.1  Structured <Strd>
Presence: [1..1]
Definition: Specification of data in a structured form.
Structured <Strd> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.37.2.2  Unstructured <Ustrd>
Presence: [1..1]
Definition: Specification of data for which there isn't a structured form.
Datatype: "Max140Text" on page 5402
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5130 May 2026
```

