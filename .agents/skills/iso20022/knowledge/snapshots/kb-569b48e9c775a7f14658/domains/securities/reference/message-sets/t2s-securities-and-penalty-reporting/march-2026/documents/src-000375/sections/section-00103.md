---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.5 SettlementParameters <SttlmParams>", "4.4.3.4.18.5.8 CCPEligibility <CCPElgblty>"]
file_pages: [146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.5.8 CCPEligibility <CCPElgblty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 146 to 146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
4.4.3.4.18.5.8  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 365 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 365
Or}   Proprietary <Prtry> [1..1] ± 365
4.4.3.4.18.5.9  DeliveryReturnReason <DlvryRtrRsn>
Presence: [0..1]
Definition: Specifies the reason of a delivery return.
DeliveryReturnReason <DlvryRtrRsn> contains one of the following elements (see
"DeliveryReturn3Choice" on page 386 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 386
Or}   Proprietary <Prtry> [1..1] ± 387
4.4.3.4.18.5.10  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem4Choice" on page 314 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 314
Or}   Proprietary <Prtry> [1..1] ± 314
4.4.3.4.18.5.11  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 360 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 360
Or}   Proprietary <Prtry> [1..1] ± 361
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 146 March 2026
```

