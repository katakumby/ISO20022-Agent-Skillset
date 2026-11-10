---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.3 Status <Sts>", "5.4.2.1.3.2.1.4.3.3 Reason <Rsn>", "5.4.2.1.3.2.1.4.3.3.6 ProprietaryRejection <PrtryRjctn>"]
file_pages: [291]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.3.3.6 ProprietaryRejection <PrtryRjctn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 291 to 291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
CodeName Name Definition
MINO MinimumSettlementAmount Securities amount is lower than the
minimum existing settlement amount for
the instructed financial instrument.
PCAP PendingCAP Payment is pending, and does not settle
because the actual use of the risk
management limit on the counterpart
(bilateral limit) prevents settlement.
5.4.2.1.3.2.1.4.3.3.6  ProprietaryRejection <PrtryRjctn>
Presence: [1..1]
Definition: Defines the reason that has been used by the system to reject the transaction.
ProprietaryRejection <PrtryRjctn> contains the following ProprietaryStatusJustification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 291
   Reason <Rsn> [1..1] Text 291
5.4.2.1.3.2.1.4.3.3.6.1  ProprietaryStatusReason <PrtryStsRsn>
Presence: [1..1]
Definition: Defines the reason why the system has rejected the transaction.
Datatype: "Max4AlphaNumericText" on page 890
5.4.2.1.3.2.1.4.3.3.6.2  Reason <Rsn>
Presence: [1..1]
Definition: Provides detailed information about the reason why the system has rejected the transaction.
Datatype: "Max256Text" on page 889
5.4.2.1.3.2.1.4.3.3.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Defines a free text proprietary reason.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.4.4  InstructedAmount <InstdAmt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
InstructedAmount <InstdAmt> contains one of the following Amount3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C8 292
Or}   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 292
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 291 February 2025
```

