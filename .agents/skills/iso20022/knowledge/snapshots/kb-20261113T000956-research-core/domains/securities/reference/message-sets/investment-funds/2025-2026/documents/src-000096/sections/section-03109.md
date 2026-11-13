---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.6 InvestmentAccount69", "66.1.2.6.3 AccountName <AcctNm>"]
file_pages: [4332]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.6.3 AccountName <AcctNm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4332 to 4332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4332

```text
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
66.1.2.6.3  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
66.1.2.6.4  Servicer <Svcr>
Presence: [0..1]
Definition: Institution that maintains the records where the account is held.
Servicer <Svcr> contains the following elements (see "PartyIdentification132" on page 5029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
66.1.2.7  SubAccountIdentification5
Definition: Account to or from which a securities entry is made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4332
   FungibleIndicator <FngbInd> [1..1] Indicator 4333
   ActivityIndicator <ActvtyInd> [1..1] Indicator 4333
   BalanceForSubAccount <BalForSubAcct> [0..*] ± C1, C8,
C5
4333
66.1.2.7.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4332 May 2026
```

