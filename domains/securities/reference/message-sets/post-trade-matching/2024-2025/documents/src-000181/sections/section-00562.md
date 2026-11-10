---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.74 StatementUpdateType1Code"]
file_pages: [652]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.74 StatementUpdateType1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 652 to 652.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 652

```text
CodeName Name Definition
OPEX OptionExercise Exercise of an option contract.
7.2.2.74  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
7.2.2.75  TaxLiability1Code
Definition: Specifies the tax role capacity of the instructing party.
Type: CodeSet
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
7.2.2.76  TradeRegulatoryConditions1Code
Definition: indicates if the Trade Regulatory Conditions is solicited or not.
Type: CodeSet
CodeName Name Definition
SOLI Solicited Trade was solicited by the executing
broker. The broker has suggested to his
client to buy/sell financial instruments.
USOL Unsolicited Trade was unsolicited. The client acts on
its own without advice from the
executing broker.
7.2.2.77  TradeTransactionCondition2Code
Definition: Specifies the conditions under which the order/trade is to be executed.
Type: CodeSet
CodeName Name Definition
SPCC SpecialCumCoupon Indicates whether the trade is executed
with a special cum coupon.
SECN SpecialExCoupon Indicates whether the trade is executed
with a special ex coupon.
SEBN SpecialExBonus Indicates whether the trade is executed
special ex bonus.
SCBN SpecialCumBonus Indicates whether the trade is executed
special cum bonus.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 652 February 2025
```

