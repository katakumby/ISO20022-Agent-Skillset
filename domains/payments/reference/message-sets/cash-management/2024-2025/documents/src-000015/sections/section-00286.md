---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.2 DefaultLimit <DfltLmt>", "9.4.2.1.2.2 LimitOrError <LmtOrErr>", "9.4.2.1.2.2.1 Limit <Lmt>"]
file_pages: [417]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.2.2.1 Limit <Lmt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 417 to 417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 417

```text
LimitOrError <LmtOrErr> contains one of the following LimitOrError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Limit <Lmt> [1..1]  417
     Amount <Amt> [1..1] ± 417
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 418
     Status <Sts> [0..1] CodeSet 418
     StartDateTime <StartDtTm> [0..1] ± 418
     UsedAmount <UsdAmt> [0..1] ± 418
     UsedAmountCreditDebitIndicator
<UsdAmtCdtDbtInd>
[0..1] CodeSet 419
     UsedPercentage <UsdPctg> [0..1] Rate 419
     RemainingAmount <RmngAmt> [0..1] ± 419
Or}   BusinessError <BizErr> [1..*]  419
     Error <Err> [1..1]  420
{Or       Code <Cd> [1..1] CodeSet 420
Or}       Proprietary <Prtry> [1..1] Text 420
     Description <Desc> [0..1] Text 420
9.4.2.1.2.2.1  Limit <Lmt>
Presence: [1..1]
Definition: Requested information on the limit.
Limit <Lmt> contains the following Limit7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 417
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 418
   Status <Sts> [0..1] CodeSet 418
   StartDateTime <StartDtTm> [0..1] ± 418
   UsedAmount <UsdAmt> [0..1] ± 418
   UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd> [0..1] CodeSet 419
   UsedPercentage <UsdPctg> [0..1] Rate 419
   RemainingAmount <RmngAmt> [0..1] ± 419
9.4.2.1.2.2.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 417 February 2025
```

