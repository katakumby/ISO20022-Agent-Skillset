---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.3 AccountServicerIdentification <AcctSvcrId>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.3 AccountServicerIdentification <AcctSvcrId>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
2.4.3 AccountServicerIdentification <AcctSvcrId>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
.
AccountServicerIdentification <AcctSvcrId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 140 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  140
     BICFI <BICFI> [0..1] IdentifierSet C4 140
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 141
     LEI <LEI> [0..1] IdentifierSet 141
     Name <Nm> [0..1] Text 141
     PostalAddress <PstlAdr> [0..1] ± 141
     Other <Othr> [0..1] ± 142
   BranchIdentification <BrnchId> [0..1]  143
     Identification <Id> [0..1] Text 143
     LEI <LEI> [0..1] IdentifierSet 143
     Name <Nm> [0..1] Text 143
     PostalAddress <PstlAdr> [0..1] ± 143
2.4.4 Organisation <Org>
Presence: [0..1]
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 13 August 2026
```

