---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>"]
file_pages: [398, 399]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1 BusinessReport <BizRpt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 398 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 398

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Type <Tp> [1..1]  413
{Or           Code <Cd> [1..1] CodeSet 413
Or}           Proprietary <Prtry> [1..1] Text 415
         AccountOwner <AcctOwnr> [0..1] ± 415
         AccountIdentification <AcctId> [0..1] ± 416
       LimitOrError <LmtOrErr> [1..1]  416
{Or         Limit <Lmt> [1..1]  417
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
Or}         BusinessError <BizErr> [1..*]  419
           Error <Err> [1..1]  420
{Or             Code <Cd> [1..1] CodeSet 420
Or}             Proprietary <Prtry> [1..1] Text 420
           Description <Desc> [0..1] Text 420
Or}   OperationalError <OprlErr> [1..*]  420
     Error <Err> [1..1]  420
{Or       Code <Cd> [1..1] CodeSet 421
Or}       Proprietary <Prtry> [1..1] Text 421
     Description <Desc> [0..1] Text 421
9.4.2.1  BusinessReport <BizRpt>
Presence: [1..1]
Definition: Reports on limits.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 398 February 2025
```

## File page 399

```text
BusinessReport <BizRpt> contains the following Limits8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrentLimit <CurLmt> [0..*]  400
     LimitIdentification <LmtId> [1..1]  C3, C4 401
       SystemIdentification <SysId> [0..1] ± 402
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 402
       Type <Tp> [1..1]  403
{Or         Code <Cd> [1..1] CodeSet 403
Or}         Proprietary <Prtry> [1..1] Text 405
       AccountOwner <AcctOwnr> [0..1] ± 405
       AccountIdentification <AcctId> [0..1] ± 406
     LimitOrError <LmtOrErr> [1..1]  406
{Or       Limit <Lmt> [1..1]  407
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
Or}       BusinessError <BizErr> [1..*]  409
         Error <Err> [1..1]  410
{Or           Code <Cd> [1..1] CodeSet 410
Or}           Proprietary <Prtry> [1..1] Text 410
         Description <Desc> [0..1] Text 410
   DefaultLimit <DfltLmt> [0..*]  410
     LimitIdentification <LmtId> [1..1]  C3, C4 411
       SystemIdentification <SysId> [0..1] ± 412
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 412
       Type <Tp> [1..1]  413
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 399 February 2025
```

