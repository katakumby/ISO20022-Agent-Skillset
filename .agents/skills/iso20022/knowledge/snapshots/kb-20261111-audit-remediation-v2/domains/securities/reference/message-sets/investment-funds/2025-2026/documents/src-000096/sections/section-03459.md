---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.8 Fund4"]
file_pages: [4707]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.8 Fund4

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4707 to 4707.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4707

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.25.8  Fund4
Definition: Information about an investment fund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4708
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4708
   Identification <Id> [0..1]  4708
     Identification <Id> [1..1] Text 4708
     Type <Tp> [1..1] ± 4708
   Currency <Ccy> [0..1] CodeSet C2 4709
   TotalNAV <TtlNAV> [0..1] Amount C2, C10 4709
   PreviousTotalNAV <PrvsTtlNAV> [0..1] Amount C2, C10 4709
   TotalUnitsNumber <TtlUnitsNb> [0..1] ± 4710
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4710
   PercentageOfFundTotalNAV <PctgOfFndTtlNAV> [0..1] Rate 4710
Constraints
• FundIdentification1Rule
If Identification is not present, then Name or LegalEntityIdentifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /Identification is absent
Following Must be True
    /Name Must be present
 Or    /LegalEntityIdentifier Must be present
• FundIdentification2Rule
If Name is not present, then Identification or Legal Entity Identifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /Name is absent
Following Must be True
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4707 May 2026
```

