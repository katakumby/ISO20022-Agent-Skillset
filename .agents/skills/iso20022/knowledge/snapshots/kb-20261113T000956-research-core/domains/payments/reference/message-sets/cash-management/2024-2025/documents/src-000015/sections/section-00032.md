---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.1 MessageHeader <MsgHdr>"]
file_pages: [54, 55, 56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.1 MessageHeader <MsgHdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 54 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 54

```text
3.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
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
3.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Reports on accounts.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 54 February 2025
```

## File page 55

```text
ReportOrError <RptOrErr> contains one of the following AccountOrOperationalError6Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountReport <AcctRpt> [1..*]  57
     AccountIdentification <AcctId> [1..1] ± 60
     AccountOrError <AcctOrErr> [1..1]  60
{Or       Account <Acct> [1..1]  C5 63
         Name <Nm> [0..1] Text 66
         Type <Tp> [0..1] ± 66
         Currency <Ccy> [0..1] CodeSet C2 66
         Proxy <Prxy> [0..1] ± 67
         CurrentMultilateralLimit <CurMulLmt> [0..1]  67
           Amount <Amt> [1..1] ± 67
           CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 68
         Owner <Ownr> [0..1] ± 68
         Servicer <Svcr> [0..1] ± 69
         MultilateralBalance <MulBal> [0..*] ± 70
         CurrentBilateralLimit <CurBilLmt> [0..*]  71
           CounterpartyIdentification <CtrPtyId> [1..1] ± 72
           LimitAmount <LmtAmt> [1..1] ± 73
           CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 73
           BilateralBalance <BilBal> [0..*]  73
             Amount <Amt> [1..1] Amount 73
             CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 74
             Type <Tp> [0..1]  74
{Or               Code <Cd> [1..1] CodeSet 74
Or}               Proprietary <Prtry> [1..1] Text 79
             Status <Sts> [0..1] CodeSet 80
             ValueDate <ValDt> [0..1] ± 80
             NumberOfPayments <NbOfPmts> [0..1] Quantity 80
         StandingOrder <StgOrdr> [0..*]  80
           Amount <Amt> [1..1] ± 82
           CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 82
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 55 February 2025
```

## File page 56

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Currency <Ccy> [0..1] CodeSet C1 82
           Type <Tp> [0..1]  83
{Or             Code <Cd> [1..1] CodeSet 83
Or}             Proprietary <Prtry> [1..1] ± 83
           AssociatedPoolAccount <AssoctdPoolAcct> [0..1] ± 84
           Reference <Ref> [0..1] Text 84
           Frequency <Frqcy> [0..1] CodeSet 84
           ValidityPeriod <VldtyPrd> [0..1]  84
             FromDate <FrDt> [1..1] Date 85
             ToDate <ToDt> [0..1] Date 85
           SystemMember <SysMmb> [0..1] ± 85
           ResponsibleParty <RspnsblPty> [0..1] ± 85
           LinkSetIdentification <LkSetId> [0..1] Text 86
           LinkSetOrderIdentification <LkSetOrdrId> [0..1] Text 86
           LinkSetOrderSequence <LkSetOrdrSeq> [0..1] Quantity 86
           ExecutionType <ExctnTp> [0..1]  86
{Or             Time <Tm> [1..1] Time 87
Or}             Event <Evt> [1..1]  87
{Or               Code <Cd> [1..1] CodeSet 87
Or}               Proprietary <Prtry> [1..1] Text 87
           Creditor <Cdtr> [0..1] ± 87
           CreditorAccount <CdtrAcct> [0..1] ± C10, C9 88
           Debtor <Dbtr> [0..1] ± 89
           DebtorAccount <DbtrAcct> [0..1] ± C10, C9 89
           TotalsPerStandingOrder <TtlsPerStgOrdr> [0..1]  90
             SetPredefinedOrder <SetPrdfndOrdr> [1..1]  90
               TotalAmount <TtlAmt> [1..1] Amount 91
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 91
               Currency <Ccy> [0..1] CodeSet C1 91
             PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  91
               TotalAmount <TtlAmt> [1..1] Amount 92
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 56 February 2025
```

