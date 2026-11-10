---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.2 SearchCriteria <SchCrit>", "30.4.2.2.2.2.6 ValidityPeriod <VldtyPrd>", "30.4.2.2.2.2.6.1 FromDate <FrDt>"]
file_pages: [699]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.2.6.1 FromDate <FrDt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 699 to 699.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 699

```text
ValidityPeriod <VldtyPrd> contains one of the following DatePeriod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 699
Or   ToDate <ToDt> [1..1] Date 699
Or}   FromToDate <FrToDt> [1..1] ± 699
30.4.2.2.2.2.6.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 883
30.4.2.2.2.2.6.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 883
30.4.2.2.2.2.6.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Range of time between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 800 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 800
   ToDate <ToDt> [1..1] Date 800
30.4.2.2.2.2.7  SystemMember <SysMmb>
Presence: [0..1]
Definition: Specifies if the account is debited or credited by the standing order.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 699 February 2025
```

