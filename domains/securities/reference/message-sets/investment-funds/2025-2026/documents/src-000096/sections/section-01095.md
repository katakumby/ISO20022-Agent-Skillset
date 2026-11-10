---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "40.4.15.5.1.1 TaxEfficientProductType <TaxEffcntPdctTp>"]
file_pages: [1538]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1.1 TaxEfficientProductType <TaxEffcntPdctTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1538 to 1538.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1538

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C18 1546
   OtherAmount <OthrAmt> [0..*]  1546
     Type <Tp> [1..1] ± 1546
     Amount <Amt> [1..1] Amount C1, C18 1546
   DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1547
   InvestorTaxReference <InvstrTaxRef> [0..1]  1547
     Type <Tp> [0..1]  1547
{Or       Code <Cd> [1..1] CodeSet 1547
Or}       Proprietary <Prtry> [1..1] ± 1548
     Reference <Ref> [1..1] Text 1548
   InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1548
   InnovativeFinance <InnvtvFinc> [0..*]  1548
     Type <Tp> [1..1] ± 1549
     Information <Inf> [1..1] Text 1549
   LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1549
   TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1549
   UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1550
   CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1550
   EstimatedValue <EstmtdVal> [0..1] ± 1550
   AdditionalInformation <AddtlInf> [0..*] ± 1551
40.4.15.5.1.1  TaxEfficientProductType <TaxEffcntPdctTp>
Presence: [1..1]
Definition: Type of tax efficient product, for example, an individual savings account (ISA) in the UK.
TaxEfficientProductType <TaxEffcntPdctTp> contains one of the following elements (see
"TaxEfficientProductType2Choice" on page 4505 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4506
Or}   Proprietary <Prtry> [1..1] ± 4507
40.4.15.5.1.2  CurrentYear <CurYr>
Presence: [0..1]
Definition: Indicates that all the current fiscal year's products are included.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1538 May 2026
```

