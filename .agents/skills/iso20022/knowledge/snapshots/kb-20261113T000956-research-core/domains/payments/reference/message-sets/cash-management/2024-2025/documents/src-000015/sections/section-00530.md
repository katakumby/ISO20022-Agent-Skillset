---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.1 NewQueryName <NewQryNm>"]
file_pages: [695]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.1 NewQueryName <NewQryNm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 695 to 695.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 695

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ValidityFromIndicator <VldtyFrInd> [0..1] Indicator 704
     ValidToIndicator <VldToInd> [0..1] Indicator 704
     LinkSetIdentificationIndicator <LkSetIdInd> [0..1] Indicator 704
     LinkSetOrderIdentificationIndicator
<LkSetOrdrIdInd>
[0..1] Indicator 704
     LinkSetOrderSequenceIndicator <LkSetOrdrSeqInd> [0..1] Indicator 705
     TotalAmountIndicator <TtlAmtInd> [0..1] Indicator 705
     ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 705
Constraints
• ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present. If
ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
On Condition
    /ReturnCriteria is absent
Following Must be True
    /SearchCriteria[1] Must be present
30.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
30.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria to be used to extract the standing order information.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 695 February 2025
```

