---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.30 ConversionRatioNumerator <ConvsRatioNmrtr>"]
file_pages: [281]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.30 ConversionRatioNumerator <ConvsRatioNmrtr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 281 to 281.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 281

```text
13.1.6.2.30  ConversionRatioNumerator <ConvsRatioNmrtr>
Presence: [0..1]
Definition: Number of target securities for the conversion.
ConversionRatioNumerator <ConvsRatioNmrtr> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.31  ConversionRatioDenominator <ConvsRatioDnmtr>
Presence: [0..1]
Definition: Number of held securities for the conversion.
ConversionRatioDenominator <ConvsRatioDnmtr> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.32  PrimaryPlaceOfDeposit <PmryPlcOfDpst>
Presence: [0..1]
Definition: Primary place of deposit.
PrimaryPlaceOfDeposit <PmryPlcOfDpst> contains the following elements (see
"PartyIdentification136" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 488
   LEI <LEI> [0..1] IdentifierSet 488
13.1.6.2.33  TradingMethod <TradgMtd>
Presence: [0..1]
Definition: Indicates whether the notional amount value is to be traded in either an amount or in units.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 281 March 2024
```

