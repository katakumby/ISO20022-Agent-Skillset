---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.19 DigitalPaymentSettlement <DgtlPmtSttlm>", "31.4.6.19.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.19.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1128 to 1128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1128

```text
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token; or
the network fee.
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C17,
C18,
C21
1128
   Quantity <Qty> [1..1]  1129
{Or     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1129
Or}     NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1129
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1130
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1130
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C6 1130
Or}     LEI <LEI> [1..1] IdentifierSet 1130
31.4.6.19.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C17 "ISINGuideline", C18
"ISINPresenceRule", C21 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1128 March 2026
```

