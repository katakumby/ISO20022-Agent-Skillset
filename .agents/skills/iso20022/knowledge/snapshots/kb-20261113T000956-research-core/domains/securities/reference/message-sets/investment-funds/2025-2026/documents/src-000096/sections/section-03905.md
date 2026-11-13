---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.21 TransferUnmatchedStatus4Choice", "66.1.45.21.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [5197]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.21.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5197 to 5197.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5197

```text
66.1.45.21.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.21.2  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the unmatched status.
Datatype: "TransferUnmatchedReason3Code" on page 5382
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
66.1.45.21.3  ExtendedReason <XtndedRsn>
Presence: [1..1]
Definition: Reason for the unmatched status.
Datatype: "Extended350Code" on page 5402
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5197 May 2026
```

