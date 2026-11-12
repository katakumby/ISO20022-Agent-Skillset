---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.7 TransactionDetails <TxDtls>", "33.4.7.2 SecuritiesMovementType <SctiesMvmntTp>"]
file_pages: [1314]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.7.2 SecuritiesMovementType <SctiesMvmntTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1314 to 1314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1314

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
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
33.4.7.2  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1314 March 2026
```

