---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.2 DefaultLimit <DfltLmt>", "9.4.2.1.2.1 LimitIdentification <LmtId>"]
file_pages: [411]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.2.1 LimitIdentification <LmtId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 411 to 411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
DefaultLimit <DfltLmt> contains the following LimitReport8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitIdentification <LmtId> [1..1]  C3, C4 411
     SystemIdentification <SysId> [0..1] ± 412
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 412
     Type <Tp> [1..1]  413
{Or       Code <Cd> [1..1] CodeSet 413
Or}       Proprietary <Prtry> [1..1] Text 415
     AccountOwner <AcctOwnr> [0..1] ± 415
     AccountIdentification <AcctId> [0..1] ± 416
   LimitOrError <LmtOrErr> [1..1]  416
{Or     Limit <Lmt> [1..1]  417
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
Or}     BusinessError <BizErr> [1..*]  419
       Error <Err> [1..1]  420
{Or         Code <Cd> [1..1] CodeSet 420
Or}         Proprietary <Prtry> [1..1] Text 420
       Description <Desc> [0..1] Text 420
9.4.2.1.2.1  LimitIdentification <LmtId>
Presence: [1..1]
Definition: Identification of the limit on which information is requested.
Impacted by: C3 "BilateralLimitCounterparty1Rule", C4 "BilateralLimitCounterparty2Rule"
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 411 February 2025
```

