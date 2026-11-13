---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.9 UnitsDetails <UnitsDtls>", "35.4.14.10.9.8 TransactionOverhead <TxOvrhd>", "35.4.14.10.9.8.5 IndividualFee <IndvFee>"]
file_pages: [1043]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.9.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1043 to 1043.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1043

```text
35.4.14.10.9.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1043
{Or     Code <Cd> [1..1] CodeSet 1044
Or}     Proprietary <Prtry> [1..1] ± 1045
   Basis <Bsis> [0..1]  1045
{Or     Code <Cd> [1..1] CodeSet 1045
Or}     Proprietary <Prtry> [1..1] ± 1046
   StandardAmount <StdAmt> [0..1] Amount C1, C18 1046
   StandardRate <StdRate> [0..1] Rate 1046
   DiscountDetails <DscntDtls> [0..1]  C23 1047
     Amount <Amt> [0..1] Amount C1, C18 1047
     Rate <Rate> [0..1] Rate 1048
     Basis <Bsis> [0..1]  1048
{Or       Code <Cd> [1..1] CodeSet 1048
Or}       Proprietary <Prtry> [1..1] ± 1048
   AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1049
   AppliedRate <ApldRate> [0..1] Rate 1049
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 1049
   RecipientIdentification <RcptId> [0..1] ± 1049
   InformativeIndicator <InftvInd> [1..1] Indicator 1050
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
35.4.14.10.9.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1043 May 2026
```

