---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.4 SafekeepingPlace <SfkpgPlc>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.4 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
PriceDetails <PricDtls> contains the following elements (see "PriceInformation30" on page 1706 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1707
   ValueType <ValTp> [1..1] ± 1707
   Value <Val> [1..1] ± 1707
   SourceOfPrice <SrcOfPric> [0..1] ± C35 1707
   QuotationDate <QtnDt> [0..1] ± 1708
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
8.4.7.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C35 "SafekeepingPlaceFormatOrLEIRule"
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
8.4.7.5  OpeningBalance <OpngBal>
Presence: [0..1]
Definition: Opening balance for the statement period (first opening balance) or of this page
(intermediary opening balance).
Impacted by: C38 "ShortLongDefaultRule"
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 221 March 2026
```

