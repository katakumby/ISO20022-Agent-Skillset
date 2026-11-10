---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.23 Intermediary48"]
file_pages: [5005]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.23 Intermediary48

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5005 to 5005.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5005

```text
66.1.30.23  Intermediary48
Definition: Party that provides services to investors relating to financial products.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5005
   Account <Acct> [0..1]  5005
     AccountIdentification <AcctId> [0..1] Text 5006
     AccountDesignation <AcctDsgnt> [0..1] Text 5006
     AccountName <AcctNm> [0..1] Text 5006
     AccountServicer <AcctSvcr> [1..1] ± 5006
     RegistrationAddress <RegnAdr> [0..1] ± 5007
   Role <Role> [0..1]  5007
{Or     Code <Cd> [1..1] CodeSet 5007
Or}     Proprietary <Prtry> [1..1] ± 5009
   ContactPerson <CtctPrsn> [0..1] ± 5009
66.1.30.23.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of the intermediary or a party related to the transfer.
Identification <Id> contains the following elements (see "PartyIdentification132" on page 5029 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
66.1.30.23.2  Account <Acct>
Presence: [0..1]
Definition: Identification of the account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5005 May 2026
```

