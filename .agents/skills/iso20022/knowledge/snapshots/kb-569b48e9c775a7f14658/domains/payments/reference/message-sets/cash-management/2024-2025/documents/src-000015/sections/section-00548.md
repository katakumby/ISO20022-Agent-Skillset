---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>"]
file_pages: [718, 719]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 718 to 719.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 718

```text
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
31.4.2.1.2  StandingOrderOrError <StgOrdrOrErr>
Presence: [1..1]
Definition: Requested information on the standing order or business error when information has not
been found.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 718 February 2025
```

## File page 719

```text
StandingOrderOrError <StgOrdrOrErr> contains one of the following
StandingOrderOrError10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StandingOrder <StgOrdr> [1..1]  720
     Amount <Amt> [1..1] ± 722
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 722
     Currency <Ccy> [0..1] CodeSet C1 722
     Type <Tp> [0..1]  723
{Or       Code <Cd> [1..1] CodeSet 723
Or}       Proprietary <Prtry> [1..1] ± 723
     AssociatedPoolAccount <AssoctdPoolAcct> [0..1] ± 724
     Reference <Ref> [0..1] Text 724
     Frequency <Frqcy> [0..1] CodeSet 724
     ValidityPeriod <VldtyPrd> [0..1]  724
       FromDate <FrDt> [1..1] Date 725
       ToDate <ToDt> [0..1] Date 725
     SystemMember <SysMmb> [0..1] ± 725
     ResponsibleParty <RspnsblPty> [0..1] ± 725
     LinkSetIdentification <LkSetId> [0..1] Text 726
     LinkSetOrderIdentification <LkSetOrdrId> [0..1] Text 726
     LinkSetOrderSequence <LkSetOrdrSeq> [0..1] Quantity 726
     ExecutionType <ExctnTp> [0..1]  726
{Or       Time <Tm> [1..1] Time 727
Or}       Event <Evt> [1..1]  727
{Or         Code <Cd> [1..1] CodeSet 727
Or}         Proprietary <Prtry> [1..1] Text 727
     Creditor <Cdtr> [0..1] ± 727
     CreditorAccount <CdtrAcct> [0..1] ± C8, C7 728
     Debtor <Dbtr> [0..1] ± 729
     DebtorAccount <DbtrAcct> [0..1] ± C8, C7 729
     TotalsPerStandingOrder <TtlsPerStgOrdr> [0..1]  730
       SetPredefinedOrder <SetPrdfndOrdr> [1..1]  730
         TotalAmount <TtlAmt> [1..1] Amount 731
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 719 February 2025
```

