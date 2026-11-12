---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.3 SecuritiesMovementType <SctiesMvmntTp>"]
file_pages: [2537, 2538, 2539]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.3 SecuritiesMovementType <SctiesMvmntTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2537 to 2539.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2537

```text
SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp> contains one of
the following elements (see "SettlementOrCorporateActionEvent26Choice" on page 3018 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 3019
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 3019
72.4.3.4.18.3  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 3283
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
72.4.3.4.18.4  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 3235
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
72.4.3.4.18.5  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C8 "CashClearingSystemRule", C14 "FXStandingInstructionPresenceRule", C32
"SettlementDetailsRule", C33 "SettlementParametersGuideline"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2537 August 2026
```

## File page 2538

```text
SettlementParameters <SttlmParams> contains the following SettlementDetails235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] ± 2540
   Priority <Prty> [0..1] ± 2540
   SecuritiesTransactionType <SctiesTxTp> [0..1] ± 2540
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2540
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 2541
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 2541
   BlockTrade <BlckTrad> [0..1] ± 2541
   CCPEligibility <CCPElgblty> [0..1] ± 2542
   DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 2542
   CashClearingSystem <CshClrSys> [0..1] ± 2542
   ExposureType <XpsrTp> [0..1] ± 2542
   FXStandingInstruction <FxStgInstr> [0..1] ± 2543
   MarketClientSide <MktClntSd> [0..1] ± 2543
   NettingEligibility <NetgElgblty> [0..1] ± 2543
   Registration <Regn> [0..1] ± 2543
   RepurchaseType <RpTp> [0..1] ± 2544
   LegalRestrictions <LglRstrctns> [0..1] ± 2544
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 2544
   SettlingCapacity <SttlgCpcty> [0..1] ± 2544
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 2545
   TaxCapacity <TaxCpcty> [0..1] ± 2545
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 2545
   Tracking <Trckg> [0..1] ± 2545
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 2546
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 2546
   ReturnLeg <RtrLeg> [0..1] Indicator 2546
   ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 2546
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 2547
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 2547
   CashSubBalanceType <CshSubBalTp> [0..1] ± 2547
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2538 August 2026
```

## File page 2539

```text
Constraints
• CashClearingSystemRule
The CashSettlementSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSD's and central banks.
• FXStandingInstructionPresenceRule
If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be present.
In ISO 15022,
and therefore in ISO 20022, the FXStandingInstruction indicator can only be used when the
transation is instructed
in a released mode.
On Condition
    /HoldIndicator is present
 And    /HoldIndicator/Indicator is equal to value 'true'
Following Must be True
    /FXStandingInstruction Must be absent
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
• SettlementParametersGuideline
• Physical settlement:
In case of physical receipt at local agent level, the receiving agent must receive a receipt free
instruction
for reconciliation purposes. If the final beneficiary of the securities uses a global custodian, the
receipt free
instruction will be sent to the global custodian that will forward it to his receiving agent on the market.
For physical settlement, SettlementTransactionCondition/Physical must be used.
• Partial settlement:
This market practice only applies in markets where partial settlement is allowed.
If an account owner wants to specify in its original instruction that partial settlement is allowed or not,
they
must use the PartialSettlementIndicator.
• Book Transfer:
The use of SecuritiesTransactionTypes OWNI, OWNE, INSP and PORT and other booktransfer
related fields is governed by a market practice document.
• Block Trades:
The parent transaction must be identified using the BloclTrade field with code BLPA. The children
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2539 August 2026
```

