---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.1 References <Refs>", "2.4.2.15.18.2.1.9 ChequeNumber <ChqNb>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.1.9 ChequeNumber <ChqNb>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
2.4.2.15.18.2.1.9  ChequeNumber <ChqNb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a cheque as assigned by the agent.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.10  ClearingSystemReference <ClrSysRef>
Presence: [0..1]
Definition: Unique reference, as assigned by a clearing system, to unambiguously identify the
instruction.
Usage: In case there are technical limitations to pass on multiple references, the end-to-end
identification must be passed on throughout the entire end-to-end chain.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.11  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the securities transaction as known by the securities account
owner (or the instructing party managing the account).
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.12  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the securities transaction as known by the securities account
servicer.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.13  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a securities transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.14  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Identification of the securities transaction assigned by the processor of the instruction other
than the securities account owner, the securities account servicer and the market infrastructure.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.15  ReturnIdentification <RtrId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the returned transaction.
Usage: The instructing party is the party sending the return message and not the party that sent the
original instruction that is being returned.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
123 March 2026
```

