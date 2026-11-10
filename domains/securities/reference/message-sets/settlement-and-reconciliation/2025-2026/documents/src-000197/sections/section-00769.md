---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks"]
file_pages: [1155, 1156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1155 to 1156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1155

```text
C82 TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
C83 TransactionIdentificationPresenceRule
If AccountOwnerTransactionIdentification is NONREF then at least one of the other references
must be present.
C84 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
C85 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
32.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
32.4.1 ModifiedTransactionDetails <ModfdTxDtls>
Presence: [1..1]
Definition: Identifies the details of the transaction that is being modified.
Impacted by: C37 "NoAccountOwnerTransactionIdentificationRule", C57
"SafekeepingAccountOrBlockChainAddress1Rule", C63
"SafekeepingAccountOrBlockChainAddress2Rule", C69
"SafekeepingAccountOrBlockChainAddress3Rule", C83 "TransactionIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1155 March 2026
```

## File page 1156

```text
ModifiedTransactionDetails <ModfdTxDtls> contains the following TransactionDetails181 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] ± 1157
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 1158
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1158
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1158
   OtherTransactionIdentification <OthrTxId> [0..1] Text 1158
   AccountOwner <AcctOwnr> [0..1] ± 1158
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1159
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1159
   TransactionDetails <TxDtls> [0..1]  1159
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1160
     TradeDate <TradDt> [0..1] ± 1161
     SettlementDate <SttlmDt> [1..1] ± 1162
     SettlementQuantity <SttlmQty> [1..1] ± 1162
     SettlementAmount <SttlmAmt> [0..1] ± 1162
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1163
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1163
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1164
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1164
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1164
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1165
Or}         LEI <LEI> [1..1] IdentifierSet 1165
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C41,
C43,
C46,
C49
1165
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C41,
C43,
1166
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1156 March 2026
```

