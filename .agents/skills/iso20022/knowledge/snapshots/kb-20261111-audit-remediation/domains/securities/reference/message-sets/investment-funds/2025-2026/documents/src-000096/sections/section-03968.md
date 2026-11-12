---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.9 TransferReason1Choice", "66.1.50.9.1 Code <Cd>"]
file_pages: [5266]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.9.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5266 to 5266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5266

```text
66.1.50.9.1  Code <Cd>
Presence: [1..1]
Definition: Transfer reason expressed as an ISO 20022 code.
Datatype: "TransferReason1Code" on page 5380
CodeName Name Definition
TRAU UndividedPossession Transfer is an undivided possession.
TRAC TransferBetweenSpouses Transfer is between spouses.
TRAT Trade Transfer is a trade.
TRAO OrdinaryTransfer Transfer is ordinary.
TRAI Heritage Transfer is a heritage.
TRAG Gift Transfer is a gift.
TPLD PledgedAccountTransfer Transfer to pledged account (in certain
circumstances distributors have to freeze
and transfer total or partial holding to
separate omnibus account e.g.
investigation required by fiscal authority
or police).
TTDT TDTFrameworkTransfer Transfer instruction executed within TDT
framework (TDT framework is the
operation model promoted by the Italian
Banking Association for transfer and
most of transfers, but not all, will be
executed in accordance with that
process).
TRPE TransferBetweenDifferentBeneficiaries Transfer between different beneficiaries
with taxation to be applied (accounts
with different owner).
TRAF Demerger Transfer is the result of a demerger or
division.
TRAN BetweenOwnAccounts Transfer is between own accounts.
66.1.50.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transfer reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification27" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4539
   SchemeName <SchmeNm> [0..1] Text 4539
   Issuer <Issr> [1..1] Text 4539
66.1.50.10  RejectionReason33
Definition: Information about a rejected status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5266 May 2026
```

