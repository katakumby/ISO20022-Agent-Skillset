---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.9 Text", "9.2.9.4 Exact5NumericText"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.9.4 Exact5NumericText

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
Format
pattern [0-9]{4}
9.2.9.4  Exact5NumericText
Definition: Specifies a numeric string with an exact length of 5 digits.
Type: Text
Format
pattern [0-9]{5}
9.2.9.5  ISO20022MessageIdentificationText
Definition: ISO 20022 Message identifier of an MX message.
Type: Text
Format
pattern [a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}
9.2.9.6  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
9.2.9.7  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
9.2.9.8  Max210Text
Definition: Specifies a character string with a maximum length of 210 characters.
Type: Text
Format
minLength 1
maxLength 210
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 344 September 2025
```

