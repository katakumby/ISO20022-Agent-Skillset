---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.36 BreakdownByCountry2", "66.1.28.36.3 CashOutForecast <CshOutFcst>", "66.1.28.36.3.3 SubTotalUnitsNumber <SubTtlUnitsNb>"]
file_pages: [4878]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.36.3.3 SubTotalUnitsNumber <SubTtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4878 to 4878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4878

```text
66.1.28.36.3.3  SubTotalUnitsNumber <SubTtlUnitsNb>
Presence: [0..1]
Definition: Sub-total amount of the cash flow out, expressed as a number of units.
SubTotalUnitsNumber <SubTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.28.36.3.4  ExceptionalCashFlowIndicator <XcptnlCshFlowInd>
Presence: [0..1]
Definition: Indicates whether the estimated cash flow out is exceptional.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.36.3.5  CashOutBreakdownDetails <CshOutBrkdwnDtls>
Presence: [0..*]
Definition: Breakdown of cash out amounts by transaction and order type.
CashOutBreakdownDetails <CshOutBrkdwnDtls> contains the following elements (see
"FundCashOutBreakdown3" on page 4826 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4827
   UnitsNumber <UnitsNb> [0..1] ± 4827
   NewAmountIndicator <NewAmtInd> [0..1] Indicator 4828
   InvestmentFundTransactionOutType
<InvstmtFndTxOutTp>
[1..1]  4828
{Or     Code <Cd> [1..1] CodeSet 4828
Or}     Proprietary <Prtry> [1..1] ± 4828
   OriginalOrderQuantityType <OrgnlOrdrQtyTp> [1..1]  4829
{Or     Code <Cd> [1..1] CodeSet 4829
Or}     Proprietary <Prtry> [1..1] ± 4829
   ChargeDetails <ChrgDtls> [0..*] ± 4829
   CommissionDetails <ComssnDtls> [0..*] ± 4830
   SettlementCurrency <SttlmCcy> [0..1] CodeSet C1 4830
66.1.28.36.3.6  AdditionalBalance <AddtlBal>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4878 May 2026
```

