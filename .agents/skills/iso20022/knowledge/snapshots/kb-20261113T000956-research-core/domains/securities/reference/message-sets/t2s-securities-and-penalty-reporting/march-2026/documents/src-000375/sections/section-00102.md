---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.5 SettlementParameters <SttlmParams>", "4.4.3.4.18.5.5 PartialSettlementIndicator <PrtlSttlmInd>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.5.5 PartialSettlementIndicator <PrtlSttlmInd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition34Choice" on page 370 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 370
Or}   Proprietary <Prtry> [1..1] ± 371
4.4.3.4.18.5.5  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: "SettlementTransactionCondition5Code" on page 540
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
4.4.3.4.18.5.6  BeneficialOwnership <BnfclOwnrsh>
Presence: [0..1]
Definition: Specifies whether there is change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 389 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 389
Or}   Proprietary <Prtry> [1..1] ± 389
4.4.3.4.18.5.7  BlockTrade <BlckTrad>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is a block parent or child.
BlockTrade <BlckTrad> contains one of the following elements (see "BlockTrade4Choice" on
page 381 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 381
Or}   Proprietary <Prtry> [1..1] ± 381
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 145 March 2026
```

