---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.1 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>"]
file_pages: [1218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.1 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1218 to 1218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherBusinessParties <OthrBizPties> [0..1]  C28,
C56
1245
     Investor <Invstr> [0..*] ± C25,
C60,
C66
1246
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1247
     StockExchange <StockXchg> [0..1] ± 1248
     TradeRegulator <TradRgltr> [0..1] ± 1248
     TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1248
     Broker <Brkr> [0..1] ± C61,
C67
1249
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1250
     CertificationIdentification <CertfctnId> [0..1] Text 1250
     CertificationDateTime <CertfctnDtTm> [0..1] ± 1251
     RegistrarAccount <RegarAcct> [0..1] Text 1251
     CertificateNumber <CertNb> [0..*] ± C31 1251
   SupplementaryData <SplmtryData> [0..*] ± C78 1251
32.4.2.2.1  SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>
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
32.4.2.2.2  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Linkages <Lnkgs> contains the following elements (see "Linkages40" on page 1619 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] ± 1619
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1218 March 2026
```

