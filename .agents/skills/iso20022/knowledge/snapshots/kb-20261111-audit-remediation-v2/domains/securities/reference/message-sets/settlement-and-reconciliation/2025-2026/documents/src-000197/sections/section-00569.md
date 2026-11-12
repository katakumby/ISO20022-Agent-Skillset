---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.14 DigitalPaymentSettlement <DgtlPmtSttlm>", "26.4.14.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [861]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.14.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 861 to 861.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 861

```text
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C25,
C26,
C33,
C34,
C41
861
   Quantity <Qty> [1..1]  862
{Or     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 862
Or}     NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 862
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  862
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 863
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C9 863
Or}     LEI <LEI> [1..1] IdentifierSet 863
26.4.14.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C25 "DescriptionPresenceRule", C26 "DescriptionUsageRule", C33 "ISINGuideline", C34
"ISINPresenceRule", C41 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 861 March 2026
```

