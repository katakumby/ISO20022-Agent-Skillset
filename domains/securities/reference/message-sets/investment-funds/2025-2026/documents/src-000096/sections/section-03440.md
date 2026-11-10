---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.4 Fund3"]
file_pages: [4688]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.4 Fund3

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4688 to 4688.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4688

```text
Definition: Specifies the direction of the cash flow from the perspective of the fund.
Datatype: "FlowDirectionType1Code" on page 5304
CodeName Name Definition
INCG Incoming Amount of money received.
OUTG Outgoing Amount of money paid out.
66.1.25.4  Fund3
Definition: Information about an investment fund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4689
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4689
   Identification <Id> [0..1]  4689
     Identification <Id> [1..1] Text 4689
     Type <Tp> [1..1] ± 4689
   Currency <Ccy> [0..1] CodeSet C2 4690
   EstimatedTotalNAV <EstmtdTtlNAV> [0..1] Amount C2, C10 4690
   PreviousTotalNAV <PrvsTtlNAV> [0..1] Amount C2, C10 4690
   EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> [0..1] ± 4691
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4691
   EstimatedPercentageOfFundTotalNAV
<EstmtdPctgOfFndTtlNAV>
[0..1] Rate 4691
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
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4688 May 2026
```

