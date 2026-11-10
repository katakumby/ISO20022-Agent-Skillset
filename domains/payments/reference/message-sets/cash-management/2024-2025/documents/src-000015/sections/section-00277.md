---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.1 CurrentLimit <CurLmt>", "9.4.2.1.1.2 LimitOrError <LmtOrErr>", "9.4.2.1.1.2.1 Limit <Lmt>"]
file_pages: [407]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.1.2.1 Limit <Lmt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 407 to 407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 407

```text
LimitOrError <LmtOrErr> contains one of the following LimitOrError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Limit <Lmt> [1..1]  407
     Amount <Amt> [1..1] ± 407
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
     Status <Sts> [0..1] CodeSet 408
     StartDateTime <StartDtTm> [0..1] ± 408
     UsedAmount <UsdAmt> [0..1] ± 408
     UsedAmountCreditDebitIndicator
<UsdAmtCdtDbtInd>
[0..1] CodeSet 409
     UsedPercentage <UsdPctg> [0..1] Rate 409
     RemainingAmount <RmngAmt> [0..1] ± 409
Or}   BusinessError <BizErr> [1..*]  409
     Error <Err> [1..1]  410
{Or       Code <Cd> [1..1] CodeSet 410
Or}       Proprietary <Prtry> [1..1] Text 410
     Description <Desc> [0..1] Text 410
9.4.2.1.1.2.1  Limit <Lmt>
Presence: [1..1]
Definition: Requested information on the limit.
Limit <Lmt> contains the following Limit7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 407
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
   Status <Sts> [0..1] CodeSet 408
   StartDateTime <StartDtTm> [0..1] ± 408
   UsedAmount <UsdAmt> [0..1] ± 408
   UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd> [0..1] CodeSet 409
   UsedPercentage <UsdPctg> [0..1] Rate 409
   RemainingAmount <RmngAmt> [0..1] ± 409
9.4.2.1.1.2.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 407 February 2025
```

