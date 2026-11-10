---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["4 reda.038.001.01 CashAccountActivityAdviceV01", "4.4 Message Building Blocks", "4.4.2 CashAccountActivity <CshAcctActvty>", "4.4.2.2 Change <Chng>", "4.4.2.2.2 FieldName <FldNm>"]
file_pages: [111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.038.001.01"]
---

# 4.4.2.2.2 FieldName <FldNm>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 111 to 111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 111

```text
CashAccountIdentification <CshAcctId> contains the following elements (see "CashAccount40" on
page 130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 130
   Type <Tp> [0..1] ± 130
   Currency <Ccy> [0..1] CodeSet C2 131
   Name <Nm> [0..1] Text 131
   Proxy <Prxy> [0..1] ± 131
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
4.4.2.2.2  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the element, as specified in the short tag name for the field in the message.
Datatype: "Max35Text" on page 183
4.4.2.2.3  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the related field before the change was applied.
Datatype: "Max350Text" on page 183
4.4.2.2.4  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the related field after the change was applied.
Datatype: "Max350Text" on page 183
4.4.2.2.5  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Specifies the timestamp of the operation.
Datatype: "ISODateTime" on page 180
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.038.001.01 CashAccountActivityAdviceV01
Target2-Securities - Cash Account Query and Report 111 August 2026
```

