---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.10 UnitsDetails <UnitsDtls>", "36.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "36.4.15.11.10.8.5 IndividualFee <IndvFee>"]
file_pages: [1238]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.10.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1238 to 1238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1238

```text
36.4.15.11.10.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1238
{Or     Code <Cd> [1..1] CodeSet 1239
Or}     Proprietary <Prtry> [1..1] ± 1240
   Basis <Bsis> [0..1]  1240
{Or     Code <Cd> [1..1] CodeSet 1240
Or}     Proprietary <Prtry> [1..1] ± 1241
   StandardAmount <StdAmt> [0..1] Amount C1, C18 1241
   StandardRate <StdRate> [0..1] Rate 1241
   DiscountDetails <DscntDtls> [0..1]  C24 1242
     Amount <Amt> [0..1] Amount C1, C18 1242
     Rate <Rate> [0..1] Rate 1243
     Basis <Bsis> [0..1]  1243
{Or       Code <Cd> [1..1] CodeSet 1243
Or}       Proprietary <Prtry> [1..1] ± 1243
   AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1244
   AppliedRate <ApldRate> [0..1] Rate 1244
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 1244
   RecipientIdentification <RcptId> [0..1] ± 1244
   InformativeIndicator <InftvInd> [1..1] Indicator 1245
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
36.4.15.11.10.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1238 May 2026
```

