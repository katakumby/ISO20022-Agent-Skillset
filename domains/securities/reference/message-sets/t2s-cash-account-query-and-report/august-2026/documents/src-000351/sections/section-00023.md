---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>"]
file_pages: [26, 27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5 AccountSearchCriteria <AcctSchCrit>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 26 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

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
2.4.5 AccountSearchCriteria <AcctSchCrit>
Presence: [1..1]
Definition: Contains the criteria that must be used to select the requested accounts.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 26 August 2026
```

## File page 27

```text
AccountSearchCriteria <AcctSchCrit> contains the following CustomerAccount10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   MinimumMonthlyTransactionNumber
<MinMnthlyTxNb>
[0..1] Text 31
   MaximumMonthlyTransactionNumber
<MaxMnthlyTxNb>
[0..1] Text 31
   MinimumAverageBalance <MinAvrgBal> [0..1] Amount 31
   MaximumAverageBalance <MaxAvrgBal> [0..1] Amount 31
   AccountPurpose <AcctPurp> [0..1] Text 31
   MinimumFloorNotificationAmount <MinFlrNtfctnAmt> [0..1] Amount 31
   MaximumFloorNotificationAmount <MaxFlrNtfctnAmt> [0..1] Amount 31
   MinimumCeilingNotificationAmount
<MinClngNtfctnAmt>
[0..1] Amount 32
   MaximumCeilingNotificationAmount
<MaxClngNtfctnAmt>
[0..1] Amount 32
   StatementFrequencyAndFormat <StmtFrqcyAndFrmt> [0..*]  32
     Frequency <Frqcy> [1..1] CodeSet 32
     CommunicationMethod <ComMtd> [1..1]  33
{Or       Code <Cd> [1..1] CodeSet 33
Or}       Proprietary <Prtry> [1..1] Text 33
     DeliveryAddress <DlvryAdr> [1..1] Text 34
     Format <Frmt> [1..1]  34
{Or       Code <Cd> [1..1] CodeSet 34
Or}       Proprietary <Prtry> [1..1] Text 34
   Restriction <Rstrctn> [0..*]  34
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 27 August 2026
```

