---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.30 VariableRateIndicator <VarblRateInd>"]
file_pages: [1469]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.30 VariableRateIndicator <VarblRateInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1469 to 1469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1469

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown60" on
page 1732 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [1..1] ± 1732
   LotQuantity <LotQty> [0..1] ± C12 1733
35.1.11.4.30  VariableRateIndicator <VarblRateInd>
Presence: [0..1]
Definition: Indicates whether the interest rate of an interest bearing instrument is reset periodically.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.11.4.31  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.11.4.32  PutableIndicator <PutblInd>
Presence: [0..1]
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.11.4.33  MarketOrIndicativePrice <MktOrIndctvPric>
Presence: [0..1]
Definition: Value of the price, for example, as a currency and value per unit or as a percentage.
MarketOrIndicativePrice <MktOrIndctvPric> contains one of the following elements (see
"PriceType4Choice" on page 1710 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Market <Mkt> [1..1] ± 1711
Or}   Indicative <Indctv> [1..1] ± 1711
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1469 March 2026
```

