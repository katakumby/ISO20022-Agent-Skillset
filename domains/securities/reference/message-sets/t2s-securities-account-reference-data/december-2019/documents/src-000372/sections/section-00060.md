---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "9.4 Message Building Blocks", "9.4.2 SearchCriteria <SchCrit>", "9.4.2.2 DatePeriod <DtPrd>"]
file_pages: [66]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 9.4.2.2 DatePeriod <DtPrd>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 66 to 66.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 79
   Type <Tp> [0..1] ± 79
   Name <Nm> [0..1] Text 79
9.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specifies the period for querying information.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 66
Or   ToDate <ToDt> [1..1] Date 66
Or   FromToDate <FrToDt> [1..1] ± 66
Or   EqualDate <EQDt> [1..1] Date 67
Or}   NotEqualDate <NEQDt> [1..1] Date 67
9.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 97
9.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 97
9.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 80
   ToDate <ToDt> [1..1] Date 80
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities - Securities Account Reference Data 66 December 2019
```

