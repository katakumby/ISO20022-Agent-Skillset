---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.1 TaxEfficientProductType <TaxEffcntPdctTp>"]
file_pages: [1347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.1 TaxEfficientProductType <TaxEffcntPdctTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1347 to 1347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1347

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C15 1355
   OtherAmount <OthrAmt> [0..*]  1355
     Type <Tp> [1..1] ± 1355
     Amount <Amt> [1..1] Amount C1, C15 1355
   DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1356
   InvestorTaxReference <InvstrTaxRef> [0..1]  1356
     Type <Tp> [0..1]  1356
{Or       Code <Cd> [1..1] CodeSet 1356
Or}       Proprietary <Prtry> [1..1] ± 1357
     Reference <Ref> [1..1] Text 1357
   InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1357
   InnovativeFinance <InnvtvFinc> [0..*]  1357
     Type <Tp> [1..1] ± 1358
     Information <Inf> [1..1] Text 1358
   LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1358
   TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1358
   UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1359
   CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1359
   EstimatedValue <EstmtdVal> [0..1] ± 1359
   AdditionalInformation <AddtlInf> [0..*] ± 1360
38.4.15.4.1.1  TaxEfficientProductType <TaxEffcntPdctTp>
Presence: [1..1]
Definition: Type of tax efficient product, for example, an individual savings account (ISA) in the UK.
TaxEfficientProductType <TaxEffcntPdctTp> contains one of the following elements (see
"TaxEfficientProductType2Choice" on page 4505 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4506
Or}   Proprietary <Prtry> [1..1] ± 4507
38.4.15.4.1.2  CurrentYear <CurYr>
Presence: [0..1]
Definition: Indicates that all the current fiscal year's products are included.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1347 May 2026
```

