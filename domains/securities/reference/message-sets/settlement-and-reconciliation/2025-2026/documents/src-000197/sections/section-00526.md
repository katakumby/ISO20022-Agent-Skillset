---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.4 Message Building Blocks", "24.4.5 AdditionalInformation <AddtlInf>"]
file_pages: [795]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.4.5 AdditionalInformation <AddtlInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 795 to 795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 795

```text
24.4.5 AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C11 "PartyRule", C12 "QuantityRule", C15
"SafekeepingAccountOrBlockChainAddress1Rule", C18
"SafekeepingAccountOrBlockChainAddress2Rule"
AdditionalInformation <AddtlInf> contains the following AdditionalInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 796
   ClassificationType <ClssfctnTp> [0..1] ± 796
   SafekeepingAccount <SfkpgAcct> [0..1] ± 796
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 796
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C3, C4,
C6, C7,
C9
797
   Quantity <Qty> [0..1] ± C5 798
   EffectiveDate <FctvDt> [0..1] ± 798
   ExpiryDate <XpryDt> [0..1] ± 798
   CutOffDate <CutOffDt> [0..1] ± 799
   Investor <Invstr> [0..1] ± 799
   DeliveringParty1 <DlvrgPty1> [0..1] ± C16,
C19
799
   ReceivingParty1 <RcvgPty1> [0..1] ± C16,
C19
800
   TransactionSubjectToBuyIn <TxSbjtToBuyIn> [0..1] Indicator 801
Constraints
• PartyRule
Investor, DeliveringParty1 and ReceivingParty1 cannot be requested to be modified using the
SecuritiesSettlementConditionModificationRequest. These fields are made available in the
SecuritiesSettlementConditionModificationRequest to enable the processing of the request vis-a-vis
the transaction requested to be modified.
• QuantityRule
If pre-agreed between account servicer and account owner, then Quantity will be used to instruct the
quantity of securities that should be partially processed, for example, partially authorised.
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 795 March 2026
```

