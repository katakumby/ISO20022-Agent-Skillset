---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["30 reda.009.001.01 SecurityActivityAdviceV01", "30.4 Message Building Blocks", "30.4.3 SecurityActivity <SctyActvty>", "30.4.3.2 Change <Chng>", "30.4.3.2.2 FieldName <FldNm>"]
file_pages: [1762]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 30.4.3.2.2 FieldName <FldNm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1762 to 1762.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1762

```text
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
30.4.3.2.2  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the element, as specified in the short tag name for the field in the message.
Datatype: "Max35Text" on page 3328
30.4.3.2.3  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the related field before the change was applied.
Datatype: "Max350Text" on page 3328
30.4.3.2.4  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the related field after the change was applied.
Datatype: "Max350Text" on page 3328
30.4.3.2.5  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Specifies the timestamp of the operation.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities 1762 August 2026
```

