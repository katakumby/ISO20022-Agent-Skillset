---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.5 SettlementTransactionCondition <SttlmTxCond>"]
file_pages: [576]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.5 SettlementTransactionCondition <SttlmTxCond>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 576 to 576.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 576

```text
7.1.27.1.5  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition31Choice" on page 605 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 605
Or}   Proprietary <Prtry> [1..1] ± 606
7.1.27.1.6  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.27.1.7  BeneficialOwnership <BnfclOwnrsh>
Presence: [0..1]
Definition: Specifies whether there is change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 356 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 357
Or}   Proprietary <Prtry> [1..1] ± 357
7.1.27.1.8  BlockTrade <BlckTrad>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is a block parent or child.
BlockTrade <BlckTrad> contains one of the following elements (see "BlockTrade4Choice" on
page 331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 331
Or}   Proprietary <Prtry> [1..1] ± 331
7.1.27.1.9  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 576 February 2025
```

