---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.15 OtherAmounts <OthrAmts>", "17.4.16.2 Quantity <Qty>"]
file_pages: [547]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.16.2 Quantity <Qty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 547 to 547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 547

```text
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
17.4.16.2  Quantity <Qty>
Presence: [1..1]
Definition: Choice between different quantities related to the payment in digital asset.
Quantity <Qty> contains one of the following Quantity83Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 547
Or}   NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 547
17.4.16.2.1  ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>
Presence: [1..1]
Definition: Quantity of E-money token for the settlement payment.
Datatype: "Max30DecimalNumber" on page 2189
17.4.16.2.2  NetworkFeeQuantity <NtwkFeeQty>
Presence: [1..1]
Definition: Quantity of digital assets for network fee assigned to a transaction on a DLT network.
Datatype: "Max30DecimalNumber" on page 2189
17.4.16.3  CashSettlementSystemPlace <CshSttlmSysPlc>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 547 March 2026
```

