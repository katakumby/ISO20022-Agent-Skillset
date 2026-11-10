---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.23 Intermediary48", "66.1.30.23.2 Account <Acct>", "66.1.30.23.2.1 AccountIdentification <AcctId>"]
file_pages: [5006]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.23.2.1 AccountIdentification <AcctId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5006 to 5006.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5006

```text
Account <Acct> contains the following Account34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1] Text 5006
   AccountDesignation <AcctDsgnt> [0..1] Text 5006
   AccountName <AcctNm> [0..1] Text 5006
   AccountServicer <AcctSvcr> [1..1] ± 5006
   RegistrationAddress <RegnAdr> [0..1] ± 5007
66.1.30.23.2.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.30.23.2.2  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
66.1.30.23.2.3  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
66.1.30.23.2.4  AccountServicer <AcctSvcr>
Presence: [1..1]
Definition: Institution that maintains the records where the account is held.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification132" on
page 5029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5006 May 2026
```

