---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.15 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [698]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.15 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 698 to 698.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 698

```text
20.4.15 DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..2]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token; or
the network fee.
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
C26,
C31
698
   Quantity <Qty> [1..1]  699
{Or     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 699
Or}     NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 700
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  700
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 700
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C7 700
Or}     LEI <LEI> [1..1] IdentifierSet 700
20.4.15.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C18 "DescriptionPresenceRule", C19 "DescriptionUsageRule", C25 "ISINGuideline", C26
"ISINPresenceRule", C31 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 698 March 2026
```

