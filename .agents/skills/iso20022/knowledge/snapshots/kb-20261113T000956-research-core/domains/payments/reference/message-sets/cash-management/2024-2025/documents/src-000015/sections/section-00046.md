---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.9 CurrentBilateralLimit <CurBilLmt>", "3.4.2.1.2.1.9.4 BilateralBalance <BilBal>", "3.4.2.1.2.1.9.4.4 Status <Sts>"]
file_pages: [80, 81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.9.4.4 Status <Sts>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 80 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Datatype: "Max35Text" on page 889
3.4.2.1.2.1.9.4.4  Status <Sts>
Presence: [0..1]
Definition: Current status of a cash balance.
Datatype: "BalanceStatus1Code" on page 850
CodeName Name Definition
PDNG Pending Balance corresponding to the pending
transactions.
STLD Settled Final status of a transaction when the
associated transfer of cash has been
successfully processed.
3.4.2.1.2.1.9.4.5  ValueDate <ValDt>
Presence: [0..1]
Definition: Date and time at which the balance is or will be available.
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
3.4.2.1.2.1.9.4.6  NumberOfPayments <NbOfPmts>
Presence: [0..1]
Definition: Number of payments taken into account for the calculation of the cash balance value.
Datatype: "Number" on page 886
3.4.2.1.2.1.10  StandingOrder <StgOrdr>
Presence: [0..*]
Definition: Instruction given by a party that has explicit authority to instruct a debit on the account, that is
either the debtor or originating party, to the debtor agent, to process liquidity transfers at specified
intervals during an implicit or explicit period of time. A standing order is given once and is valid for an
open or closed period of time.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 80 February 2025
```

## File page 81

```text
StandingOrder <StgOrdr> contains the following StandingOrder11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 82
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 82
   Currency <Ccy> [0..1] CodeSet C1 82
   Type <Tp> [0..1]  83
{Or     Code <Cd> [1..1] CodeSet 83
Or}     Proprietary <Prtry> [1..1] ± 83
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
{Or     Time <Tm> [1..1] Time 87
Or}     Event <Evt> [1..1]  87
{Or       Code <Cd> [1..1] CodeSet 87
Or}       Proprietary <Prtry> [1..1] Text 87
   Creditor <Cdtr> [0..1] ± 87
   CreditorAccount <CdtrAcct> [0..1] ± C10, C9 88
   Debtor <Dbtr> [0..1] ± 89
   DebtorAccount <DbtrAcct> [0..1] ± C10, C9 89
   TotalsPerStandingOrder <TtlsPerStgOrdr> [0..1]  90
     SetPredefinedOrder <SetPrdfndOrdr> [1..1]  90
       TotalAmount <TtlAmt> [1..1] Amount 91
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 91
       Currency <Ccy> [0..1] CodeSet C1 91
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 81 February 2025
```

