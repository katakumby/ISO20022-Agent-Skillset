---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.36 ChargeTaxBasisType <ChrgTaxBsisTp>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.36 ChargeTaxBasisType <ChrgTaxBsisTp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
Definition: Indicates whether the derivative product is covered or not by an underlying financial
instrument position.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.4.36  ChargeTaxBasisType <ChrgTaxBsisTp>
Presence: [0..1]
Definition: Type of charge/tax basis.
ChargeTaxBasisType <ChrgTaxBsisTp> contains one of the following elements (see
"ChargeTaxBasisType2Choice" on page 248 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 248
Or}   Proprietary <Prtry> [1..1] ± 248
3.4.4.37  CapitalGainType <CptlGnTp>
Presence: [0..1]
Definition: Specifies the type of capital gain.
CapitalGainType <CptlGnTp> contains one of the following elements (see
"EUCapitalGainType3Choice" on page 307 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   EUCapitalGain <EUCptlGn> [1..1] CodeSet 307
Or}   Proprietary <Prtry> [1..1] ± 307
3.4.4.38  MatchStatus <MtchSts>
Presence: [0..1]
Definition: Provides the matching status of the trade confirmation.
MatchStatus <MtchSts> contains one of the following elements (see "MatchingStatus27Choice" on
page 594 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 594
3.4.4.39  CallInType <CallInTp>
Presence: [0..1]
Definition: Specifies the type of pay-in call report.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 61 February 2025
```

