---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Bank Transaction Code", "7.1.3.2 BankTransactionCodeStructure6", "7.1.3.2.1 Code <Cd>"]
file_pages: [137]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.2.1 Code <Cd>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 137 to 137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 137

```text
7.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the family within a domain.
Datatype: "ExternalBankTransactionFamily1Code" on page 175
7.1.3.2.2  SubFamilyCode <SubFmlyCd>
Presence: [1..1]
Definition: Specifies the sub-product family within a specific family.
Datatype: "ExternalBankTransactionSubFamily1Code" on page 175
7.1.3.3  BankTransactionCodeStructure5
Definition: Set of elements used to identify the type or operations code of a transaction entry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 137
   Family <Fmly> [1..1] ± 137
7.1.3.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the business area of the underlying transaction.
Datatype: "ExternalBankTransactionDomain1Code" on page 175
7.1.3.3.2  Family <Fmly>
Presence: [1..1]
Definition: Specifies the family and the sub-family of the bank transaction code, within a specific
domain, in a structured and hierarchical format.
Family <Fmly> contains the following elements (see "BankTransactionCodeStructure6" on page 136
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 137
   SubFamilyCode <SubFmlyCd> [1..1] CodeSet 137
7.1.4 Date Period
7.1.4.1  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 137 August 2026
```

