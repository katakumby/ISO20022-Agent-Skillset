---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.2 Structure"]
file_pages: [15, 16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 15 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <GetAcct> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 18
   AccountQueryDefinition <AcctQryDef> [0..1]  18
     QueryType <QryTp> [0..1] CodeSet 21
     AccountCriteria <AcctCrit> [0..1]  21
{Or       QueryName <QryNm> [1..1] Text 24
Or}       NewCriteria <NewCrit> [1..1]  C9 24
         NewQueryName <NewQryNm> [0..1] Text 27
         SearchCriteria <SchCrit> [0..*]  C4 27
           AccountIdentification <AcctId> [0..*]  29
{Or             Equal <EQ> [1..1] ± 29
Or             ContainText <CTTxt> [1..1] Text 30
Or}             NotContainText <NCTTxt> [1..1] Text 30
           Type <Tp> [0..*] ± 30
           Currency <Ccy> [0..*] CodeSet C1 30
           Balance <Bal> [0..*]  C5, C6 30
             Type <Tp> [0..*]  32
{Or               Code <Cd> [1..1] CodeSet 32
Or}               Proprietary <Prtry> [1..1] Text 32
             CounterpartyType <CtrPtyTp> [1..1] CodeSet 32
             CounterpartyIdentification <CtrPtyId> [0..*] ± 33
             ValueDate <ValDt> [0..*]  33
{Or               DateTime <DtTm> [1..1]  34
{Or                 FromDateTime <FrDtTm> [1..1] DateTime 34
Or                 ToDateTime <ToDtTm> [1..1] DateTime 34
Or                 FromToDateTime <FrToDtTm> [1..1] ± 35
Or                 EqualDateTime <EQDtTm> [1..1] DateTime 35
Or}                 NotEqualDateTime <NEQDtTm> [1..1] DateTime 35
Or}               Date <Dt> [1..1]  35
{Or                 FromDate <FrDt> [1..1] Date 35
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 15 February 2025
```

## File page 16

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or                 ToDate <ToDt> [1..1] Date 35
Or                 FromToDate <FrToDt> [1..1] ± 36
Or                 EqualDate <EQDt> [1..1] Date 36
Or}                 NotEqualDate <NEQDt> [1..1] Date 36
             ProcessingDate <PrcgDt> [0..1]  36
{Or               DateTime <DtTm> [1..1]  37
{Or                 FromDateTime <FrDtTm> [1..1] DateTime 37
Or                 ToDateTime <ToDtTm> [1..1] DateTime 37
Or                 FromToDateTime <FrToDtTm> [1..1] ± 38
Or                 EqualDateTime <EQDtTm> [1..1] DateTime 38
Or}                 NotEqualDateTime <NEQDtTm> [1..1] DateTime 38
Or}               Date <Dt> [1..1]  38
{Or                 FromDate <FrDt> [1..1] Date 38
Or                 ToDate <ToDt> [1..1] Date 38
Or                 FromToDate <FrToDt> [1..1] ± 39
Or                 EqualDate <EQDt> [1..1] Date 39
Or}                 NotEqualDate <NEQDt> [1..1] Date 39
           AccountOwner <AcctOwnr> [0..1] ± 39
           AccountServicer <AcctSvcr> [0..1] ± 40
         ReturnCriteria <RtrCrit> [0..1]  41
           NameIndicator <NmInd> [0..1] Indicator 42
           CurrencyIndicator <CcyInd> [0..1] Indicator 42
           TypeIndicator <TpInd> [0..1] Indicator 43
           MultilateralLimitIndicator <MulLmtInd> [0..1] Indicator 43
           MultilateralBalanceReturnCriteria <MulBalRtrCrit> [0..1]  43
             TypeIndicator <TpInd> [1..1] Indicator 43
             StatusIndicator <StsInd> [1..1] Indicator 43
             ValueDateIndicator <ValDtInd> [1..1] Indicator 44
             ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 44
             NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 44
           BilateralLimitIndicator <BilLmtInd> [0..1] Indicator 44
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 16 February 2025
```

