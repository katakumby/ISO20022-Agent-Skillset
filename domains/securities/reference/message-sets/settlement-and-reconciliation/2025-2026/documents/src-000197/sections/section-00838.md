---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.1 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>"]
file_pages: [1256]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.1 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1256 to 1256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1256

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1297
     CertificationIdentification <CertfctnId> [0..1] Text 1297
     CertificationDateTime <CertfctnDtTm> [0..1] ± 1298
     RegistrarAccount <RegarAcct> [0..1] Text 1298
     CertificateNumber <CertNb> [0..*] ± C31 1298
   SupplementaryData <SplmtryData> [0..*] ± C78 1298
32.4.2.3.1  SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>
Presence: [0..1]
Definition: Provides settlement type and identification information.
SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams> contains the following
elements (see "SettlementTypeAndAdditionalParameters14" on page 1540 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesMovementType <SctiesMvmntTp> [0..1] CodeSet 1540
   Payment <Pmt> [0..1] CodeSet 1540
   CommonIdentification <CmonId> [0..1] Text 1541
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1541
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1541
32.4.2.3.2  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Impacted by: C35 "LinkedQuantityRule"
Linkages <Lnkgs> contains the following Linkages80 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C85 1257
   MessageNumber <MsgNb> [0..1] ± C77 1257
   Reference <Ref> [1..1] ± 1258
   LinkedQuantity <LkdQty> [0..1]  1258
{Or     PairedOffQuantity <PairdOffQty> [1..1] ± C23 1258
Or}     TurnedQuantity <TrndQty> [1..1] ± C23 1259
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1256 March 2026
```

