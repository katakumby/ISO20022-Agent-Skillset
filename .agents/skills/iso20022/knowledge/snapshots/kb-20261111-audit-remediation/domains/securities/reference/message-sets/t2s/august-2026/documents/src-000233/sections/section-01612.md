---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["55 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "55.4 Message Building Blocks", "55.4.3 SecuritiesAccountActivity <SctiesAcctActvty>", "55.4.3.2 Change <Chng>", "55.4.3.2.1 SecuritiesAccountIdentification <SctiesAcctId>"]
file_pages: [2239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 55.4.3.2.1 SecuritiesAccountIdentification <SctiesAcctId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2239 to 2239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2239

```text
Change <Chng> contains the following SecuritiesAccountReferenceDataChange2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 2239
   FieldName <FldNm> [1..1] Text 2239
   OldFieldValue <OdFldVal> [1..1] Text 2239
   NewFieldValue <NewFldVal> [1..1] Text 2239
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 2239
55.4.3.2.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Identifies the securities account for which the changes are listed in the advice.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
55.4.3.2.2  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the element, as specified in the short tag name for the field in the message.
Datatype: "Max35Text" on page 3328
55.4.3.2.3  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the related field before the change was applied.
Datatype: "Max350Text" on page 3328
55.4.3.2.4  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the related field after the change was applied.
Datatype: "Max350Text" on page 3328
55.4.3.2.5  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Specifies the timestamp of the operation.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities 2239 August 2026
```

