---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.5 BorrowedBalance <BrrwdBal>"]
file_pages: [807]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.5 BorrowedBalance <BrrwdBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 807 to 807.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 807

```text
14.4.3.5.3.5  BorrowedBalance <BrrwdBal>
Presence: [0..1]
Definition: Balance of financial instruments that have been borrowed from another party.
BorrowedBalance <BrrwdBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.6  CollateralInBalance <CollInBal>
Presence: [0..1]
Definition: Balance of securities that belong to a third party and that are held for the purpose of
collateralisation.
CollateralInBalance <CollInBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.7  CollateralOutBalance <CollOutBal>
Presence: [0..1]
Definition: Balance of securities that belong to the safekeeping account indicated within this message,
and are deposited with a third party for the purpose of collateralisation.
CollateralOutBalance <CollOutBal> contains the following elements (see "SignedQuantityFormat10"
on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.8  OnLoanBalance <OnLnBal>
Presence: [0..1]
Definition: Balance of financial instruments that have been loaned to a third party.
OnLoanBalance <OnLnBal> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 807 February 2026
```

