---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.1 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>"]
file_pages: [1179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.1 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1179 to 1179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1179

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1207
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1207
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1207
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1208
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1208
Or}       LEI <LEI> [1..1] IdentifierSet 1208
   OtherBusinessParties <OthrBizPties> [0..1]  C28,
C56
1208
     Investor <Invstr> [0..*] ± C25,
C60,
C66
1209
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1210
     StockExchange <StockXchg> [0..1] ± 1211
     TradeRegulator <TradRgltr> [0..1] ± 1211
     TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1211
     Broker <Brkr> [0..1] ± C61,
C67
1212
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1213
     CertificationIdentification <CertfctnId> [0..1] Text 1213
     CertificationDateTime <CertfctnDtTm> [0..1] ± 1214
     RegistrarAccount <RegarAcct> [0..1] Text 1214
     CertificateNumber <CertNb> [0..*] ± C31 1214
   SupplementaryData <SplmtryData> [0..*] ± C78 1214
32.4.2.1.1  SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>
Presence: [0..1]
Definition: Provides settlement type and identification information.
SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams> contains the following
elements (see "SettlementTypeAndAdditionalParameters13" on page 1548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommonIdentification <CmonId> [0..1] Text 1548
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1548
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1548
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1179 March 2026
```

