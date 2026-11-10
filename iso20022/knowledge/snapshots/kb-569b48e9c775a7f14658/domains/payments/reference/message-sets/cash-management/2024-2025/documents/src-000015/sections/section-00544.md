---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks"]
file_pages: [711, 712, 713]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 711 to 713.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 711

```text
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
31.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
31.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader6" on page 820 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 820
   CreationDateTime <CreDtTm> [0..1] DateTime 820
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 820
   QueryName <QryNm> [0..1] Text 821
   RequestType <ReqTp> [0..1]  821
{Or     Code <Cd> [1..1] CodeSet 821
Or}     Proprietary <Prtry> [1..1] ± 821
31.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Reports on standing orders.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 711 February 2025
```

## File page 712

```text
ReportOrError <RptOrErr> contains one of the following StandingOrderOrError9Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Report <Rpt> [1..*]  714
     StandingOrderIdentification <StgOrdrId> [1..1]  716
       Identification <Id> [0..1] Text 717
       Account <Acct> [1..1] ± C8, C7 717
       AccountOwner <AcctOwnr> [0..1] ± 717
     StandingOrderOrError <StgOrdrOrErr> [1..1]  718
{Or       StandingOrder <StgOrdr> [1..1]  720
         Amount <Amt> [1..1] ± 722
         CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 722
         Currency <Ccy> [0..1] CodeSet C1 722
         Type <Tp> [0..1]  723
{Or           Code <Cd> [1..1] CodeSet 723
Or}           Proprietary <Prtry> [1..1] ± 723
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
{Or           Time <Tm> [1..1] Time 727
Or}           Event <Evt> [1..1]  727
{Or             Code <Cd> [1..1] CodeSet 727
Or}             Proprietary <Prtry> [1..1] Text 727
         Creditor <Cdtr> [0..1] ± 727
         CreditorAccount <CdtrAcct> [0..1] ± C8, C7 728
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 712 February 2025
```

## File page 713

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Debtor <Dbtr> [0..1] ± 729
         DebtorAccount <DbtrAcct> [0..1] ± C8, C7 729
         TotalsPerStandingOrder <TtlsPerStgOrdr> [0..1]  730
           SetPredefinedOrder <SetPrdfndOrdr> [1..1]  730
             TotalAmount <TtlAmt> [1..1] Amount 731
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 731
             Currency <Ccy> [0..1] CodeSet C1 731
           PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  731
             TotalAmount <TtlAmt> [1..1] Amount 732
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 732
             Currency <Ccy> [0..1] CodeSet C1 732
           SetStandingOrder <SetStgOrdr> [1..1]  732
             TotalAmount <TtlAmt> [1..1] Amount 733
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 733
             Currency <Ccy> [0..1] CodeSet C1 733
           PendingStandingOrder <PdgStgOrdr> [1..1]  733
             TotalAmount <TtlAmt> [1..1] Amount 734
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 734
             Currency <Ccy> [0..1] CodeSet C1 734
         ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 734
Or}       BusinessError <BizErr> [1..*]  735
         Error <Err> [1..1]  735
{Or           Code <Cd> [1..1] CodeSet 735
Or}           Proprietary <Prtry> [1..1] Text 735
         Description <Desc> [0..1] Text 735
Or}   OperationalError <OprlErr> [1..*]  735
     Error <Err> [1..1]  736
{Or       Code <Cd> [1..1] CodeSet 736
Or}       Proprietary <Prtry> [1..1] Text 736
     Description <Desc> [0..1] Text 736
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 713 February 2025
```

