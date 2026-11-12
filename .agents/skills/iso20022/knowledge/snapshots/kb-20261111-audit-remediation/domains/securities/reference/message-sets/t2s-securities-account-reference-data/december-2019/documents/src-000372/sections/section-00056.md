---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["8 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "8.4 Message Building Blocks", "8.4.3 SecuritiesAccountActivity <SctiesAcctActvty>", "8.4.3.2 Change <Chng>", "8.4.3.2.1 SecuritiesAccountIdentification <SctiesAcctId>"]
file_pages: [62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 8.4.3.2.1 SecuritiesAccountIdentification <SctiesAcctId>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 62 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 62

```text
Change <Chng> contains the following SecuritiesAccountReferenceDataChange2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 62
   FieldName <FldNm> [1..1] Text 62
   OldFieldValue <OdFldVal> [1..1] Text 62
   NewFieldValue <NewFldVal> [1..1] Text 62
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 62
8.4.3.2.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Identifies the securities account for which the changes are listed in the advice.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 79
   Type <Tp> [0..1] ± 79
   Name <Nm> [0..1] Text 79
8.4.3.2.2  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the element, as specified in the short tag name for the field in the message.
Datatype: "Max35Text" on page 100
8.4.3.2.3  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the related field before the change was applied.
Datatype: "Max350Text" on page 100
8.4.3.2.4  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the related field after the change was applied.
Datatype: "Max350Text" on page 100
8.4.3.2.5  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Specifies the timestamp of the operation.
Datatype: "ISODateTime" on page 97
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities - Securities Account Reference Data 62 December 2019
```

