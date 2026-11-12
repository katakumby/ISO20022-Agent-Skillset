---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.1 NewQueryName <NewQryNm>"]
file_pages: [27, 28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.1 NewQueryName <NewQryNm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 27 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountServicerIndicator <AcctSvcrInd> [0..1] Indicator 46
Constraints
• ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present. If
ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
On Condition
    /ReturnCriteria is absent
Following Must be True
    /SearchCriteria[1] Must be present
2.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
2.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria to be used to extract the account information.
Impacted by: C4 "CashAccountIdentificationGuideline"
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 27 February 2025
```

## File page 28

```text
SearchCriteria <SchCrit> contains the following CashAccountSearchCriteria8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..*]  29
{Or     Equal <EQ> [1..1] ± 29
Or     ContainText <CTTxt> [1..1] Text 30
Or}     NotContainText <NCTTxt> [1..1] Text 30
   Type <Tp> [0..*] ± 30
   Currency <Ccy> [0..*] CodeSet C1 30
   Balance <Bal> [0..*]  C5, C6 30
     Type <Tp> [0..*]  32
{Or       Code <Cd> [1..1] CodeSet 32
Or}       Proprietary <Prtry> [1..1] Text 32
     CounterpartyType <CtrPtyTp> [1..1] CodeSet 32
     CounterpartyIdentification <CtrPtyId> [0..*] ± 33
     ValueDate <ValDt> [0..*]  33
{Or       DateTime <DtTm> [1..1]  34
{Or         FromDateTime <FrDtTm> [1..1] DateTime 34
Or         ToDateTime <ToDtTm> [1..1] DateTime 34
Or         FromToDateTime <FrToDtTm> [1..1] ± 35
Or         EqualDateTime <EQDtTm> [1..1] DateTime 35
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 35
Or}       Date <Dt> [1..1]  35
{Or         FromDate <FrDt> [1..1] Date 35
Or         ToDate <ToDt> [1..1] Date 35
Or         FromToDate <FrToDt> [1..1] ± 36
Or         EqualDate <EQDt> [1..1] Date 36
Or}         NotEqualDate <NEQDt> [1..1] Date 36
     ProcessingDate <PrcgDt> [0..1]  36
{Or       DateTime <DtTm> [1..1]  37
{Or         FromDateTime <FrDtTm> [1..1] DateTime 37
Or         ToDateTime <ToDtTm> [1..1] DateTime 37
Or         FromToDateTime <FrToDtTm> [1..1] ± 38
Or         EqualDateTime <EQDtTm> [1..1] DateTime 38
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 28 February 2025
```

