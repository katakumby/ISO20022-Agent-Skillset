---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.6 Bank Transaction Code", "6.1.6.1 BankTransactionCodeStructure4", "6.1.6.1.2 Proprietary <Prtry>", "6.1.6.1.2.1 Code <Cd>"]
file_pages: [822]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.6.1.2.1 Code <Cd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 822 to 822.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 822

```text
Proprietary <Prtry> contains the following ProprietaryBankTransactionCodeStructure1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] Text 822
   Issuer <Issr> [0..1] Text 822
6.1.6.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Proprietary bank transaction code to identify the underlying transaction.
Datatype: "Max35Text" on page 916
6.1.6.1.2.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the proprietary bank transaction code.
Datatype: "Max35Text" on page 916
6.1.6.2  BankTransactionCodeStructure6
Definition: Set of elements used to identify the type or operations code of a transaction entry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 822
   SubFamilyCode <SubFmlyCd> [1..1] CodeSet 822
6.1.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the family within a domain.
Datatype: "ExternalBankTransactionFamily1Code" on page 893
6.1.6.2.2  SubFamilyCode <SubFmlyCd>
Presence: [1..1]
Definition: Specifies the sub-product family within a specific family.
Datatype: "ExternalBankTransactionSubFamily1Code" on page 894
6.1.6.3  BankTransactionCodeStructure5
Definition: Set of elements used to identify the type or operations code of a transaction entry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 823
   Family <Fmly> [1..1] ± 823
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
822 March 2026
```

