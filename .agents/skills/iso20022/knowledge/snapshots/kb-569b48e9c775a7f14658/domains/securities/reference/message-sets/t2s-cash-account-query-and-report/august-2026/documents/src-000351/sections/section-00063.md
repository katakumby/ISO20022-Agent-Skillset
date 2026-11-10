---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>"]
file_pages: [70, 71, 72, 73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4 ReportOrError <RptOrErr>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 70 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
LegalRepresentative <LglRprtv> contains the following elements (see "PartyIdentification274" on
page 148 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 149
   PostalAddress <PstlAdr> [0..1] ± 149
   Identification <Id> [0..1]  150
     DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  151
       BirthDate <BirthDt> [1..1] Date 151
       ProvinceOfBirth <PrvcOfBirth> [0..1] Text 151
       CityOfBirth <CityOfBirth> [1..1] Text 151
       CountryOfBirth <CtryOfBirth> [1..1] CodeSet C7 152
     Other <Othr> [0..*]  152
       Identification <Id> [1..1] Text 152
       SchemeName <SchmeNm> [0..1]  152
{Or         Code <Cd> [1..1] CodeSet 153
Or}         Proprietary <Prtry> [1..1] Text 153
       Issuer <Issr> [0..1] Text 153
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C7 153
   ContactDetails <CtctDtls> [0..1] ± 153
3.4.4 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Contains the requested report, or the error that occurred during processing.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 70 August 2026
```

## File page 71

```text
ReportOrError <RptOrErr> contains one of the following AccountReportOrError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Error <Err> [1..*]  74
     Error <Err> [1..1]  74
{Or       Code <Cd> [1..1] CodeSet 74
Or}       Proprietary <Prtry> [1..1] Text 74
     Description <Desc> [0..1] Text 74
Or}   AccountReport <AcctRpt> [1..*]  C5, C6 75
     Account <Acct> [1..1]  79
       Identification <Id> [0..1] ± 81
       Name <Nm> [0..1] Text 81
       Status <Sts> [0..1] CodeSet 81
       Type <Tp> [0..1] ± 81
       Currency <Ccy> [1..1] CodeSet C1 82
       Proxy <Prxy> [0..1] ± 82
       MonthlyPaymentValue <MnthlyPmtVal> [0..1] Amount 82
       MonthlyReceivedValue <MnthlyRcvdVal> [0..1] Amount 82
       MonthlyTransactionNumber <MnthlyTxNb> [0..1] Text 82
       AverageBalance <AvrgBal> [0..1] Amount 82
       AccountPurpose <AcctPurp> [0..1] Text 83
       FloorNotificationAmount <FlrNtfctnAmt> [0..1] Amount 83
       CeilingNotificationAmount <ClngNtfctnAmt> [0..1] Amount 83
       StatementFrequencyAndFormat
<StmtFrqcyAndFrmt>
[0..*]  83
         Frequency <Frqcy> [1..1] CodeSet 83
         CommunicationMethod <ComMtd> [1..1]  84
{Or           Code <Cd> [1..1] CodeSet 84
Or}           Proprietary <Prtry> [1..1] Text 85
         DeliveryAddress <DlvryAdr> [1..1] Text 85
         Format <Frmt> [1..1]  85
{Or           Code <Cd> [1..1] CodeSet 85
Or}           Proprietary <Prtry> [1..1] Text 85
       ClosingDate <ClsgDt> [0..1] Date 85
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 71 August 2026
```

## File page 72

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Restriction <Rstrctn> [0..*]  85
         RestrictionType <RstrctnTp> [1..1]  86
{Or           Code <Cd> [1..1] Text 86
Or}           Proprietary <Prtry> [1..1] ± 86
         ValidFrom <VldFr> [1..1] DateTime 86
         ValidUntil <VldUntil> [0..1] DateTime 87
       OpeningDate <OpngDt> [0..1] Date 87
     UnderlyingMasterAgreement <UndrlygMstrAgrmt> [0..1]  87
       Reference <Ref> [1..1] Text 87
       SignOffDate <SgnOffDt> [0..1] Date 87
       Version <Vrsn> [0..1] Text 87
     ContractDates <CtrctDts> [0..1]  87
       TargetGoLiveDate <TrgtGoLiveDt> [0..1] Date 88
       TargetClosingDate <TrgtClsgDt> [0..1] Date 88
       GoLiveDate <GoLiveDt> [0..1] Date 88
       ClosingDate <ClsgDt> [0..1] Date 88
       UrgencyFlag <UrgcyFlg> [0..1] Indicator 88
       RemovalIndicator <RmvlInd> [0..1] Indicator 89
     Mandate <Mndt> [0..*]  89
       Identification <Id> [1..1] Text 90
       ApplicableChannel <AplblChanl> [1..*]  91
{Or         Code <Cd> [1..1] CodeSet 91
Or}         Proprietary <Prtry> [1..1] Text 91
       RequiredSignatureNumber <ReqrdSgntrNb> [1..1] Text 91
       SignatureOrderIndicator <SgntrOrdrInd> [1..1] Indicator 91
       MandateHolder <MndtHldr> [0..*]  92
         PartyOrGroup <PtyOrGrp> [1..1]  92
{Or           GroupIdentification <GrpId> [1..1] Text 92
Or}           Party <Pty> [1..1]  93
             Party <Pty> [1..1] ± 93
             Certificate <Cert> [0..1] Binary 94
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 72 August 2026
```

## File page 73

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SignatureOrder <SgntrOrdr> [0..1] Text 95
         Authorisation <Authstn> [1..1]  95
           MaximumAmountByTransaction <MaxAmtByTx> [0..1]  95
{Or             Amount <Amt> [1..1] Amount C1, C8 95
Or}             NotLimited <NotLtd> [1..1] Text 96
           MaximumAmountByPeriod <MaxAmtByPrd> [0..*]  96
             MaximumAmount <MaxAmt> [1..1] Amount C1, C8 96
             NumberOfDays <NbOfDays> [1..1] Text 97
           MaximumAmountByBulkSubmission
<MaxAmtByBlkSubmissn>
[0..1]  97
{Or             Amount <Amt> [1..1] Amount C1, C8 97
Or}             NotLimited <NotLtd> [1..1] Text 97
       BankOperation <BkOpr> [1..*] ± C9, C10 97
       StartDate <StartDt> [0..1] Date 98
       EndDate <EndDt> [0..1] Date 98
     ReferenceAccount <RefAcct> [0..1] ± C13,
C12
98
     BalanceTransferAccount <BalTrfAcct> [0..1]  99
       Identification <Id> [1..1] ± 99
       Currency <Ccy> [1..1] CodeSet C1 100
     TransferAccountServicerIdentification
<TrfAcctSvcrId>
[0..1] ± 100
     AccountOwner <AcctOwnr> [0..1]  100
       AnyBIC <AnyBIC> [0..1] IdentifierSet C3 101
       LEI <LEI> [0..1] IdentifierSet 101
       Other <Othr> [0..*]  101
         Identification <Id> [1..1] Text 102
         SchemeName <SchmeNm> [0..1]  102
{Or           Code <Cd> [1..1] CodeSet 102
Or}           Proprietary <Prtry> [1..1] Text 102
         Issuer <Issr> [0..1] Text 102
     Proprietary <Prtry> [0..*] ± 102
     Group <Grp> [0..*]  103
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 73 August 2026
```

