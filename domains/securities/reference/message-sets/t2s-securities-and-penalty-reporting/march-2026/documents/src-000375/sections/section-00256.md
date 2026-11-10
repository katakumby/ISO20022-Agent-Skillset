---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.30 CallableIndicator <CllblInd>"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.30 CallableIndicator <CllblInd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
• Meaning When True: Yes
• Meaning When False: No
7.1.12.1.30  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.12.1.31  PutableIndicator <PutblInd>
Presence: [0..1]
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.12.1.32  MarketOrIndicativePrice <MktOrIndctvPric>
Presence: [0..1]
Definition: Value of the price, for example, as a currency and value per unit or as a percentage.
MarketOrIndicativePrice <MktOrIndctvPric> contains one of the following elements (see
"PriceType4Choice" on page 445 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Market <Mkt> [1..1] ± 445
Or}   Indicative <Indctv> [1..1] ± 446
7.1.12.1.33  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a derivative will buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following elements (see "Price7" on page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 333 March 2026
```

