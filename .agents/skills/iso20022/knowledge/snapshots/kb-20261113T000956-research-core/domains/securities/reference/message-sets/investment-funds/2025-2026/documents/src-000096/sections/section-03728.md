---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.27 PartyIdentification140", "66.1.30.27.2 LEI <LEI>"]
file_pages: [5014]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.27.2 LEI <LEI>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5014 to 5014.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5014

```text
Party <Pty> contains one of the following elements (see "PartyIdentification126Choice" on page 4915
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4915
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 4916
66.1.30.27.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
66.1.30.28  Intermediary11
Definition: Party that provides services to investors relating to financial products.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5014
   Account <Acct> [0..1] ± 5014
{Or   Role <Role> [0..1] CodeSet 5015
Or}   ExtendedRole <XtndedRole> [0..1] Text 5016
66.1.30.28.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of the intermediary.
Identification <Id> contains one of the following elements (see "PartyIdentification2Choice" on
page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.30.28.2  Account <Acct>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5014 May 2026
```

