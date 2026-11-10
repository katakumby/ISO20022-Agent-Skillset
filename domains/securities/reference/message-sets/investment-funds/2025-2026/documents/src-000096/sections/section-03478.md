---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.23 PriceDetails <PricDtls>", "66.1.26.3.23.4 PriceMethod <PricMtd>"]
file_pages: [4728]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.23.4 PriceMethod <PricMtd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4728 to 4728.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4728

```text
Value <Val> contains the following elements (see "PriceValue1" on page 5127 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 5128
66.1.26.3.23.4  PriceMethod <PricMtd>
Presence: [0..1]
Definition: Type of pricing calculation method.
Datatype: "PriceMethod1Code" on page 5343
CodeName Name Definition
FORW ForwardPrice Price will be calculated after the close of
the dealing period. An investor,
therefore, does not know the exact buy
or sell price.
HIST HistoricalPrice Price is calculated at an earlier valuation
point preceding the dealing period. An
investor, therefore, knows the exact buy
or sell price.
66.1.26.4  OtherTargetMarket1
Definition: Other target market parameter.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TargetMarketType <TrgtMktTp> [1..1] Text 4728
   AdditionalInformation <AddtlInf> [0..1] ± 4728
66.1.26.4.1  TargetMarketType <TrgtMktTp>
Presence: [1..1]
Definition: Type of target market parameter.
Datatype: "Max350Text" on page 5403
66.1.26.4.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the target market.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4728 May 2026
```

