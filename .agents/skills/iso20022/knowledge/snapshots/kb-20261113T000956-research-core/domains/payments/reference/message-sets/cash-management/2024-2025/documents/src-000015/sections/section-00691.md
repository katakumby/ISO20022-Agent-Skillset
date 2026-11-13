---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.50 QueryType2Code"]
file_pages: [872]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.50 QueryType2Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 872 to 872.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 872

```text
CodeName Name Definition
RSVT Reservation Restriction is the creation of a
reservation of a cash balance or a
securities position for a specific purpose.
BLCK Blocking Restriction is the blocking of a party,
securities account, security or cash
account from settlement, blocking of
securities position or cash balance for a
specific purpose.
EARM Earmarking Restriction of linked to the balance type
that defines and manages position types
for securities positions.
EFAC EarmarkingForAutoCollateralisation Restriction of linked to the balance type
that defines and manages position types
for securities positions for auto-
collateralisation.
DLVR Deliverable No restriction has been defined.
COLD Collateralised Restriction is linked to a sub-pledged
collateral transaction.
CSDB CoSDBlocking Restriction does not support any partial
execution.
37.2.2.50  QueryType2Code
Definition: Specifies the nature of the query, i.e. whether the query requests that all matching items be
returned or only new matching items since the last similar query be returned.
Type: CodeSet
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
DELD Deleted Specifies that the query requests that
items that have been deleted since the
last query be returned.
37.2.2.51  ReportIndicator1Code
Definition: Specifies the nature of the report, that is, standard or proprietary.
Type: CodeSet
CodeName Name Definition
STND Standard Requested report must contain
information in the format of a statement.
PRPR Proprietary Requested report must contain
information in a bilaterally agreed format.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 872 February 2025
```

