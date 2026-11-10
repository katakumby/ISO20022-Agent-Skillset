---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "11.4 Message Building Blocks"]
file_pages: [408, 409]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.020.001.07"]
---

# 11.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 408 to 409.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 408

```text
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C4 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C5 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C6 SecuritiesSettlementTransactionAllegementNotificationRule
The SecuritiesMessageCancellationAdvice can be used to cancel a
SecuritiesSettlementTransactionAllegementNotification for two reasons:
- The message was sent by mistake
- The counterparty cancelled its instruction.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
11.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
11.4.1 Reference <Ref>
Presence: [1..1]
Definition: Reference to the message advised to be cancelled by the account servicer.
Impacted by: C2 "OtherMessageIdentificationUsageRule", C6
"SecuritiesSettlementTransactionAllegementNotificationRule"
Approved by the Securities SEG on 27 January 2026 semt.020.001.07
SecuritiesMessageCancellationAdviceV07
Settlement And Reconciliation - Maintenance 2025 - 2026 408 March 2026
```

## File page 409

```text
Reference <Ref> contains one of the following elements (see "References69Choice" on page 1489 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionConfirmationIdentificatio
n <SctiesSttlmTxConfId>
[1..1] ± 1490
Or   IntraPositionMovementConfirmationIdentification
<IntraPosMvmntConfId>
[1..1] Text 1490
Or   SecuritiesBalanceAccountingReportIdentification
<SctiesBalAcctgRptId>
[1..1] Text 1490
Or   SecuritiesBalanceCustodyReportIdentification
<SctiesBalCtdyRptId>
[1..1] Text 1490
Or   IntraPositionMovementPostingReportIdentification
<IntraPosMvmntPstngRptId>
[1..1] Text 1490
Or   SecuritiesFinancingConfirmationIdentification
<SctiesFincgConfId>
[1..1] ± 1491
Or   SecuritiesTransactionPendingReportIdentification
<SctiesTxPdgRptId>
[1..1] Text 1491
Or   SecuritiesTransactionPostingReportIdentification
<SctiesTxPstngRptId>
[1..1] Text 1491
Or   SecuritiesSettlementTransactionAllegementReportIdentifi
cation <SctiesSttlmTxAllgmtRptId>
[1..1] Text 1491
Or   SecuritiesSettlementTransactionAllegementNotificationTr
ansactionIdentification <SctiesSttlmTxAllgmtNtfctnTxId>
[1..1] ± 1491
Or   PortfolioTransferNotificationIdentification
<PrtflTrfNtfctnId>
[1..1] Text 1492
Or   SecuritiesSettlementTransactionGenerationNotificationId
entification <SctiesSttlmTxGnrtnNtfctnId>
[1..1] ± 1492
Or   OtherMessageIdentification <OthrMsgId> [1..1] Text 1492
Or   TotalPortfolioValuationReportIdentification
<TtlPrtflValtnRptId>
[1..1] Text 1492
Or   TripartyCollateralTransactionInstructionProcessingStatus
AdviceIdentification <TrptyCollTxInstrPrcgStsAdvcId>
[1..1] Text 1492
Or   TripartyCollateralStatusAdviceIdentification
<TrptyCollStsAdvcId>
[1..1] Text 1493
Or}   TripartyCollateralAndExposureReportIdentification
<TrptyCollAndXpsrRptId>
[1..1] Text 1493
Constraints
• OtherMessageIdentificationUsageRule
If OtherMessageIdentification is used, then the message to be cancelled must not be one that can be
identified using of the message identification available in the choice list.
• SecuritiesSettlementTransactionAllegementNotificationRule
The SecuritiesMessageCancellationAdvice can be used to cancel a
SecuritiesSettlementTransactionAllegementNotification for two reasons:
Approved by the Securities SEG on 27 January 2026 semt.020.001.07
SecuritiesMessageCancellationAdviceV07
Settlement And Reconciliation - Maintenance 2025 - 2026 409 March 2026
```

