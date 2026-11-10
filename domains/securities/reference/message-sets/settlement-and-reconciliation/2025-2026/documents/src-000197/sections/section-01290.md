---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.22 Rate"]
file_pages: [1747]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.22 Rate

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1747 to 1747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1747

```text
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace5" on
page 1749 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 1749
   LEI <LEI> [0..1] IdentifierSet 1750
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
35.1.22 Rate
35.1.22.1  RateName1
Definition: Rate name specifies the reference rate or basis rate on which a variable rate is based (ex:
EONIA, EURIBOR, LIBOR, FEFUND, EURREPO).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 1747
   RateName <RateNm> [1..1] Text 1747
35.1.22.1.1  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max8Text" on page 2192
35.1.22.1.2  RateName <RateNm>
Presence: [1..1]
Definition: Rate Name specifies the reference rate or basis rate on which a variable rate is based (ex:
EONIA, EURIBOR, LIBOR, FEFUND, EURREPO).
Datatype: "Max35Text" on page 2192
35.1.22.2  RateType35Choice
Definition: Choice between a code and or a data source scheme to determine the rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1748
Or}   Proprietary <Prtry> [1..1] ± 1748
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1747 March 2026
```

