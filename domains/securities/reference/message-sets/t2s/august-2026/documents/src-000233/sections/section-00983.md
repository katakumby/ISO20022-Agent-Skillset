---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.3 Debt <Debt>", "28.4.2.1.3.1.3.62 AutoReinvestment <AutoRinvstmt>"]
file_pages: [1435]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.3.62 AutoReinvestment <AutoRinvstmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1435 to 1435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1435

```text
28.4.2.1.3.1.3.62  AutoReinvestment <AutoRinvstmt>
Presence: [0..1]
Definition: Indicates an instruction to reinvest dividends in the underlying security (or proceeds at
maturity in a similar instrument) if the current rate is <rate> or better.
Datatype: "PercentageRate" on page 3325
28.4.2.1.3.1.3.63  Haircut <Hrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage.
Datatype: "PercentageRate" on page 3325
28.4.2.1.3.1.3.64  TransactionConditions <TxConds>
Presence: [0..1]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TransactionConditions <TxConds> contains one of the following elements (see
"TradeTransactionCondition7Choice" on page 3204 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3204
Or}   Proprietary <Prtry> [1..1] ± 3205
28.4.2.1.3.1.3.65  LookBack <LookBck>
Presence: [0..1]
Definition: Indicates an instruction or attribute giving the number of days to be included in the look-back
period for the investment. For example some options allow exercise based on the underlying asset's
optimal value over the look-back period.
Datatype: "Number" on page 3324
28.4.2.1.3.1.3.66  MaximumSubstitution <MaxSbstitn>
Presence: [0..1]
Definition: Maximum number of time the collateral can be substitute.
Datatype: "Number" on page 3324
28.4.2.1.3.1.3.67  MinimumIncrement <MinIncrmt>
Presence: [0..1]
Definition: Indicates the minimum tradable increments of a security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1435 August 2026
```

