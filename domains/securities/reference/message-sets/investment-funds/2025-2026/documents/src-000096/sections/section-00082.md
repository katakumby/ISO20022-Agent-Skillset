---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "9.4 Message Building Blocks", "9.4.5 MessagePagination <MsgPgntn>"]
file_pages: [121, 122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.042.001.04"]
---

# 9.4.5 MessagePagination <MsgPgntn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 121 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
9.4.5 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
9.4.6 FundOrSubFundDetails <FndOrSubFndDtls>
Presence: [0..1]
Definition: Information about the fund/sub fund when the report either specifies cash flow for the
fund/sub fund or for a share class of the fund/sub fund.
Impacted by: C14 "FundIdentification1Rule", C15 "FundIdentification2Rule", C16
"FundIdentification3Rule"
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 121 May 2026
```

## File page 122

```text
FundOrSubFundDetails <FndOrSubFndDtls> contains the following elements (see "Fund3" on
page 4688 for details)
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
• FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /LegalEntityIdentifier is absent
Following Must be True
    /Identification Must be present
 Or    /Name Must be present
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 122 May 2026
```

