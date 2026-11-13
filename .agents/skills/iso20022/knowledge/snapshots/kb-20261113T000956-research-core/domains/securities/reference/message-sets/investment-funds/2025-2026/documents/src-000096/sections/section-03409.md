---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.19 RoundingDetails <RndgDtls>"]
file_pages: [4655]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.19 RoundingDetails <RndgDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4655 to 4655.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4655

```text
When an ISIN code exists, it is strongly recommended that the ISIN be used.
66.1.24.14.19  RoundingDetails <RndgDtls>
Presence: [0..1]
Definition: Parameters to be applied on deal amount for orders when the amount is a fractional number.
RoundingDetails <RndgDtls> contains the following elements (see "RoundingParameters1" on
page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RoundingModulus <RndgMdlus> [0..1] Quantity 4345
   RoundingDirection <RndgDrctn> [1..1] CodeSet 4345
66.1.24.14.20  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.24.14.21  BlockedStatus <BlckdSts>
Presence: [0..1]
Definition: Specifies the account is blocked and other factors for the blocked account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4655 May 2026
```

