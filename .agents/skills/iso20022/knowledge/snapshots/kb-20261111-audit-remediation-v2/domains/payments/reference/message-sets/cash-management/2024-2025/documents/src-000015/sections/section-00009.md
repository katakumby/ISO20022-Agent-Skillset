---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.1 QueryName <QryNm>"]
file_pages: [24, 25, 26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.1 QueryName <QryNm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 24 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       StandingOrderIndicator <StgOrdrInd> [0..1] Indicator 46
       AccountOwnerIndicator <AcctOwnrInd> [0..1] Indicator 46
       AccountServicerIndicator <AcctSvcrInd> [0..1] Indicator 46
2.4.2.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
2.4.2.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Explicitly defines the query criteria.
Impacted by: C9 "ReturnCriteriaAndOrSearchCriteriaRule"
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 24 February 2025
```

## File page 25

```text
NewCriteria <NewCrit> contains the following AccountCriteria8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewQueryName <NewQryNm> [0..1] Text 27
   SearchCriteria <SchCrit> [0..*]  C4 27
     AccountIdentification <AcctId> [0..*]  29
{Or       Equal <EQ> [1..1] ± 29
Or       ContainText <CTTxt> [1..1] Text 30
Or}       NotContainText <NCTTxt> [1..1] Text 30
     Type <Tp> [0..*] ± 30
     Currency <Ccy> [0..*] CodeSet C1 30
     Balance <Bal> [0..*]  C5, C6 30
       Type <Tp> [0..*]  32
{Or         Code <Cd> [1..1] CodeSet 32
Or}         Proprietary <Prtry> [1..1] Text 32
       CounterpartyType <CtrPtyTp> [1..1] CodeSet 32
       CounterpartyIdentification <CtrPtyId> [0..*] ± 33
       ValueDate <ValDt> [0..*]  33
{Or         DateTime <DtTm> [1..1]  34
{Or           FromDateTime <FrDtTm> [1..1] DateTime 34
Or           ToDateTime <ToDtTm> [1..1] DateTime 34
Or           FromToDateTime <FrToDtTm> [1..1] ± 35
Or           EqualDateTime <EQDtTm> [1..1] DateTime 35
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 35
Or}         Date <Dt> [1..1]  35
{Or           FromDate <FrDt> [1..1] Date 35
Or           ToDate <ToDt> [1..1] Date 35
Or           FromToDate <FrToDt> [1..1] ± 36
Or           EqualDate <EQDt> [1..1] Date 36
Or}           NotEqualDate <NEQDt> [1..1] Date 36
       ProcessingDate <PrcgDt> [0..1]  36
{Or         DateTime <DtTm> [1..1]  37
{Or           FromDateTime <FrDtTm> [1..1] DateTime 37
Or           ToDateTime <ToDtTm> [1..1] DateTime 37
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 25 February 2025
```

## File page 26

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           FromToDateTime <FrToDtTm> [1..1] ± 38
Or           EqualDateTime <EQDtTm> [1..1] DateTime 38
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 38
Or}         Date <Dt> [1..1]  38
{Or           FromDate <FrDt> [1..1] Date 38
Or           ToDate <ToDt> [1..1] Date 38
Or           FromToDate <FrToDt> [1..1] ± 39
Or           EqualDate <EQDt> [1..1] Date 39
Or}           NotEqualDate <NEQDt> [1..1] Date 39
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
     BilateralBalanceReturnCriteria <BilBalRtrCrit> [0..1]  44
       TypeIndicator <TpInd> [1..1] Indicator 45
       StatusIndicator <StsInd> [1..1] Indicator 45
       ValueDateIndicator <ValDtInd> [1..1] Indicator 45
       ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 45
       NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 46
     StandingOrderIndicator <StgOrdrInd> [0..1] Indicator 46
     AccountOwnerIndicator <AcctOwnrInd> [0..1] Indicator 46
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 26 February 2025
```

