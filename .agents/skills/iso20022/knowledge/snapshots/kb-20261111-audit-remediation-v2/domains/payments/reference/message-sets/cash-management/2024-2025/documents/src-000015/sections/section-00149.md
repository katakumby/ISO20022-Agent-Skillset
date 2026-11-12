---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>", "5.4.2.1.1.3 CommonStatus <CmonSts>", "5.4.2.1.1.3.3 Reason <Rsn>", "5.4.2.1.1.3.3.6 ProprietaryRejection <PrtryRjctn>"]
file_pages: [247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1.3.3.6 ProprietaryRejection <PrtryRjctn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 247 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
CodeName Name Definition
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
5.4.2.1.1.3.3.6  ProprietaryRejection <PrtryRjctn>
Presence: [1..1]
Definition: Defines the reason that has been used by the system to reject the transaction.
ProprietaryRejection <PrtryRjctn> contains the following ProprietaryStatusJustification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 247
   Reason <Rsn> [1..1] Text 247
5.4.2.1.1.3.3.6.1  ProprietaryStatusReason <PrtryStsRsn>
Presence: [1..1]
Definition: Defines the reason why the system has rejected the transaction.
Datatype: "Max4AlphaNumericText" on page 890
5.4.2.1.1.3.3.6.2  Reason <Rsn>
Presence: [1..1]
Definition: Provides detailed information about the reason why the system has rejected the transaction.
Datatype: "Max256Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 247 February 2025
```

