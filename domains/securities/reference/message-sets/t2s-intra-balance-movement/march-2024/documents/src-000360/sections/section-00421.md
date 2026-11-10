---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.2 Message Datatypes", "17.2.8 Text", "17.2.8.4 Exact5NumericText"]
file_pages: [496]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.2.8.4 Exact5NumericText

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 496 to 496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 496

```text
Type: Text
Format
pattern [0-9]{4}
17.2.8.4  Exact5NumericText
Definition: Specifies a numeric string with an exact length of 5 digits.
Type: Text
Format
pattern [0-9]{5}
17.2.8.5  ISO20022MessageIdentificationText
Definition: ISO 20022 Message identifier of an MX message.
Type: Text
Format
pattern [a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}
17.2.8.6  Max140Text
Definition: Specifies a character string with a maximum length of 140 characters.
Type: Text
Format
minLength 1
maxLength 140
17.2.8.7  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
17.2.8.8  Max2048Text
Definition: Specifies a character string with a maximum length of 2048 characters.
Type: Text
Format
minLength 1
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
496 March 2024
```

