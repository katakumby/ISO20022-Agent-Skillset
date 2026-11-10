---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09", "14.4 Message Building Blocks"]
file_pages: [463]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 463 to 463.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 463

```text
This constraint is defined at the MessageDefinition level.
C21 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C22 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C23 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C24 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C25 TransactionIdentificationPresence2Rule
If AccountOwnerTransactionIdentification is NONREF then at least one of the other references
must be present.
On Condition
    /AccountOwnerTransactionIdentification/
SecuritiesSettlementTransactionIdentification/TransactionIdentification is 
equal to value 'NONREF'
 Or    /AccountOwnerTransactionIdentification/
SecuritiesFinancingTransactionIdentification/TransactionIdentification is 
equal to value 'NONREF'
 Or    /AccountOwnerTransactionIdentification/
IntraPositionMovementIdentification is equal to value 'NONREF'
 Or    /AccountOwnerTransactionIdentification/OtherTransactionIdentification/
Identification is equal to value 'NONREF'
Following Must be True
    /AccountServicerTransactionIdentification Must be present
 Or    /MarketInfrastructureTransactionIdentification Must be present
 Or    /ProcessorTransactionIdentification Must be present
This constraint is defined at the MessageDefinition level.
14.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
14.4.1 AccountOwnerTransactionIdentification
<AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 463 March 2026
```

