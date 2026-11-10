---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.1 CurrentLimit <CurLmt>", "9.4.2.1.1.1 LimitIdentification <LmtId>"]
file_pages: [401]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.1.1 LimitIdentification <LmtId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 401 to 401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 401

```text
CurrentLimit <CurLmt> contains the following LimitReport8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitIdentification <LmtId> [1..1]  C3, C4 401
     SystemIdentification <SysId> [0..1] ± 402
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 402
     Type <Tp> [1..1]  403
{Or       Code <Cd> [1..1] CodeSet 403
Or}       Proprietary <Prtry> [1..1] Text 405
     AccountOwner <AcctOwnr> [0..1] ± 405
     AccountIdentification <AcctId> [0..1] ± 406
   LimitOrError <LmtOrErr> [1..1]  406
{Or     Limit <Lmt> [1..1]  407
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
Or}     BusinessError <BizErr> [1..*]  409
       Error <Err> [1..1]  410
{Or         Code <Cd> [1..1] CodeSet 410
Or}         Proprietary <Prtry> [1..1] Text 410
       Description <Desc> [0..1] Text 410
9.4.2.1.1.1  LimitIdentification <LmtId>
Presence: [1..1]
Definition: Identification of the limit on which information is requested.
Impacted by: C3 "BilateralLimitCounterparty1Rule", C4 "BilateralLimitCounterparty2Rule"
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 401 February 2025
```

