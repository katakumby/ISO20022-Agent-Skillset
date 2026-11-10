---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.1 Identification <Id>"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.1 Identification <Id>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     RestrictionType <RstrctnTp> [1..1]  35
{Or       Code <Cd> [1..1] Text 35
Or}       Proprietary <Prtry> [1..1] ± 35
     ValidFrom <VldFr> [1..1] DateTime 35
     ValidUntil <VldUntil> [0..1] DateTime 35
   ClosingDate <ClsgDt> [0..1]  35
{Or     FromDate <FrDt> [1..1] Date 36
Or     ToDate <ToDt> [1..1] Date 36
Or     FromToDate <FrToDt> [1..1] ± 36
Or     EqualDate <EQDt> [1..1] Date 36
Or}     NotEqualDate <NEQDt> [1..1] Date 36
   OpeningDate <OpngDt> [0..1]  36
{Or     FromDate <FrDt> [1..1] Date 37
Or     ToDate <ToDt> [1..1] Date 37
Or     FromToDate <FrToDt> [1..1] ± 37
Or     EqualDate <EQDt> [1..1] Date 37
Or}     NotEqualDate <NEQDt> [1..1] Date 37
   ReferenceAccountIdentification <RefAcctId> [0..1] ± 38
   Proprietary <Prtry> [0..*] ± 38
   AccountOwner <AcctOwnr> [0..1]  38
     AnyBIC <AnyBIC> [0..1] IdentifierSet C2 39
     LEI <LEI> [0..1] IdentifierSet 39
     Other <Othr> [0..*]  39
       Identification <Id> [1..1] Text 39
       SchemeName <SchmeNm> [0..1]  39
{Or         Code <Cd> [1..1] CodeSet 40
Or}         Proprietary <Prtry> [1..1] Text 40
       Issuer <Issr> [0..1] Text 40
2.4.5.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the account.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 28 August 2026
```

