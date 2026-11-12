---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 colr.001.001.02 CollateralValueQueryV02", "2.4 Message Building Blocks", "2.4.2 CollateralValueQueryDefinition <CollValQryDef>", "2.4.2.1 QueryName <QryNm>"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 2.4.2.1 QueryName <QryNm>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
CollateralValueQueryDefinition <CollValQryDef> contains one of the following
CollateralValueCriteriaDefinition4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 8
Or}   NewCriteria <NewCrit> [1..1]  8
     QueryName <QryNm> [0..1] Text 9
     SearchCriteria <SchCrit> [0..1]  C4 9
       CashAccountIdentification <CshAcctId> [0..1] ± 10
       Currency <Ccy> [0..*] CodeSet C1 10
       CashAccountOwner <CshAcctOwnr> [0..1] ± 11
       CashAccountServicer <CshAcctSvcr> [0..1] ± 11
       FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C9, C10,
C11
11
       SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 12
       SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 13
     ReturnCriteria <RtrCrit> [0..1]  13
       CashAccountOwnerIndicator <CshAcctOwnrInd> [0..1] Indicator 13
       CashAccountServicerIndicator <CshAcctSvcrInd> [0..1] Indicator 14
       SecuritiesAccountOwnerIndicator
<SctiesAcctOwnrInd>
[0..1] Indicator 14
       SecuritiesAccountServicerIndicator
<SctiesAcctSvcrInd>
[0..1] Indicator 14
       TotalCollateralValuationIndicator <TtlCollValtnInd> [0..1] Indicator 14
       SecuritiesAccountIndicator <SctiesAcctInd> [0..1] Indicator 14
       Securities <Scties> [0..1] Indicator 14
2.4.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 83
2.4.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Explicitly defines the query criteria.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
8 March 2024
```

