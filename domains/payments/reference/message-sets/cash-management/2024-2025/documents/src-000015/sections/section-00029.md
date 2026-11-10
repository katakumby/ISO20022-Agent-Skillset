---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.2 Structure"]
file_pages: [50, 51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 50 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RtrAcct> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 54
   ReportOrError <RptOrErr> [1..1]  54
{Or     AccountReport <AcctRpt> [1..*]  57
       AccountIdentification <AcctId> [1..1] ± 60
       AccountOrError <AcctOrErr> [1..1]  60
{Or         Account <Acct> [1..1]  C5 63
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
{Or                 Code <Cd> [1..1] CodeSet 74
Or}                 Proprietary <Prtry> [1..1] Text 79
               Status <Sts> [0..1] CodeSet 80
               ValueDate <ValDt> [0..1] ± 80
               NumberOfPayments <NbOfPmts> [0..1] Quantity 80
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 50 February 2025
```

## File page 51

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           StandingOrder <StgOrdr> [0..*]  80
             Amount <Amt> [1..1] ± 82
             CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 82
             Currency <Ccy> [0..1] CodeSet C1 82
             Type <Tp> [0..1]  83
{Or               Code <Cd> [1..1] CodeSet 83
Or}               Proprietary <Prtry> [1..1] ± 83
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
{Or               Time <Tm> [1..1] Time 87
Or}               Event <Evt> [1..1]  87
{Or                 Code <Cd> [1..1] CodeSet 87
Or}                 Proprietary <Prtry> [1..1] Text 87
             Creditor <Cdtr> [0..1] ± 87
             CreditorAccount <CdtrAcct> [0..1] ± C10, C9 88
             Debtor <Dbtr> [0..1] ± 89
             DebtorAccount <DbtrAcct> [0..1] ± C10, C9 89
             TotalsPerStandingOrder <TtlsPerStgOrdr> [0..1]  90
               SetPredefinedOrder <SetPrdfndOrdr> [1..1]  90
                 TotalAmount <TtlAmt> [1..1] Amount 91
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 91
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 51 February 2025
```

