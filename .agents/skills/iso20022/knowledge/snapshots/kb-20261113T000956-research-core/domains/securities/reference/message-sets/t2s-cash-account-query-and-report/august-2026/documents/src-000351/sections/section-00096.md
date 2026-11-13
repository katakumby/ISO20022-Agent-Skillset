---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["4 reda.038.001.01 CashAccountActivityAdviceV01", "4.4 Message Building Blocks", "4.4.2 CashAccountActivity <CshAcctActvty>", "4.4.2.1 SystemDate <SysDt>"]
file_pages: [110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.038.001.01"]
---

# 4.4.2.1 SystemDate <SysDt>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 110 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 110

```text
CashAccountActivity <CshAcctActvty> contains the following CashAccountStatement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDate <SysDt> [1..1] Date 110
   Change <Chng> [0..*]  110
     CashAccountIdentification <CshAcctId> [1..1] ± C4, C3 110
     FieldName <FldNm> [1..1] Text 111
     OldFieldValue <OdFldVal> [1..1] Text 111
     NewFieldValue <NewFldVal> [1..1] Text 111
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 111
4.4.2.1  SystemDate <SysDt>
Presence: [1..1]
Definition: Date for which the statement is valid.
Datatype: "ISODate" on page 179
4.4.2.2  Change <Chng>
Presence: [0..*]
Definition: Provides information on the actual change occurred to the cash account.
Change <Chng> contains the following CashAccountReferenceDataChange3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountIdentification <CshAcctId> [1..1] ± C4, C3 110
   FieldName <FldNm> [1..1] Text 111
   OldFieldValue <OdFldVal> [1..1] Text 111
   NewFieldValue <NewFldVal> [1..1] Text 111
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 111
4.4.2.2.1  CashAccountIdentification <CshAcctId>
Presence: [1..1]
Definition: Identifies the cash account for which the changes are listed in the advice.
Impacted by: C4 "IdentificationOrProxyPresenceRule", C3 "IdentificationAndProxyGuideline"
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.038.001.01 CashAccountActivityAdviceV01
Target2-Securities - Cash Account Query and Report 110 August 2026
```

