---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>"]
file_pages: [396, 397]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2 ReportOrError <RptOrErr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 396 to 397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 396

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader7" on page 814 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 814
   CreationDateTime <CreDtTm> [0..1] DateTime 814
   RequestType <ReqTp> [0..1]  814
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 814
Or     Enquiry <Enqry> [1..1] CodeSet 815
Or}     Proprietary <Prtry> [1..1] ± 815
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 815
   QueryName <QryNm> [0..1] Text 815
9.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Reports on limits.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 396 February 2025
```

## File page 397

```text
ReportOrError <RptOrErr> contains one of the following LimitReportOrError5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessReport <BizRpt> [1..1]  398
     CurrentLimit <CurLmt> [0..*]  400
       LimitIdentification <LmtId> [1..1]  C3, C4 401
         SystemIdentification <SysId> [0..1] ± 402
         BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 402
         Type <Tp> [1..1]  403
{Or           Code <Cd> [1..1] CodeSet 403
Or}           Proprietary <Prtry> [1..1] Text 405
         AccountOwner <AcctOwnr> [0..1] ± 405
         AccountIdentification <AcctId> [0..1] ± 406
       LimitOrError <LmtOrErr> [1..1]  406
{Or         Limit <Lmt> [1..1]  407
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
Or}         BusinessError <BizErr> [1..*]  409
           Error <Err> [1..1]  410
{Or             Code <Cd> [1..1] CodeSet 410
Or}             Proprietary <Prtry> [1..1] Text 410
           Description <Desc> [0..1] Text 410
     DefaultLimit <DfltLmt> [0..*]  410
       LimitIdentification <LmtId> [1..1]  C3, C4 411
         SystemIdentification <SysId> [0..1] ± 412
         BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 412
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 397 February 2025
```

