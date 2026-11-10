---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.9 ModifiedIssueAllocation <ModfdIsseAllcn>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.9 ModifiedIssueAllocation <ModfdIsseAllcn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
4.4.9 ModifiedIssueAllocation <ModfdIsseAllcn>
Presence: [0..1]
Definition: Eligibility conditions related to allocation of new issues to be inserted, updated or deleted.
ModifiedIssueAllocation <ModfdIsseAllcn> contains the following elements (see
"ModificationScope21" on page 4879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4880
   IssueAllocation <IsseAllcn> [1..1] ± 4880
4.4.10 ModifiedSavingsInvestmentPlan
<ModfdSvgsInvstmtPlan>
Presence: [0..50]
Definition: Information related to a savings plan to be inserted, updated or deleted.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 71 May 2026
```

