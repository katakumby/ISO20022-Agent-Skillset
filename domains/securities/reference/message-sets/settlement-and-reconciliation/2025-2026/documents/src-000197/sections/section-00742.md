---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.1 NotificationSenderTransactionIdentification <NtfctnSndrTxId>"]
file_pages: [1107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.1 NotificationSenderTransactionIdentification <NtfctnSndrTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1107 to 1107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1107

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C6 1130
Or}       LEI <LEI> [1..1] IdentifierSet 1130
   OtherBusinessParties <OthrBizPties> [0..1]  C16 1130
     Investor <Invstr> [0..1] ± 1131
     StockExchange <StockXchg> [0..1] ± 1131
     TradeRegulator <TradRgltr> [0..1] ± 1131
   SupplementaryData <SplmtryData> [0..*] ± C37 1132
Constraints
• DeliveringParty1Rule
If the instruction is a receive, then DeliveringParty1 must be present.
On Condition
    /SecuritiesMovementType is equal to value 'Receive'
Following Must be True
    /DeliveringSettlementParties Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
• ReceivingParty1Rule
If the instruction is a delivery, then ReceivingParty 1 must be present.
On Condition
    /SecuritiesMovementType is equal to value 'Delivery'
Following Must be True
    /ReceivingSettlementParties Must be present
 And    /ReceivingSettlementParties/Party1 Must be present
• SettlementAmountRule
If the instruction is against payment, then SettlementAmount must be present.
On Condition
    /Payment is equal to value 'AgainstPaymentSettlement'
Following Must be True
    /SettlementAmount Must be present
• TradeDateRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time of the
place of trade, for example, of the stock exchange, or of the selling broker for OTC.
31.4.6.1  NotificationSenderTransactionIdentification <NtfctnSndrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the notification receiver.
Datatype: "Max35Text" on page 2192
31.4.6.2  NotificationReceiverTransactionIdentification <NtfctnRcvrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the notification receiver.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1107 March 2026
```

