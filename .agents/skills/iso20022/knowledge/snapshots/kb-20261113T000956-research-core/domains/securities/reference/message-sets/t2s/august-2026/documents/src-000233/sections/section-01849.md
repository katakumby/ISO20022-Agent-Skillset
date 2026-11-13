---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.5 SettlementParameters <SttlmParams>", "72.4.3.4.18.5.8 CCPEligibility <CCPElgblty>"]
file_pages: [2542]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.5.8 CCPEligibility <CCPElgblty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2542 to 2542.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2542

```text
72.4.3.4.18.5.8  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 2984 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 2984
Or}   Proprietary <Prtry> [1..1] ± 2984
72.4.3.4.18.5.9  DeliveryReturnReason <DlvryRtrRsn>
Presence: [0..1]
Definition: Specifies the reason of a delivery return.
DeliveryReturnReason <DlvryRtrRsn> contains one of the following elements (see
"DeliveryReturn3Choice" on page 3026 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3026
Or}   Proprietary <Prtry> [1..1] ± 3027
72.4.3.4.18.5.10  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem4Choice" on page 2906 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2906
Or}   Proprietary <Prtry> [1..1] ± 2906
72.4.3.4.18.5.11  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 2975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2975
Or}   Proprietary <Prtry> [1..1] ± 2976
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2542 August 2026
```

