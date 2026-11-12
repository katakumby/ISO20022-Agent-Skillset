---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.30 VariableRateIndicator <VarblRateInd>"]
file_pages: [217]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.30 VariableRateIndicator <VarblRateInd>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 217 to 217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 217

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown31" on
page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [1..1] ± 264
   LotQuantity <LotQty> [0..1] ± 264
9.1.9.2.30  VariableRateIndicator <VarblRateInd>
Presence: [0..1]
Definition: Indicates whether the interest rate of an interest bearing instrument is reset periodically.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
9.1.9.2.31  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
9.1.9.2.32  PutableIndicator <PutblInd>
Presence: [0..1]
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
9.1.9.2.33  MarketOrIndicativePrice <MktOrIndctvPric>
Presence: [0..1]
Definition: Value of the price, for example, as a currency and value per unit or as a percentage.
MarketOrIndicativePrice <MktOrIndctvPric> contains one of the following elements (see
"PriceType4Choice" on page 262 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Market <Mkt> [1..1] ± 262
Or}   Indicative <Indctv> [1..1] ± 262
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 217 September 2025
```

