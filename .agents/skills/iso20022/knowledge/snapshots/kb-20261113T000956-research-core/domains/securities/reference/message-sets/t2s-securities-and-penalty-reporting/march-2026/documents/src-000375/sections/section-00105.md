---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.5 SettlementParameters <SttlmParams>", "4.4.3.4.18.5.16 RepurchaseType <RpTp>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.5.16 RepurchaseType <RpTp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
4.4.3.4.18.5.16  RepurchaseType <RpTp>
Presence: [0..1]
Definition: Specifies the type of repurchase transaction.
RepurchaseType <RpTp> contains one of the following elements (see "RepurchaseType23Choice" on
page 380 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 380
Or}   Proprietary <Prtry> [1..1] ± 381
4.4.3.4.18.5.17  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 367 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 368
Or}   Proprietary <Prtry> [1..1] ± 368
4.4.3.4.18.5.18  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 368 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 368
Or}   Proprietary <Prtry> [1..1] ± 369
4.4.3.4.18.5.19  SettlingCapacity <SttlgCpcty>
Presence: [0..1]
Definition: Role of a party in the settlement of the transaction.
SettlingCapacity <SttlgCpcty> contains one of the following elements (see "SettlingCapacity7Choice"
on page 402 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 402
Or}   Proprietary <Prtry> [1..1] ± 403
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 148 March 2026
```

