---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.3 SecuritiesMovementDetails <SctiesMvmntDtls>", "9.4.9.3.4 PostingDate <PstngDt>"]
file_pages: [685]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.3.4 PostingDate <PstngDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 685 to 685.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 685

```text
PostingQuantity <PstngQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
9.4.9.3.4  PostingDate <PstngDt>
Presence: [1..1]
Definition: Date of the posting (credit or debit) to the account.
PostingDate <PstngDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
9.4.9.3.5  OriginalPostingDate <OrgnlPstngDt>
Presence: [0..1]
Definition: Date/Time of the posting (credit or debit) to the account that was initially communicated in
the confirmation.
OriginalPostingDate <OrgnlPstngDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
9.4.9.4  CashMovementDetails <CshMvmntDtls>
Presence: [0..*]
Definition: Provides information about the cash movement related to a corporate action option.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 685 February 2026
```

