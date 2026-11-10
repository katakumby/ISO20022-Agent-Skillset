---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.22 Rate", "35.1.22.3 Rate2", "35.1.22.3.2 Rate <Rate>"]
file_pages: [1749]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.22.3.2 Rate <Rate>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1749 to 1749.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1749

```text
35.1.22.3.2  Rate <Rate>
Presence: [1..1]
Definition: Percentage charged for the use of an amount of money, usually expressed at an annual rate.
The interest rate is the ratio of the amount of interest paid during a certain period of time compared to
the principal amount of the interest bearing financial instrument.
Datatype: "PercentageRate" on page 2190
35.1.23 Safekeeping Place
35.1.23.1  SafeKeepingPlace5
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
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
35.1.23.1.1  SafekeepingPlaceFormat <SfkpgPlcFrmt>
Presence: [0..1]
Definition: Unique identification of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1749 March 2026
```

