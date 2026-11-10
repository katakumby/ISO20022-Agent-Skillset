---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "36.4.15.5.1.1 TaxEfficientProductType <TaxEffcntPdctTp>"]
file_pages: [1155]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1.1 TaxEfficientProductType <TaxEffcntPdctTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1155 to 1155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1155

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C18 1163
   OtherAmount <OthrAmt> [0..*]  1163
     Type <Tp> [1..1] ± 1163
     Amount <Amt> [1..1] Amount C1, C18 1163
   DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1164
   InvestorTaxReference <InvstrTaxRef> [0..1]  1164
     Type <Tp> [0..1]  1164
{Or       Code <Cd> [1..1] CodeSet 1164
Or}       Proprietary <Prtry> [1..1] ± 1165
     Reference <Ref> [1..1] Text 1165
   InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1165
   InnovativeFinance <InnvtvFinc> [0..*]  1165
     Type <Tp> [1..1] ± 1166
     Information <Inf> [1..1] Text 1166
   LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1166
   TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1166
   UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1167
   CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1167
   EstimatedValue <EstmtdVal> [0..1] ± 1167
   AdditionalInformation <AddtlInf> [0..*] ± 1168
36.4.15.5.1.1  TaxEfficientProductType <TaxEffcntPdctTp>
Presence: [1..1]
Definition: Type of tax efficient product, for example, an individual savings account (ISA) in the UK.
TaxEfficientProductType <TaxEffcntPdctTp> contains one of the following elements (see
"TaxEfficientProductType2Choice" on page 4505 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4506
Or}   Proprietary <Prtry> [1..1] ± 4507
36.4.15.5.1.2  CurrentYear <CurYr>
Presence: [0..1]
Definition: Indicates that all the current fiscal year's products are included.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1155 May 2026
```

