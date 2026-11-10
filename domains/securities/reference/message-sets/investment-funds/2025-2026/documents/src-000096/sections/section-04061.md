---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.241 TransferType4Code"]
file_pages: [5382]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.241 TransferType4Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5382 to 5382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5382

```text
66.2.2.241  TransferType4Code
Definition: Specifies whether a financial instrument is transferred as an asset or as cash.
Type: CodeSet
CodeName Name Definition
CASH Cash Transfer as cash.
CONV Conversion ISIN is converted to another ISIN and
then transferred.
EXCL Excluded Asset excluded from transfer.
SECU InSpecie Transfer the security as an asset in
specie, that is, 'in its actual form'.
66.2.2.242  TransferUnmatchedReason3Code
Definition: Specifies the reason the transaction, transfer or settlement instruction is unmatched.
Type: CodeSet
CodeName Name Definition
CMIS NoMatch No potential match has been found.
CPCA CounterpartyCancelled Counterparty has cancelled the
transaction/instruction.
DELN TransactionDirection Direction of transaction does not match:
delivery instead of receipt or vice versa.
DSEC FinancialInstrument Financial instrument identification does
not match or a financial instrument
attribute differs.
PHYS PhysicalSettlement Settlement does not match:
counterparty's instruction is for physical
settlement, your instruction is not, or vice
versa.
PODU Duplicate Instruction has not been matched: it is a
possible duplicate instruction.
DEPT SettlementPlace Place of settlement does not match.
DDAT SettlementDate Settlement date or transfer date does not
match.
DQUA FinancialInstrumentQuantity Financial instrument quantity does not
match.
ICUS ReceivingOrDeliveringCustodian Delivering or receiving custodian does
not match.
SAFE SafekeepingAccount Safekeeping account used as a
matching criteria on the market
concerned does not match.
66.2.2.243  TypeOfIdentification1Code
Definition: Specifies the type of alternate identification which can be used to give an alternate
identification of the party identified.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5382 May 2026
```

