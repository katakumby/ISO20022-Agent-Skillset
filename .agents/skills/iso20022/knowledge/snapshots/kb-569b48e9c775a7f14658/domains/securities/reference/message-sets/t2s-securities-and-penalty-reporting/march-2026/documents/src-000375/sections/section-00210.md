---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.2 BalanceForAccount <BalForAcct>", "7.1.5.14.2.8 NotAvailableBalance <NotAvlblBal>"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.2.8 NotAvailableBalance <NotAvlblBal>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
AvailableBalance <AvlblBal> contains the following elements (see "Balance8" on page 271 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 271
   Quantity <Qty> [1..1] ± 271
7.1.5.14.2.8  NotAvailableBalance <NotAvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is not available.
NotAvailableBalance <NotAvlblBal> contains one of the following elements (see
"BalanceQuantity8Choice" on page 387 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 387
Or}   Proprietary <Prtry> [1..1] ± 388
7.1.5.14.2.9  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are kept safe physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C33 "SafekeepingPlaceFormatOrLEIRule"
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace3" on
page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 453
   LEI <LEI> [0..1] IdentifierSet 453
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
7.1.5.14.2.10  CorporateActionOptionType <CorpActnOptnTp>
Presence: [0..1]
Definition: Specifies the corporate action options available to the account owner.
Datatype: "CorporateActionOption5Code" on page 501
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 283 March 2026
```

