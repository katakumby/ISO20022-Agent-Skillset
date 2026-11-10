---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.8 TransactionOverhead <TxOvrhd>", "38.4.15.8.4.8.5 IndividualFee <IndvFee>"]
file_pages: [1404]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1404 to 1404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1404

```text
38.4.15.8.4.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1404
{Or     Code <Cd> [1..1] CodeSet 1405
Or}     Proprietary <Prtry> [1..1] ± 1406
   Basis <Bsis> [0..1]  1406
{Or     Code <Cd> [1..1] CodeSet 1406
Or}     Proprietary <Prtry> [1..1] ± 1407
   StandardAmount <StdAmt> [0..1] Amount C1, C15 1407
   StandardRate <StdRate> [0..1] Rate 1407
   DiscountDetails <DscntDtls> [0..1]  C21 1408
     Amount <Amt> [0..1] Amount C1, C15 1408
     Rate <Rate> [0..1] Rate 1409
     Basis <Bsis> [0..1]  1409
{Or       Code <Cd> [1..1] CodeSet 1409
Or}       Proprietary <Prtry> [1..1] ± 1409
   AppliedAmount <ApldAmt> [0..1] Amount C1, C15 1410
   AppliedRate <ApldRate> [0..1] Rate 1410
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 1410
   RecipientIdentification <RcptId> [0..1] ± 1410
   InformativeIndicator <InftvInd> [1..1] Indicator 1411
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
38.4.15.8.4.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1404 May 2026
```

