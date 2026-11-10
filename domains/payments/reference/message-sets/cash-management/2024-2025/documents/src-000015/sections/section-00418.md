---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.4 Message Building Blocks", "20.4.2 ReportOrError <RptOrErr>", "20.4.2.1 OperationalError <OprlErr>", "20.4.2.1.1 Error <Err>"]
file_pages: [572]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.4.2.1.1 Error <Err>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 572 to 572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 572

```text
20.4.2.1.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 572
Or}   Proprietary <Prtry> [1..1] Text 572
20.4.2.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 857
20.4.2.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 889
20.4.2.1.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
20.4.2.2  BusinessReport <BizRpt>
Presence: [1..*]
Definition: Reports either on the business information or on a business error.
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 572 February 2025
```

