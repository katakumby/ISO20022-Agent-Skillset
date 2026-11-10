---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.3 SecuritiesMovementType <SctiesMvmntTp>"]
file_pages: [141, 142, 143]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.3 SecuritiesMovementType <SctiesMvmntTp>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 141 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp> contains one of
the following elements (see "SettlementOrCorporateActionEvent26Choice" on page 382 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 382
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 382
4.4.3.4.18.3  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 526
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
4.4.3.4.18.4  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 502
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
4.4.3.4.18.5  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C8 "CashClearingSystemRule", C14 "FXStandingInstructionPresenceRule", C32
"SettlementDetailsRule", C33 "SettlementParametersGuideline"
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 141 March 2026
```

## File page 142

```text
SettlementParameters <SttlmParams> contains the following SettlementDetails235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] ± 144
   Priority <Prty> [0..1] ± 144
   SecuritiesTransactionType <SctiesTxTp> [0..1] ± 144
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 144
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 145
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 145
   BlockTrade <BlckTrad> [0..1] ± 145
   CCPEligibility <CCPElgblty> [0..1] ± 146
   DeliveryReturnReason <DlvryRtrRsn> [0..1] ± 146
   CashClearingSystem <CshClrSys> [0..1] ± 146
   ExposureType <XpsrTp> [0..1] ± 146
   FXStandingInstruction <FxStgInstr> [0..1] ± 147
   MarketClientSide <MktClntSd> [0..1] ± 147
   NettingEligibility <NetgElgblty> [0..1] ± 147
   Registration <Regn> [0..1] ± 147
   RepurchaseType <RpTp> [0..1] ± 148
   LegalRestrictions <LglRstrctns> [0..1] ± 148
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 148
   SettlingCapacity <SttlgCpcty> [0..1] ± 148
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 149
   TaxCapacity <TaxCpcty> [0..1] ± 149
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 149
   Tracking <Trckg> [0..1] ± 149
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 150
   LetterOfGuarantee <LttrOfGrnt> [0..1] ± 150
   ReturnLeg <RtrLeg> [0..1] Indicator 150
   ModificationCancellationAllowed <ModCxlAllwd> [0..1] ± 150
   EligibleForCollateral <ElgblForColl> [0..1] Indicator 151
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 151
   CashSubBalanceType <CshSubBalTp> [0..1] ± 151
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 142 March 2026
```

## File page 143

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
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 143 March 2026
```

