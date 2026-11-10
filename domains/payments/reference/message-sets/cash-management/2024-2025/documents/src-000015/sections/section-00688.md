---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.45 PendingStatus4Code"]
file_pages: [869]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.45 PendingStatus4Code

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 869 to 869.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 869

```text
CodeName Name Definition
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
FUTU AwaitingSettlementDate Instruction is awaiting the settlement
date, and no settlement problems have
been reported.
LACK LackOfSecurities Insufficient deliverable securities in your
account.
LALO SecuritiesLoanedOut Insufficient deliverable securities in your
account because securities are loaned
out.
MONY InsufficientMoney Insufficient money in your account.
NCON ConfirmationNotReceived Settlement confirmation has not been
received.
REFS NotInGoodOrder Delivery/receipt has been refused
because the physical securities are not
in good order.
SDUT LackOfStampDutyInformation Instruction is pending as stamp duty
information is missing.
BATC ProcessingBatchDifference Processing batch differs in the
counterparty's instruction, for example,
day time/real time versus overnight.
CYCL AwaitingNextSettlementCycle Instruction is confirmed in the local
market or is ready for settlement,
awaiting the next settlement cycle.
SBLO SecuritiesBlocked Settlement is pending. The securities are
blocked due to, for example, a corporate
action event, re-alignment.
CPEC CounterpartyInReceivership Counterparty is in receivership, that is,
the form of bankruptcy where a court
appointed person, the receiver, manages
the affairs of the business.
MINO MinimumSettlementAmount Securities amount is lower than the
minimum existing settlement amount for
the instructed financial instrument.
PCAP PendingCAP Payment is pending, and does not settle
because the actual use of the risk
management limit on the counterpart
(bilateral limit) prevents settlement.
37.2.2.45  PendingStatus4Code
Definition: Indicates that the state of a payment at the clearing agent side is pending.
Type: CodeSet
CodeName Name Definition
ACPD Accepted Transaction has been accepted by the
clearing agent.
VALD Validated Transaction has been validated by the
clearing agent.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 869 February 2025
```

