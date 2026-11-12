---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["5 reda.009.001.01 SecurityActivityAdviceV01", "5.4 Message Building Blocks", "5.4.3 SecurityActivity <SctyActvty>", "5.4.3.2 Change <Chng>", "5.4.3.2.2 FieldName <FldNm>"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 5.4.3.2.2 FieldName <FldNm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

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
5.4.3.2.2  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the element, as specified in the short tag name for the field in the message.
Datatype: "Max35Text" on page 534
5.4.3.2.3  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the related field before the change was applied.
Datatype: "Max350Text" on page 534
5.4.3.2.4  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the related field after the change was applied.
Datatype: "Max350Text" on page 534
5.4.3.2.5  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Specifies the timestamp of the operation.
Datatype: "ISODateTime" on page 529
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities - Securities Reference Data 75 March 2024
```

