---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.2 Account Identification", "35.1.2.5 SecuritiesAccount25", "35.1.2.5.1 Identification <Id>"]
file_pages: [1346]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.2.5.1 Identification <Id>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1346 to 1346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1346

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1346
   Type <Tp> [0..1] ± 1346
   Name <Nm> [0..1] Text 1346
35.1.2.5.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.".
Datatype: "Max35Text" on page 2192
35.1.2.5.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains one of the following elements (see "PurposeCode7Choice" on page 1603 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1603
Or}   Proprietary <Prtry> [1..1] ± 1604
35.1.2.5.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 2192
35.1.2.6  AccountIdentification26
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1]  1346
     Identification <Id> [1..1] Text 1347
35.1.2.6.1  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1346 March 2026
```

