---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.1 CurrentLimit <CurLmt>"]
file_pages: [400]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.1 CurrentLimit <CurLmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 400 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 400

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 413
Or}         Proprietary <Prtry> [1..1] Text 415
       AccountOwner <AcctOwnr> [0..1] ± 415
       AccountIdentification <AcctId> [0..1] ± 416
     LimitOrError <LmtOrErr> [1..1]  416
{Or       Limit <Lmt> [1..1]  417
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
Or}       BusinessError <BizErr> [1..*]  419
         Error <Err> [1..1]  420
{Or           Code <Cd> [1..1] CodeSet 420
Or}           Proprietary <Prtry> [1..1] Text 420
         Description <Desc> [0..1] Text 420
9.4.2.1.1  CurrentLimit <CurLmt>
Presence: [0..*]
Definition: Report is given for a current risk management type limit.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 400 February 2025
```

