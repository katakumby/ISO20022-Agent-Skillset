---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.62 AutoReinvestment <AutoRinvstmt>"]
file_pages: [224]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.62 AutoReinvestment <AutoRinvstmt>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 224 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
13.1.2.3.62  AutoReinvestment <AutoRinvstmt>
Presence: [0..1]
Definition: Indicates an instruction to reinvest dividends in the underlying security (or proceeds at
maturity in a similar instrument) if the current rate is <rate> or better.
Datatype: "PercentageRate" on page 532
13.1.2.3.63  Haircut <Hrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage.
Datatype: "PercentageRate" on page 532
13.1.2.3.64  TransactionConditions <TxConds>
Presence: [0..1]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TransactionConditions <TxConds> contains one of the following elements (see
"TradeTransactionCondition7Choice" on page 504 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 504
Or}   Proprietary <Prtry> [1..1] ± 505
13.1.2.3.65  LookBack <LookBck>
Presence: [0..1]
Definition: Indicates an instruction or attribute giving the number of days to be included in the look-back
period for the investment. For example some options allow exercise based on the underlying asset's
optimal value over the look-back period.
Datatype: "Number" on page 532
13.1.2.3.66  MaximumSubstitution <MaxSbstitn>
Presence: [0..1]
Definition: Maximum number of time the collateral can be substitute.
Datatype: "Number" on page 532
13.1.2.3.67  MinimumIncrement <MinIncrmt>
Presence: [0..1]
Definition: Indicates the minimum tradable increments of a security.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 224 March 2024
```

