---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>"]
file_pages: [57, 58, 59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1 AccountReport <AcctRpt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 57 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
               Currency <Ccy> [0..1] CodeSet C1 92
             SetStandingOrder <SetStgOrdr> [1..1]  92
               TotalAmount <TtlAmt> [1..1] Amount 93
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 93
               Currency <Ccy> [0..1] CodeSet C1 93
             PendingStandingOrder <PdgStgOrdr> [1..1]  93
               TotalAmount <TtlAmt> [1..1] Amount 94
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 94
               Currency <Ccy> [0..1] CodeSet C1 94
           ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 94
Or}       BusinessError <BizErr> [1..*]  95
         Error <Err> [1..1]  95
{Or           Code <Cd> [1..1] CodeSet 95
Or}           Proprietary <Prtry> [1..1] Text 95
         Description <Desc> [0..1] Text 95
Or}   OperationalError <OprlErr> [1..*]  95
     Error <Err> [1..1]  96
{Or       Code <Cd> [1..1] CodeSet 96
Or}       Proprietary <Prtry> [1..1] Text 96
     Description <Desc> [0..1] Text 96
3.4.2.1  AccountReport <AcctRpt>
Presence: [1..*]
Definition: Reports either on the account information or on a business error.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 57 February 2025
```

## File page 58

```text
AccountReport <AcctRpt> contains the following AccountReport35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] ± 60
   AccountOrError <AcctOrErr> [1..1]  60
{Or     Account <Acct> [1..1]  C5 63
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
{Or             Code <Cd> [1..1] CodeSet 74
Or}             Proprietary <Prtry> [1..1] Text 79
           Status <Sts> [0..1] CodeSet 80
           ValueDate <ValDt> [0..1] ± 80
           NumberOfPayments <NbOfPmts> [0..1] Quantity 80
       StandingOrder <StgOrdr> [0..*]  80
         Amount <Amt> [1..1] ± 82
         CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 82
         Currency <Ccy> [0..1] CodeSet C1 82
         Type <Tp> [0..1]  83
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 58 February 2025
```

## File page 59

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 83
Or}           Proprietary <Prtry> [1..1] ± 83
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
{Or           Time <Tm> [1..1] Time 87
Or}           Event <Evt> [1..1]  87
{Or             Code <Cd> [1..1] CodeSet 87
Or}             Proprietary <Prtry> [1..1] Text 87
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
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
             Currency <Ccy> [0..1] CodeSet C1 92
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 59 February 2025
```

