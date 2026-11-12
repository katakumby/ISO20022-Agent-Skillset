---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>"]
file_pages: [69, 70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4 Movement <Mvmnt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 69 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 273
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 273
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
3.4.3.4  Movement <Mvmnt>
Presence: [1..*]
Definition: Identifies the individual transaction.
Impacted by: C14 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 69 September 2025
```

## File page 70

```text
Movement <Mvmnt> contains the following IntraPositionMovement10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 71
   SafekeepingAccount <SfkpgAcct> [0..1] ± 72
   StatusAndReason <StsAndRsn> [0..1]  72
     ProcessingStatus <PrcgSts> [0..*] ± 72
     SettlementStatus <SttlmSts> [0..*] ± C16 72
     Settled <Sttld> [0..1] ± C6 73
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 73
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 73
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 74
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 74
   PoolIdentification <PoolId> [0..1] Text 74
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 74
   MovementDetails <MvmntDtls> [0..1]  74
     BalanceFrom <BalFr> [1..1] ± 76
     BalanceTo <BalTo> [1..1] ± 76
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
76
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C17 77
     SettlementQuantity <SttlmQty> [1..1] ± 79
     SettledQuantity <SttldQty> [0..1] ± 79
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 80
     RemainingToBeSettledQuantity
<RmngToBeSttldQty>
[0..1] ± 80
     IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 80
     EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 81
     StatusDate <StsDt> [0..1] DateTime 81
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 81
     Linkages <Lnkgs> [0..*]  81
       ProcessingPosition <PrcgPos> [0..1] ± C25 82
       MessageNumber <MsgNb> [0..1] ± C22 82
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 70 September 2025
```

