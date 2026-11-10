---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.37 ModificationScope21", "66.1.28.37.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [4880]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.37.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4880 to 4880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4880

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4880
   IssueAllocation <IsseAllcn> [1..1] ± 4880
66.1.28.37.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied on a set of information.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.28.37.2  IssueAllocation <IsseAllcn>
Presence: [1..1]
Definition: Information about the investment account ownership with respect to new issue allocation for
a hedge fund.
IssueAllocation <IsseAllcn> contains the following elements (see "NewIssueAllocation2" on
page 4819 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Restricted <Rstrctd> [1..1] Indicator 4819
   ExemptPersonReason <XmptPrsnRsn> [0..1] Text 4819
   DeMinimus <DeMnms> [0..1] ± 4819
66.1.28.38  BreakdownByCurrency2
Definition: Specifies the cash-in and cash-out flows by currency.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4880 May 2026
```

