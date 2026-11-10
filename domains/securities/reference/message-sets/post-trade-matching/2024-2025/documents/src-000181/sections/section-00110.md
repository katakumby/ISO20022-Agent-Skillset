---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "4.4 Message Building Blocks", "4.4.3 OtherBusinessParties <OthrBizPties>"]
file_pages: [143]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4.4.3 OtherBusinessParties <OthrBizPties>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 143 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 143

```text
4.4.3 OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Impacted by: C6 "InvestorUsageRule", C8 "QualifiedForeignIntermediaryRule"
OtherBusinessParties <OthrBizPties> contains the following OtherParties45 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C5 143
   StockExchange <StockXchg> [0..1] ± 144
   TradeRegulator <TradRgltr> [0..1] ± 145
   TripartyAgent <TrptyAgt> [0..1] ± 145
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 145
Constraints
• InvestorUsageRule
When investor is used with a country code, the country code specifies the nationality of the investor,
for the settlement of certain securities (i.e. airlines, defence manufacturers) under the EU legislation.
• QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
4.4.3.1  Investor <Invstr>
Presence: [0..*]
Definition: Party that identifies the underlying investor.
Impacted by: C5 "IdentificationUsageRule"
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 143 February 2025
```

