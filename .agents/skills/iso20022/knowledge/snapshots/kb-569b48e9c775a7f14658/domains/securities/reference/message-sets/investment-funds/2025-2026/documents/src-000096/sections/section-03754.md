---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.43 Intermediary43", "66.1.30.43.2 Account <Acct>"]
file_pages: [5041]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.43.2 Account <Acct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5041 to 5041.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5041

```text
66.1.30.43.2  Account <Acct>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Account <Acct> contains the following Account27 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 5041
   AccountServicer <AcctSvcr> [1..1] ± 5041
66.1.30.43.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.30.43.2.2  AccountServicer <AcctSvcr>
Presence: [1..1]
Definition: Institution that maintains the records where the account is held.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.30.43.3  Role <Role>
Presence: [0..1]
Definition: Function performed by the intermediary.
Role <Role> contains one of the following elements (see "Role4Choice" on page 5016 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5016
Or}   Proprietary <Prtry> [1..1] ± 5017
66.1.30.43.4  ContactPerson <CtctPrsn>
Presence: [0..1]
Definition: Contact person and contact information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5041 May 2026
```

