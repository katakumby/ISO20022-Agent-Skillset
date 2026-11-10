---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.2 Structure"]
file_pages: [393, 394]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 393 to 394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 393

```text
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RtrLmt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 395
   ReportOrError <RptOrErr> [1..1]  396
{Or     BusinessReport <BizRpt> [1..1]  398
       CurrentLimit <CurLmt> [0..*]  400
         LimitIdentification <LmtId> [1..1]  C3, C4 401
           SystemIdentification <SysId> [0..1] ± 402
           BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 402
           Type <Tp> [1..1]  403
{Or             Code <Cd> [1..1] CodeSet 403
Or}             Proprietary <Prtry> [1..1] Text 405
           AccountOwner <AcctOwnr> [0..1] ± 405
           AccountIdentification <AcctId> [0..1] ± 406
         LimitOrError <LmtOrErr> [1..1]  406
{Or           Limit <Lmt> [1..1]  407
             Amount <Amt> [1..1] ± 407
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
             Status <Sts> [0..1] CodeSet 408
             StartDateTime <StartDtTm> [0..1] ± 408
             UsedAmount <UsdAmt> [0..1] ± 408
             UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd> [0..1] CodeSet 409
             UsedPercentage <UsdPctg> [0..1] Rate 409
             RemainingAmount <RmngAmt> [0..1] ± 409
Or}           BusinessError <BizErr> [1..*]  409
             Error <Err> [1..1]  410
{Or               Code <Cd> [1..1] CodeSet 410
Or}               Proprietary <Prtry> [1..1] Text 410
             Description <Desc> [0..1] Text 410
       DefaultLimit <DfltLmt> [0..*]  410
         LimitIdentification <LmtId> [1..1]  C3, C4 411
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 393 February 2025
```

## File page 394

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SystemIdentification <SysId> [0..1] ± 412
           BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 412
           Type <Tp> [1..1]  413
{Or             Code <Cd> [1..1] CodeSet 413
Or}             Proprietary <Prtry> [1..1] Text 415
           AccountOwner <AcctOwnr> [0..1] ± 415
           AccountIdentification <AcctId> [0..1] ± 416
         LimitOrError <LmtOrErr> [1..1]  416
{Or           Limit <Lmt> [1..1]  417
             Amount <Amt> [1..1] ± 417
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 418
             Status <Sts> [0..1] CodeSet 418
             StartDateTime <StartDtTm> [0..1] ± 418
             UsedAmount <UsdAmt> [0..1] ± 418
             UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd> [0..1] CodeSet 419
             UsedPercentage <UsdPctg> [0..1] Rate 419
             RemainingAmount <RmngAmt> [0..1] ± 419
Or}           BusinessError <BizErr> [1..*]  419
             Error <Err> [1..1]  420
{Or               Code <Cd> [1..1] CodeSet 420
Or}               Proprietary <Prtry> [1..1] Text 420
             Description <Desc> [0..1] Text 420
Or}     OperationalError <OprlErr> [1..*]  420
       Error <Err> [1..1]  420
{Or         Code <Cd> [1..1] CodeSet 421
Or}         Proprietary <Prtry> [1..1] Text 421
       Description <Desc> [0..1] Text 421
   SupplementaryData <SplmtryData> [0..*] ± C8 421
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 394 February 2025
```

