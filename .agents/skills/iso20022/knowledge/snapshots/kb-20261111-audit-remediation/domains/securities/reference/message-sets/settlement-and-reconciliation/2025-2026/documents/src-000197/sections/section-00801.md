---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.13 DigitalPaymentSettlement <DgtlPmtSttlm>", "32.4.2.1.13.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1206]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.13.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1206 to 1206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1206

```text
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1206
   Quantity <Qty> [1..1]  1207
{Or     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1207
Or}     NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1207
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1207
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1208
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1208
Or}     LEI <LEI> [1..1] IdentifierSet 1208
32.4.2.1.13.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C21 "DescriptionPresenceRule", C22 "DescriptionUsageRule", C29 "ISINGuideline", C30
"ISINPresenceRule", C40 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1206 March 2026
```

