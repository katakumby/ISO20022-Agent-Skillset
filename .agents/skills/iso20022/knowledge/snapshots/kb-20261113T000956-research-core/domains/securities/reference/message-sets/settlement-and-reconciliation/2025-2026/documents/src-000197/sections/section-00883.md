---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.7 TransactionDetails <TxDtls>", "33.4.7.6 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [1316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.7.6 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1316 to 1316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1316

```text
33.4.7.6  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
1316
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1317
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1317
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1317
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1318
Or}     LEI <LEI> [1..1] IdentifierSet 1318
33.4.7.6.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C9 "DescriptionPresenceRule", C10 "DescriptionUsageRule", C12 "ISINGuideline", C13
"ISINPresenceRule", C15 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1316 March 2026
```

