---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.5 Balance", "37.1.5.1 CashBalance13", "37.1.5.1.8 RestrictionType <RstrctnTp>", "37.1.5.1.8.3 ProcessingType <PrcgTp>", "37.1.5.1.8.3.2 Proprietary <Prtry>"]
file_pages: [800]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.5.1.8.3.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 800 to 800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 800

```text
CodeName Name Definition
EFAC EarmarkingForAutoCollateralisation Restriction of linked to the balance type
that defines and manages position types
for securities positions for auto-
collateralisation.
DLVR Deliverable No restriction has been defined.
COLD Collateralised Restriction is linked to a sub-pledged
collateral transaction.
CSDB CoSDBlocking Restriction does not support any partial
execution.
37.1.5.1.8.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of processing restrictions, in a proprietary form.
Datatype: "Max35Text" on page 889
37.1.6 Date Period
37.1.6.1  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 800
   ToDate <ToDt> [1..1] Date 800
37.1.6.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 883
37.1.6.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 883
37.1.7 Date Time
37.1.7.1  Period2
Definition: Time span defined by a start date and time, and an end date and time.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 800 February 2025
```

