---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.14 SettlementParameters <SttlmParams>"]
file_pages: [1115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.14 SettlementParameters <SttlmParams>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1115 to 1115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1115

```text
QuantityDetails <QtyDtls> contains the following elements (see "Quantity48" on page 1721 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1721
   DenominationChoice <DnmtnChc> [0..1] Text 1721
   CertificateNumber <CertNb> [0..*] ± C19 1721
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1722
31.4.6.14  SettlementParameters <SttlmParams>
Presence: [0..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C36 "SettlementDetailsRule"
SettlementParameters <SttlmParams> contains the following SettlementDetails236 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1115
   Registration <Regn> [0..1] ± 1116
   LegalRestrictions <LglRstrctns> [0..1] ± 1116
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1116
   SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1116
   TaxCapacity <TaxCpcty> [0..1] ± 1117
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1117
Constraints
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
31.4.6.14.1  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition47Choice" on page 2035 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2035
Or}   Proprietary <Prtry> [1..1] ± 2036
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1115 March 2026
```

