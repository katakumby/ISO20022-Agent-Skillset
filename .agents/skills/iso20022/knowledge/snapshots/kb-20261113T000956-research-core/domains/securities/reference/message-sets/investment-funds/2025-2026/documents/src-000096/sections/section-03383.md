---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.20 AccountServicer <AcctSvcr>"]
file_pages: [4627]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.20 AccountServicer <AcctSvcr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4627 to 4627.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4627

```text
RoundingDetails <RndgDtls> contains the following elements (see "RoundingParameters1" on
page 4345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RoundingModulus <RndgMdlus> [0..1] Quantity 4345
   RoundingDirection <RndgDrctn> [1..1] CodeSet 4345
66.1.24.9.20  AccountServicer <AcctSvcr>
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
66.1.24.9.21  BlockedStatus <BlckdSts>
Presence: [0..1]
Definition: Specifies the account is blocked and other factors for the blocked account.
BlockedStatus <BlckdSts> contains one of the following elements (see
"BlockedStatusReason2Choice" on page 5164 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5164
Or}   Reason <Rsn> [1..*]  5165
     TransactionType <TxTp> [1..1]  5165
{Or       Code <Cd> [1..1] CodeSet 5165
Or}       Proprietary <Prtry> [1..1] ± 5167
     Blocked <Blckd> [1..1] Indicator 5167
     Reason <Rsn> [0..*]  5167
{Or       Code <Cd> [1..1] CodeSet 5167
Or}       Proprietary <Prtry> [1..1] ± 5168
     AdditionalInformation <AddtlInf> [1..1] Text 5168
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4627 May 2026
```

