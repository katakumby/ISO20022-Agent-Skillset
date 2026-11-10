---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.5 SettlementParameters <SttlmParams>", "72.4.3.4.18.5.5 PartialSettlementIndicator <PrtlSttlmInd>"]
file_pages: [2541]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.5.5 PartialSettlementIndicator <PrtlSttlmInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2541 to 2541.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2541

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition34Choice" on page 3000 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3000
Or}   Proprietary <Prtry> [1..1] ± 3002
72.4.3.4.18.5.5  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: "SettlementTransactionCondition5Code" on page 3302
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
72.4.3.4.18.5.6  BeneficialOwnership <BnfclOwnrsh>
Presence: [0..1]
Definition: Specifies whether there is change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 3030 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 3030
Or}   Proprietary <Prtry> [1..1] ± 3030
72.4.3.4.18.5.7  BlockTrade <BlckTrad>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is a block parent or child.
BlockTrade <BlckTrad> contains one of the following elements (see "BlockTrade4Choice" on
page 3018 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3018
Or}   Proprietary <Prtry> [1..1] ± 3018
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2541 August 2026
```

