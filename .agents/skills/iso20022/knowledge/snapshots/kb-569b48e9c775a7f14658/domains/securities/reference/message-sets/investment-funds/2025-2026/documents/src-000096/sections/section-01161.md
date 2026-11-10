---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.10 UnitsDetails <UnitsDtls>", "40.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "40.4.15.11.10.8.5 IndividualFee <IndvFee>"]
file_pages: [1621]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.10.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1621 to 1621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1621

```text
40.4.15.11.10.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1621
{Or     Code <Cd> [1..1] CodeSet 1622
Or}     Proprietary <Prtry> [1..1] ± 1623
   Basis <Bsis> [0..1]  1623
{Or     Code <Cd> [1..1] CodeSet 1623
Or}     Proprietary <Prtry> [1..1] ± 1624
   StandardAmount <StdAmt> [0..1] Amount C1, C18 1624
   StandardRate <StdRate> [0..1] Rate 1624
   DiscountDetails <DscntDtls> [0..1]  C24 1625
     Amount <Amt> [0..1] Amount C1, C18 1625
     Rate <Rate> [0..1] Rate 1626
     Basis <Bsis> [0..1]  1626
{Or       Code <Cd> [1..1] CodeSet 1626
Or}       Proprietary <Prtry> [1..1] ± 1626
   AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1627
   AppliedRate <ApldRate> [0..1] Rate 1627
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 1627
   RecipientIdentification <RcptId> [0..1] ± 1627
   InformativeIndicator <InftvInd> [1..1] Indicator 1628
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
40.4.15.11.10.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1621 May 2026
```

