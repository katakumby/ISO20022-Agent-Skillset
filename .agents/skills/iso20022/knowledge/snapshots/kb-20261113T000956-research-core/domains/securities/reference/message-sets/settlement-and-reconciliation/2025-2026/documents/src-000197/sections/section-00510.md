---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08", "23.4 Message Building Blocks", "23.4.7 TransactionDetails <TxDtls>", "23.4.7.6 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [777]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.029.001.08"]
---

# 23.4.7.6 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 777 to 777.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 777

```text
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection51" on
page 1387 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1387
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1387
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1388
23.4.7.6  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..1]
Definition: Amount of digital asset that is to be/was posted to the account as a means of payment.
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
777
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 778
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  779
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 779
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C3 779
Or}     LEI <LEI> [1..1] IdentifierSet 779
23.4.7.6.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C10 "ISINGuideline", C11
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 777 March 2026
```

