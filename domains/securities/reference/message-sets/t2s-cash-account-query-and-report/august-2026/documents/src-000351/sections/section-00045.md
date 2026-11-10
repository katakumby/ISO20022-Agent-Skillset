---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.2 Structure"]
file_pages: [49, 50, 51, 52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.2 Structure

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 49 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctListRpt> [1..1]  
   References <Refs> [1..1]  54
     RequestType <ReqTp> [1..1] CodeSet 55
     MessageIdentification <MsgId> [1..1] ± 55
     ProcessIdentification <PrcId> [1..1] ± 55
     AcknowledgedMessageIdentification <AckdMsgId> [0..*] ± 56
     Status <Sts> [0..1] Text 56
     AttachedDocumentName <AttchdDocNm> [0..*] Text 56
   AccountServicerIdentification <AcctSvcrId> [1..1] ± 56
   Organisation <Org> [0..1]  57
     FullLegalName <FullLglNm> [1..1] Text 58
     TradingName <TradgNm> [0..1] Text 58
     CountryOfOperation <CtryOfOpr> [1..1] CodeSet C7 59
     RegistrationDate <RegnDt> [0..1] Date 59
     OperationalAddress <OprlAdr> [0..1] ± 59
     BusinessAddress <BizAdr> [0..1] ± 60
     LegalAddress <LglAdr> [1..1] ± 61
     BillingAddress <BllgAdr> [0..1] ± 62
     OrganisationIdentification <OrgId> [1..1]  63
       AnyBIC <AnyBIC> [0..1] IdentifierSet C3 64
       LEI <LEI> [0..1] IdentifierSet 64
       Other <Othr> [0..*]  64
         Identification <Id> [1..1] Text 65
         SchemeName <SchmeNm> [0..1]  65
{Or           Code <Cd> [1..1] CodeSet 65
Or}           Proprietary <Prtry> [1..1] Text 65
         Issuer <Issr> [0..1] Text 65
     RepresentativeOfficer <RprtvOffcr> [0..*] ± 65
     TreasuryManager <TrsrMgr> [0..1] ± 66
     MainMandateHolder <MainMndtHldr> [0..*] ± 67
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 49 August 2026
```

## File page 50

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     Sender <Sndr> [0..*] ± 68
     LegalRepresentative <LglRprtv> [0..*] ± 69
   ReportOrError <RptOrErr> [1..1]  70
{Or     Error <Err> [1..*]  74
       Error <Err> [1..1]  74
{Or         Code <Cd> [1..1] CodeSet 74
Or}         Proprietary <Prtry> [1..1] Text 74
       Description <Desc> [0..1] Text 74
Or}     AccountReport <AcctRpt> [1..*]  C5, C6 75
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
         StatementFrequencyAndFormat <StmtFrqcyAndFrmt> [0..*]  83
           Frequency <Frqcy> [1..1] CodeSet 83
           CommunicationMethod <ComMtd> [1..1]  84
{Or             Code <Cd> [1..1] CodeSet 84
Or}             Proprietary <Prtry> [1..1] Text 85
           DeliveryAddress <DlvryAdr> [1..1] Text 85
           Format <Frmt> [1..1]  85
{Or             Code <Cd> [1..1] CodeSet 85
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 50 August 2026
```

## File page 51

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] Text 85
         ClosingDate <ClsgDt> [0..1] Date 85
         Restriction <Rstrctn> [0..*]  85
           RestrictionType <RstrctnTp> [1..1]  86
{Or             Code <Cd> [1..1] Text 86
Or}             Proprietary <Prtry> [1..1] ± 86
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
{Or           Code <Cd> [1..1] CodeSet 91
Or}           Proprietary <Prtry> [1..1] Text 91
         RequiredSignatureNumber <ReqrdSgntrNb> [1..1] Text 91
         SignatureOrderIndicator <SgntrOrdrInd> [1..1] Indicator 91
         MandateHolder <MndtHldr> [0..*]  92
           PartyOrGroup <PtyOrGrp> [1..1]  92
{Or             GroupIdentification <GrpId> [1..1] Text 92
Or}             Party <Pty> [1..1]  93
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 51 August 2026
```

## File page 52

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Party <Pty> [1..1] ± 93
               Certificate <Cert> [0..1] Binary 94
           SignatureOrder <SgntrOrdr> [0..1] Text 95
           Authorisation <Authstn> [1..1]  95
             MaximumAmountByTransaction <MaxAmtByTx> [0..1]  95
{Or               Amount <Amt> [1..1] Amount C1, C8 95
Or}               NotLimited <NotLtd> [1..1] Text 96
             MaximumAmountByPeriod <MaxAmtByPrd> [0..*]  96
               MaximumAmount <MaxAmt> [1..1] Amount C1, C8 96
               NumberOfDays <NbOfDays> [1..1] Text 97
             MaximumAmountByBulkSubmission
<MaxAmtByBlkSubmissn>
[0..1]  97
{Or               Amount <Amt> [1..1] Amount C1, C8 97
Or}               NotLimited <NotLtd> [1..1] Text 97
         BankOperation <BkOpr> [1..*] ± C9, C10 97
         StartDate <StartDt> [0..1] Date 98
         EndDate <EndDt> [0..1] Date 98
       ReferenceAccount <RefAcct> [0..1] ± C13,
C12
98
       BalanceTransferAccount <BalTrfAcct> [0..1]  99
         Identification <Id> [1..1] ± 99
         Currency <Ccy> [1..1] CodeSet C1 100
       TransferAccountServicerIdentification <TrfAcctSvcrId> [0..1] ± 100
       AccountOwner <AcctOwnr> [0..1]  100
         AnyBIC <AnyBIC> [0..1] IdentifierSet C3 101
         LEI <LEI> [0..1] IdentifierSet 101
         Other <Othr> [0..*]  101
           Identification <Id> [1..1] Text 102
           SchemeName <SchmeNm> [0..1]  102
{Or             Code <Cd> [1..1] CodeSet 102
Or}             Proprietary <Prtry> [1..1] Text 102
           Issuer <Issr> [0..1] Text 102
       Proprietary <Prtry> [0..*] ± 102
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 52 August 2026
```

