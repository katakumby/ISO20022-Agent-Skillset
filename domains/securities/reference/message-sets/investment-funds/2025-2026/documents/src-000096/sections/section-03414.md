---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.37 ModifiedInvestorProfile <ModfdInvstrPrfl>"]
file_pages: [4660]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.37 ModifiedInvestorProfile <ModfdInvstrPrfl>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4660 to 4660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4660

```text
Definition: Specifies whether the investor assumes responsibility for the liability.
Liability <Lblty> contains one of the following elements (see "Liability1Choice" on page 4870 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4870
Or}   Proprietary <Prtry> [1..1] ± 4870
66.1.24.14.37  ModifiedInvestorProfile <ModfdInvstrPrfl>
Presence: [0..*]
Definition: Information related to the investor profile to be inserted, updated or deleted.
ModifiedInvestorProfile <ModfdInvstrPrfl> contains the following ModificationScope46 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4660
   InvestorProfile <InvstrPrfl> [1..1] ± 4660
66.1.24.14.37.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.24.14.37.2  InvestorProfile <InvstrPrfl>
Presence: [1..1]
Definition: Information used to determine fees and types of operations that can be carried out on the
account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4660 May 2026
```

