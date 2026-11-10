---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.2 FinancialInstrumentAttributes92", "82.1.13.2.30 VariableRateIndicator <VarblRateInd>"]
file_pages: [2942]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.2.30 VariableRateIndicator <VarblRateInd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2942 to 2942.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2942

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown31" on
page 3112 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [1..1] ± 3112
   LotQuantity <LotQty> [0..1] ± 3112
82.1.13.2.30  VariableRateIndicator <VarblRateInd>
Presence: [0..1]
Definition: Indicates whether the interest rate of an interest bearing instrument is reset periodically.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.13.2.31  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.13.2.32  PutableIndicator <PutblInd>
Presence: [0..1]
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.13.2.33  MarketOrIndicativePrice <MktOrIndctvPric>
Presence: [0..1]
Definition: Value of the price, for example, as a currency and value per unit or as a percentage.
MarketOrIndicativePrice <MktOrIndctvPric> contains one of the following elements (see
"PriceType4Choice" on page 3103 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Market <Mkt> [1..1] ± 3103
Or}   Indicative <Indctv> [1..1] ± 3103
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2942 August 2026
```

