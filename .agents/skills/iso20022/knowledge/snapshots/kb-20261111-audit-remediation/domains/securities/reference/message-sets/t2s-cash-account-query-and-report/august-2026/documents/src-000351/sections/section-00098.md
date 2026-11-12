---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["4 reda.038.001.01 CashAccountActivityAdviceV01", "4.4 Message Building Blocks", "4.4.3 SupplementaryData <SplmtryData>"]
file_pages: [112]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.038.001.01"]
---

# 4.4.3 SupplementaryData <SplmtryData>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 112 to 112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 112

```text
4.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C5 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 147 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 147
   Envelope <Envlp> [1..1] (External Schema) 147
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.038.001.01 CashAccountActivityAdviceV01
Target2-Securities - Cash Account Query and Report 112 August 2026
```

