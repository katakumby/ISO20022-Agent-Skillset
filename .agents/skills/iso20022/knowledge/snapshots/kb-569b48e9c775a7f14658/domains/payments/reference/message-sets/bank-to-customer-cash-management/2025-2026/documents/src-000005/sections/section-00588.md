---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.6 Bank Transaction Code"]
file_pages: [821]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.6 Bank Transaction Code

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 821 to 821.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 821

```text
6.1.6 Bank Transaction Code
6.1.6.1  BankTransactionCodeStructure4
Definition: Set of elements used to identify the type or operations code of a transaction entry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Domain <Domn> [0..1] ± 821
   Proprietary <Prtry> [0..1]  821
     Code <Cd> [1..1] Text 822
     Issuer <Issr> [0..1] Text 822
Constraints
• DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
Following Must be True
    /Domain Must be present
 Or    /Proprietary Must be present
• FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily code
is not allowed.
6.1.6.1.1  Domain <Domn>
Presence: [0..1]
Definition: Set of elements used to provide the domain, the family and the sub-family of the bank
transaction code, in a structured and hierarchical format.
Usage: If a specific family or sub-family code cannot be provided, the generic family code defined for
the domain or the generic sub-family code defined for the family should be provided.
Domain <Domn> contains the following elements (see "BankTransactionCodeStructure5" on
page 822 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 823
   Family <Fmly> [1..1] ± 823
6.1.6.1.2  Proprietary <Prtry>
Presence: [0..1]
Definition: Bank transaction code in a proprietary form, as defined by the issuer.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
821 March 2026
```

