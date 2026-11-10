---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.34 SubscriptionPrice <SbcptPric>"]
file_pages: [334]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.34 SubscriptionPrice <SbcptPric>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 334 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 334

```text
7.1.12.1.34  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a right is entitled to buy the underlying
instrument.
SubscriptionPrice <SbcptPric> contains the following elements (see "Price7" on page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
7.1.12.1.35  ConversionPrice <ConvsPric>
Presence: [0..1]
Definition: Price of one target security in the conversion.
ConversionPrice <ConvsPric> contains the following elements (see "Price7" on page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
7.1.12.1.36  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
StrikePrice <StrkPric> contains the following elements (see "Price7" on page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
7.1.12.1.37  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Minimum nominal quantity of financial instrument.
MinimumNominalQuantity <MinNmnlQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 334 March 2026
```

