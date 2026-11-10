---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.39 Intermediary49", "66.1.30.39.1 Identification <Id>"]
file_pages: [5032]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.39.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5032 to 5032.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5032

```text
Constraints
• OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or UCL2
(UnderlyingClient2).
66.1.30.39.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of the intermediary.
Identification <Id> contains the following elements (see "PartyIdentification139" on page 5043 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.30.39.2  Account <Acct>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Account <Acct> contains the following Account35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 5032
   AccountServicer <AcctSvcr> [0..1] ± 5032
66.1.30.39.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.30.39.2.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Institution servicing the account and assigning the account identifier to the account owner.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5032 May 2026
```

