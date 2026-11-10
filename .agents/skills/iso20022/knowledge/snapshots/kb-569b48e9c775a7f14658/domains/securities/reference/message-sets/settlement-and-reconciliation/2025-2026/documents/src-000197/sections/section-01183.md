---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.87 BlockChainAddressWallet2", "35.1.16.87.3 Name <Nm>"]
file_pages: [1634]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.87.3 Name <Nm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1634 to 1634.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1634

```text
35.1.16.87.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 2192
35.1.16.88  LinkageType3Choice
Definition: Choice of format for the linkage type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1634
Or}   Proprietary <Prtry> [1..1] ± 1634
35.1.16.88.1  Code <Cd>
Presence: [1..1]
Definition: Linkage type expressed as an ISO 20022 code.
Datatype: "LinkageType1Code" on page 2086
CodeName Name Definition
LINK Link Request is to link the referenced
transactions.
UNLK Unlink Request is to unlink the referenced
transactions.
SOFT Soft Request is to soft link the referenced
transactions.
35.1.16.88.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Linkage type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.89  Statement74
Definition: Characteristics of the statement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1634 March 2026
```

