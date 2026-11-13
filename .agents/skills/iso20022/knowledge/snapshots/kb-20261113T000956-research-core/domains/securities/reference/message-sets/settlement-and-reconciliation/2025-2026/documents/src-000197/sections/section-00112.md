---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.4 Message Building Blocks", "5.4.5 TransactionDetails <TxDtls>", "5.4.5.1 PoolIdentification <PoolId>"]
file_pages: [157]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.4.5.1 PoolIdentification <PoolId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 157 to 157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 157

```text
TransactionDetails <TxDtls> contains the following IntraPositionDetails60 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PoolIdentification <PoolId> [0..1] Text 157
   AccountOwner <AcctOwnr> [0..1] ± 158
   SafekeepingAccount <SfkpgAcct> [0..1] ± 158
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 158
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C6, C7,
C9
158
   SettlementQuantity <SttlmQty> [1..1] ± C5 159
   LotNumber <LotNb> [0..1] ± 160
   SettlementDate <SttlmDt> [1..1] ± 160
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 160
   BalanceFrom <BalFr> [0..1] ± 161
   BalanceTo <BalTo> [0..1] ± 161
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
5.4.5.1  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 157 March 2026
```

