---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.3 SecuritiesMovementDetails <SctiesMvmntDtls>", "9.4.9.3.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [684]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.3.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 684 to 684.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 684

```text
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
9.4.9.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the value is a debit or credit.
Datatype: "CreditDebitCode" on page 1205
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
9.4.9.3.3  PostingQuantity <PstngQty>
Presence: [1..1]
Definition: Quantity of securities that have been posted (credit or debit) to the safekeeping account.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 684 February 2026
```

