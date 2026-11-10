---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.12 TemporaryFinancialInstrumentIndicator3Choice"]
file_pages: [906]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.12 TemporaryFinancialInstrumentIndicator3Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 906 to 906.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 906

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.12  TemporaryFinancialInstrumentIndicator3Choice
Definition: Choice between an indicator or a proprietary code to specify whether the security is a
temporary security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TemporaryIndicator <TempInd> [1..1] Indicator 906
Or}   Proprietary <Prtry> [1..1] ± 906
16.1.15.12.1  TemporaryIndicator <TempInd>
Presence: [1..1]
Definition: Temporary financial instrument identification used for processing reasons.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
16.1.15.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary code to specify whether the security is a temporary security.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.13  RateTypeAndAmountAndStatus26
Definition: Specifies the value expressed as a rate and an amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 906 February 2026
```

