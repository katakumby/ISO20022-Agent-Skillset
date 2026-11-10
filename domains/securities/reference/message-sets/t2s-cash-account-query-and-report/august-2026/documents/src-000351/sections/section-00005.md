---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.2 Structure"]
file_pages: [5, 6, 7, 8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.2 Structure

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 5 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctQryList> [1..1]  
   References <Refs> [1..1]  9
     MessageIdentification <MsgId> [1..1] ± 9
     ProcessIdentification <PrcId> [1..1] ± 10
     AttachedDocumentName <AttchdDocNm> [0..*] Text 10
   From <Fr> [0..1]  10
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 11
     LEI <LEI> [0..1] IdentifierSet 11
     Other <Othr> [0..*]  11
       Identification <Id> [1..1] Text 12
       SchemeName <SchmeNm> [0..1]  12
{Or         Code <Cd> [1..1] CodeSet 12
Or}         Proprietary <Prtry> [1..1] Text 12
       Issuer <Issr> [0..1] Text 12
   AccountServicerIdentification <AcctSvcrId> [1..1] ± 13
   Organisation <Org> [0..1]  13
     FullLegalName <FullLglNm> [1..1] Text 14
     TradingName <TradgNm> [0..1] Text 14
     CountryOfOperation <CtryOfOpr> [1..1] CodeSet C4 15
     RegistrationDate <RegnDt> [0..1] Date 15
     OperationalAddress <OprlAdr> [0..1] ± 15
     BusinessAddress <BizAdr> [0..1] ± 16
     LegalAddress <LglAdr> [1..1] ± 17
     BillingAddress <BllgAdr> [0..1] ± 18
     OrganisationIdentification <OrgId> [1..1]  19
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 20
       LEI <LEI> [0..1] IdentifierSet 20
       Other <Othr> [0..*]  20
         Identification <Id> [1..1] Text 21
         SchemeName <SchmeNm> [0..1]  21
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 5 August 2026
```

## File page 6

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 21
Or}           Proprietary <Prtry> [1..1] Text 21
         Issuer <Issr> [0..1] Text 21
     RepresentativeOfficer <RprtvOffcr> [0..*] ± 21
     TreasuryManager <TrsrMgr> [0..1] ± 22
     MainMandateHolder <MainMndtHldr> [0..*] ± 23
     Sender <Sndr> [0..*] ± 24
     LegalRepresentative <LglRprtv> [0..*] ± 25
   AccountSearchCriteria <AcctSchCrit> [1..1]  26
     Identification <Id> [0..1] ± 28
     Name <Nm> [0..1] Text 29
     Status <Sts> [0..1] CodeSet 29
     Type <Tp> [0..1] ± 29
     Currency <Ccy> [0..1] CodeSet C1 29
     Proxy <Prxy> [0..1] ± 30
     MinimumMonthlyPaymentValue <MinMnthlyPmtVal> [0..1] Amount 30
     MaximumMonthlyPaymentValue <MaxMnthlyPmtVal> [0..1] Amount 30
     MinimumMonthlyReceivedValue <MinMnthlyRcvdVal> [0..1] Amount 30
     MaximumMonthlyReceivedValue <MaxMnthlyRcvdVal> [0..1] Amount 31
     MinimumMonthlyTransactionNumber <MinMnthlyTxNb> [0..1] Text 31
     MaximumMonthlyTransactionNumber <MaxMnthlyTxNb> [0..1] Text 31
     MinimumAverageBalance <MinAvrgBal> [0..1] Amount 31
     MaximumAverageBalance <MaxAvrgBal> [0..1] Amount 31
     AccountPurpose <AcctPurp> [0..1] Text 31
     MinimumFloorNotificationAmount <MinFlrNtfctnAmt> [0..1] Amount 31
     MaximumFloorNotificationAmount <MaxFlrNtfctnAmt> [0..1] Amount 31
     MinimumCeilingNotificationAmount <MinClngNtfctnAmt> [0..1] Amount 32
     MaximumCeilingNotificationAmount <MaxClngNtfctnAmt> [0..1] Amount 32
     StatementFrequencyAndFormat <StmtFrqcyAndFrmt> [0..*]  32
       Frequency <Frqcy> [1..1] CodeSet 32
       CommunicationMethod <ComMtd> [1..1]  33
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 6 August 2026
```

## File page 7

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 33
Or}         Proprietary <Prtry> [1..1] Text 33
       DeliveryAddress <DlvryAdr> [1..1] Text 34
       Format <Frmt> [1..1]  34
{Or         Code <Cd> [1..1] CodeSet 34
Or}         Proprietary <Prtry> [1..1] Text 34
     Restriction <Rstrctn> [0..*]  34
       RestrictionType <RstrctnTp> [1..1]  35
{Or         Code <Cd> [1..1] Text 35
Or}         Proprietary <Prtry> [1..1] ± 35
       ValidFrom <VldFr> [1..1] DateTime 35
       ValidUntil <VldUntil> [0..1] DateTime 35
     ClosingDate <ClsgDt> [0..1]  35
{Or       FromDate <FrDt> [1..1] Date 36
Or       ToDate <ToDt> [1..1] Date 36
Or       FromToDate <FrToDt> [1..1] ± 36
Or       EqualDate <EQDt> [1..1] Date 36
Or}       NotEqualDate <NEQDt> [1..1] Date 36
     OpeningDate <OpngDt> [0..1]  36
{Or       FromDate <FrDt> [1..1] Date 37
Or       ToDate <ToDt> [1..1] Date 37
Or       FromToDate <FrToDt> [1..1] ± 37
Or       EqualDate <EQDt> [1..1] Date 37
Or}       NotEqualDate <NEQDt> [1..1] Date 37
     ReferenceAccountIdentification <RefAcctId> [0..1] ± 38
     Proprietary <Prtry> [0..*] ± 38
     AccountOwner <AcctOwnr> [0..1]  38
       AnyBIC <AnyBIC> [0..1] IdentifierSet C2 39
       LEI <LEI> [0..1] IdentifierSet 39
       Other <Othr> [0..*]  39
         Identification <Id> [1..1] Text 39
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 7 August 2026
```

## File page 8

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         SchemeName <SchmeNm> [0..1]  39
{Or           Code <Cd> [1..1] CodeSet 40
Or}           Proprietary <Prtry> [1..1] Text 40
         Issuer <Issr> [0..1] Text 40
   AccountReturnCriteria <AcctRtrCrit> [0..1]  40
     Identification <Id> [1..1] Indicator 41
     Name <Nm> [1..1] Indicator 41
     Status <Sts> [1..1] Indicator 42
     Type <Tp> [1..1] Indicator 42
     Currency <Ccy> [1..1] Indicator 42
     MonthlyPaymentValue <MnthlyPmtVal> [1..1] Indicator 42
     MonthlyReceivedValue <MnthlyRcvdVal> [1..1] Indicator 42
     MonthlyTransactionNumber <MnthlyTxNb> [1..1] Indicator 43
     AverageBalance <AvrgBal> [1..1] Indicator 43
     AccountPurpose <AcctPurp> [1..1] Indicator 43
     FloorNotificationAmount <FlrNtfctnAmt> [1..1] Indicator 43
     CeilingNotificationAmount <ClngNtfctnAmt> [1..1] Indicator 43
     StatementCycle <StmtCycl> [1..1] Indicator 44
     ClosingDate <ClsgDt> [1..1] Indicator 44
     Restriction <Rstrctn> [1..1] Indicator 44
     OpeningDate <OpngDt> [1..1] Indicator 44
     AccountOwner <AcctOwnr> [1..1] Indicator 44
     ReferenceAccount <RefAcct> [1..1] Indicator 44
     Proprietary <Prtry> [0..*]  45
       SchemeName <SchmeNm> [0..1] Text 45
       Issuer <Issr> [0..1] Text 45
   DigitalSignature <DgtlSgntr> [0..*]  45
     Party <Pty> [1..1] ± 45
     Signature <Sgntr> [1..1] (External Schema) 46
   SupplementaryData <SplmtryData> [0..*] ± C6 47
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 8 August 2026
```

