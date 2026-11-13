---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.2 BalanceForAccount <BalForAcct>", "82.1.5.16.2.8 NotAvailableBalance <NotAvlblBal>"]
file_pages: [2875]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.2.8 NotAvailableBalance <NotAvlblBal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2875 to 2875.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2875

```text
AvailableBalance <AvlblBal> contains the following elements (see "Balance8" on page 2863 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 2863
   Quantity <Qty> [1..1] ± 2863
82.1.5.16.2.8  NotAvailableBalance <NotAvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is not available.
NotAvailableBalance <NotAvlblBal> contains one of the following elements (see
"BalanceQuantity8Choice" on page 3027 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 3027
Or}   Proprietary <Prtry> [1..1] ± 3027
82.1.5.16.2.9  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are kept safe physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C33 "SafekeepingPlaceFormatOrLEIRule"
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace3" on
page 3113 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 3113
   LEI <LEI> [0..1] IdentifierSet 3114
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
82.1.5.16.2.10  CorporateActionOptionType <CorpActnOptnTp>
Presence: [0..1]
Definition: Specifies the corporate action options available to the account owner.
Datatype: "CorporateActionOption5Code" on page 3234
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2875 August 2026
```

