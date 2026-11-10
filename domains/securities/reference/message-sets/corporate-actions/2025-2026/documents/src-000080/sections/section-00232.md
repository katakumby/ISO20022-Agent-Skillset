---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.12 SecuritiesQuantityOrInstructedAmount <SctiesQtyOrInstdAmt>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.12 SecuritiesQuantityOrInstructedAmount <SctiesQtyOrInstdAmt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
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
5.4.9.12  SecuritiesQuantityOrInstructedAmount <SctiesQtyOrInstdAmt>
Presence: [1..1]
Definition: Provides information about securities quantity linked to a corporate action option.
SecuritiesQuantityOrInstructedAmount <SctiesQtyOrInstdAmt> contains one of the following
SecuritiesQuantityOrAmount6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesQuantity <SctiesQty> [1..1]  309
     ConditionalQuantity <CondlQty> [0..1] ± C12 310
     InstructedQuantity <InstdQty> [1..1] ± 310
     AdditionalRoundUpQuantity <AddtlRndUpQty> [0..1] ± C12 310
Or}   InstructedAmount <InstdAmt> [1..1] Amount C1, C9 311
5.4.9.12.1  SecuritiesQuantity <SctiesQty>
Presence: [1..1]
Definition: Provides information about securities quantity linked to a corporate action option.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 309 February 2026
```

