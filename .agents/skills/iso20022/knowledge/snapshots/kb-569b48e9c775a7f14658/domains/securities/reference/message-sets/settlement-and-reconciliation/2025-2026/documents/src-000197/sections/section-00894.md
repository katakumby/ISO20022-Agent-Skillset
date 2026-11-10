---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "34.4 Message Building Blocks", "34.4.3 TransactionDetails <TxDtls>"]
file_pages: [1328, 1329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.040.001.06"]
---

# 34.4.3 TransactionDetails <TxDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1328 to 1329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1328

```text
ResponseStatus <RspnSts> contains one of the following elements (see "ResponseStatus6Choice"
on page 1992 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Consented <Cnsntd> [1..1] ± 1992
Or   Rejected <Rjctd> [1..1] ± 1992
Or}   Pending <Pdg> [1..1] ± 1992
34.4.3 TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C17 "SafekeepingAccountOrBlockChainAddress1Rule", C19
"SafekeepingAccountOrBlockChainAddress2Rule", C21
"SafekeepingAccountOrBlockChainAddress3Rule"
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1328 March 2026
```

## File page 1329

```text
TransactionDetails <TxDtls> contains the following TransactionDetails183 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
1330
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1331
   Payment <Pmt> [1..1] CodeSet 1331
   SettlementQuantity <SttlmQty> [1..1] ± 1331
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1332
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1332
   SettlementAmount <SttlmAmt> [0..1] ± 1332
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1333
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
1333
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1334
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1335
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1335
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1335
Or}       LEI <LEI> [1..1] IdentifierSet 1335
   SettlementDate <SttlmDt> [1..1] ± 1335
   TradeDate <TradDt> [0..1] ± 1336
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C13,
C14,
C15,
C16
1336
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C13,
C14,
C15,
C16
1337
   Investor <Invstr> [0..1] ± 1338
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1329 March 2026
```

