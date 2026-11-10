---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>", "9.4.6.2.15.13 DigitalPaymentSettlement <DgtlPmtSttlm>", "9.4.6.2.15.13.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15.13.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
320
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 321
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  321
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 321
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 321
Or}     LEI <LEI> [1..1] IdentifierSet 322
9.4.6.2.15.13.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C11 "DescriptionPresenceRule", C12 "DescriptionUsageRule", C15 "ISINGuideline", C16
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
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 320 March 2026
```

