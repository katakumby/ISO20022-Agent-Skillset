---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.9 ModificationScope43", "66.1.30.9.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [4924]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.9.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4924 to 4924.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4924

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4924
   Placement <Plcmnt> [1..1] ± C30 4924
66.1.30.9.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.30.9.2  Placement <Plcmnt>
Presence: [1..1]
Definition: Referral information.
Impacted by: C30 "ReferredPlacementAgentRule"
Placement <Plcmnt> contains the following elements (see "ReferredAgent3" on page 5027 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Referred <Rfrd> [1..1] CodeSet 5027
   ReferredPlacementAgent <RfrdPlcmntAgt> [0..1] ± 5027
Constraints
• ReferredPlacementAgentRule
ReferredPlacementAgent may only be present if Referred is REFR (Referred).
66.1.30.10  AccountParties17
Definition: Information about a party's account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4924 May 2026
```

