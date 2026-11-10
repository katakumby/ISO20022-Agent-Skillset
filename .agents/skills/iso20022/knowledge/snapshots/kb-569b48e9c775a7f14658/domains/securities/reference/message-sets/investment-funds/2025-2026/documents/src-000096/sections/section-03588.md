---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.20 BreakdownByParty3", "66.1.28.20.1 Party <Pty>", "66.1.28.20.1.1 AccountIdentification <AcctId>"]
file_pages: [4838]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.20.1.1 AccountIdentification <AcctId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4838 to 4838.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4838

```text
Constraints
• AccountOrOwner1Rule
If AccountIdentification is not present, then OwnerIdentification must be present. Both
AccountIdentification and OwnerIdentification may be present.
On Condition
    /AccountIdentification is absent
Following Must be True
    /OwnerIdentification Must be present
• AccountOrOwner2Rule
If OwnerIdentification is not present, then AccountIdentification must be present. Both
OwnerIdentification and AccountIdentification may be present.
On Condition
    /OwnerIdentification is absent
Following Must be True
    /AccountIdentification Must be present
66.1.28.20.1.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains the following elements (see "AccountIdentification1" on
page 4328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1] ± 4329
66.1.28.20.1.2  OwnerIdentification <OwnrId>
Presence: [0..1]
Definition: Party that legally owns the account.
OwnerIdentification <OwnrId> contains one of the following elements (see
"PartyIdentification2Choice" on page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.28.20.1.3  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4838 May 2026
```

