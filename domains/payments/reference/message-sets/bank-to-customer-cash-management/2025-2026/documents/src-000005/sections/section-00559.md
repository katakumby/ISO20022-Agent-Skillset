---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.4 Message Building Blocks", "5.4.2 ReportingRequest <RptgReq>", "5.4.2.6 ReportingPeriod <RptgPrd>", "5.4.2.6.1 FromToDate <FrToDt>", "5.4.2.6.1.1 FromDate <FrDt>"]
file_pages: [792]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.4.2.6.1.1 FromDate <FrDt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 792 to 792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 792

```text
FromToDate <FrToDt> contains the following DatePeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 792
   ToDate <ToDt> [0..1] Date 792
5.4.2.6.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 908
5.4.2.6.1.2  ToDate <ToDt>
Presence: [0..1]
Definition: End date of the range.
Datatype: "ISODate" on page 908
5.4.2.6.2  FromToTime <FrToTm>
Presence: [0..1]
Definition: Specifies a time range.
FromToTime <FrToTm> contains the following elements (see "TimePeriodDetails1" on page 827 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromTime <FrTm> [1..1] Time 827
   ToTime <ToTm> [0..1] Time 828
5.4.2.6.3  Type <Tp>
Presence: [1..1]
Definition: Specifies whether all matching items need to be reported or only those items that are new or
have changed since the last similar request was made.
Datatype: "QueryType3Code" on page 904
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
792 March 2026
```

