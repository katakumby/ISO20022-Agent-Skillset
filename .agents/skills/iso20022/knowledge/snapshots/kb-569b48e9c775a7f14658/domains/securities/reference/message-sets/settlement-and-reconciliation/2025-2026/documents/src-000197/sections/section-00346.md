---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks"]
file_pages: [510, 511]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 510 to 511.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 510

```text
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
This constraint is defined at the MessageDefinition level.
C79 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
C80 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
17.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
17.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 2192
17.4.2 SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
Presence: [1..1]
Definition: Provides settlement type and identification information.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 510 March 2026
```

## File page 511

```text
SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams> contains the following
elements (see "SettlementTypeAndAdditionalParameters23" on page 1643 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1643
   Payment <Pmt> [1..1] CodeSet 1643
   CommonIdentification <CmonId> [0..1] Text 1644
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1644
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1644
   ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 1644
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 1644
   TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 1644
   TripartyAgentServiceProviderCollateralInstructionIdentific
ation <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 1645
   NonceIdentification <NonceId> [0..1] Text 1645
17.4.3 NumberCounts <NbCounts>
Presence: [0..1]
Definition: Count of the number of transactions linked.
Impacted by: C21 "CurrentInstructionNumberRule"
NumberCounts <NbCounts> contains one of the following elements (see "NumberCount2Choice" on
page 1590 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1590
Or}   TotalNumber <TtlNb> [1..1]  C19, C9 1590
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 1591
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1591
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
17.4.4 Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 511 March 2026
```

