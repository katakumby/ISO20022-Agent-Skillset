---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.238 TransferReason1Code"]
file_pages: [5380]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.238 TransferReason1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5380 to 5380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5380

```text
CodeName Name Definition
CONF Confirmation The transfer-in is a confirmation (rather
than an advice).
ADVI Advice The transfer-in provides advice about
account information for a transfer.
66.2.2.238  TransferReason1Code
Definition: Specifies the reason for the assets transfer.
Type: CodeSet
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
66.2.2.239  TransferStatus6Code
Definition: Specifies a transfer or settlement instruction status.
Type: CodeSet
CodeName Name Definition
PACK Accepted Transfer or settlement instruction has
been acknowledged / accepted for
further processing.
COSE AlreadyExecuted Transfer or settlement instruction is fully
executed and the confirmation is sent.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5380 May 2026
```

