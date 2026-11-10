---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.23 BorrowingReason <BrrwgRsn>"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.23 BorrowingReason <BrrwgRsn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
Definition: Indicates if the contract is with or without an exchange of collateral.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.49.23  BorrowingReason <BrrwgRsn>
Presence: [0..1]
Definition: Identifies the underlying reason for the borrowing, for instance, sale on my behalf or on
behalf of a third party.
BorrowingReason <BrrwgRsn> contains one of the following elements (see
"BorrowingReason2Choice" on page 585 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 585
Or}   Proprietary <Prtry> [1..1] ± 586
7.1.19.49.24  CollateralType <CollTp>
Presence: [0..1]
Definition: Indicates the type of collateral, for insatnce, security, bond, etc.
CollateralType <CollTp> contains one of the following elements (see "CollateralType4Choice" on
page 249 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 249
Or}   Proprietary <Prtry> [1..1] ± 249
7.1.19.49.25  ContractTermsModificationChanged <CtrctTermsModChngd>
Presence: [0..1]
Definition: Indicates whether or not the contract terms changed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.49.26  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Interest rate to be paid as agreed between the counterparties.
Impacted by: C48 "SignRule"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 366 February 2025
```

