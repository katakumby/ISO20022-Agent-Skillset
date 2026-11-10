---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Bank Transaction Code", "7.1.3.1 BankTransactionCodeStructure4", "7.1.3.1.1 Domain <Domn>"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.1.1 Domain <Domn>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
7.1.3.1.1  Domain <Domn>
Presence: [0..1]
Definition: Set of elements used to provide the domain, the family and the sub-family of the bank
transaction code, in a structured and hierarchical format.
Usage: If a specific family or sub-family code cannot be provided, the generic family code defined for
the domain or the generic sub-family code defined for the family should be provided.
Domain <Domn> contains the following elements (see "BankTransactionCodeStructure5" on page 137
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 137
   Family <Fmly> [1..1] ± 137
7.1.3.1.2  Proprietary <Prtry>
Presence: [0..1]
Definition: Bank transaction code in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following ProprietaryBankTransactionCodeStructure1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] Text 136
   Issuer <Issr> [0..1] Text 136
7.1.3.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Proprietary bank transaction code to identify the underlying transaction.
Datatype: "Max35Text" on page 183
7.1.3.1.2.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the proprietary bank transaction code.
Datatype: "Max35Text" on page 183
7.1.3.2  BankTransactionCodeStructure6
Definition: Set of elements used to identify the type or operations code of a transaction entry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 137
   SubFamilyCode <SubFmlyCd> [1..1] CodeSet 137
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 136 August 2026
```

