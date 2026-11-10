---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.35 OptionFeaturesFormat25Choice", "16.1.15.35.1 Code <Cd>"]
file_pages: [943]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.35.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 943 to 943.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 943

```text
16.1.15.35.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the features that may apply to a corporate action option.
Datatype: "OptionFeatures12Code" on page 1224
CodeName Name Definition
OPLF OddLotPreference Tender or exchange with the odd lot
preference.
16.1.15.35.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the features that may apply to a corporate action option.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.36  RenounceableEntitlementStatusTypeFormat3Choice
Definition: Choice between a standard code or proprietary code to specify the type of the renounceable
entitlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 943
Or}   Proprietary <Prtry> [1..1] ± 943
16.1.15.36.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the renounceable status.
Datatype: "RenounceableStatus1Code" on page 1240
CodeName Name Definition
NREN NonRenounceable Intermediate securities cannot be sold.
RENO Renounceable Intermediate securities can be sold.
16.1.15.36.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the renounceable status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 943 February 2026
```

