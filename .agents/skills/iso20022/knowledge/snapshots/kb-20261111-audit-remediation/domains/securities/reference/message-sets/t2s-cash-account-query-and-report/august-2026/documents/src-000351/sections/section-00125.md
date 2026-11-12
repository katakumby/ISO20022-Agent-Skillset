---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Financial Institution Identification", "7.1.5.3 BranchAndFinancialInstitutionIdentification8"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.3 BranchAndFinancialInstitutionIdentification8

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
7.1.5.3  BranchAndFinancialInstitutionIdentification8
Definition: Unique and unambiguous identification of a financial institution or a branch of a financial
institution.
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
7.1.5.3.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C4 140
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 141
   LEI <LEI> [0..1] IdentifierSet 141
   Name <Nm> [0..1] Text 141
   PostalAddress <PstlAdr> [0..1] ± 141
   Other <Othr> [0..1] ± 142
7.1.5.3.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C4 "BICFI"
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 140 August 2026
```

