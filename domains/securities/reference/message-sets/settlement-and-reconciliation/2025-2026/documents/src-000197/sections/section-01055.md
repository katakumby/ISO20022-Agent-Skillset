---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.9 TransactionIdentifications33", "35.1.14.9.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [1494]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.9.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1494 to 1494.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1494

```text
35.1.14.9.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.9.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.9.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
35.1.14.9.5  OtherIdentification <OthrId>
Presence: [0..1]
Definition: Reference to a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 2192
35.1.14.10  IdentificationType42Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1494
Or}   Proprietary <Prtry> [1..1] ± 1495
35.1.14.10.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification is defined using a code.
Datatype: "TypeOfIdentification1Code" on page 2173
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
CCPT PassportNumber Number assigned by a passport
authority.
CHTY TaxExemptIdentificationNumber Number assigned to a tax exempt entity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1494 March 2026
```

