---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.7 Transaction <Tx>", "8.4.7.7.19 TransactionDetails <TxDtls>", "8.4.7.7.19.12 DigitalPaymentSettlement <DgtlPmtSttlm>", "8.4.7.7.19.12.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [236]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.7.19.12.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 236 to 236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 236

```text
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C14,
C15,
C20
236
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 237
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  237
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 237
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 237
Or}     LEI <LEI> [1..1] IdentifierSet 238
8.4.7.7.19.12.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C8 "DescriptionPresenceRule", C9 "DescriptionUsageRule", C14 "ISINGuideline", C15
"ISINPresenceRule", C20 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 236 March 2026
```

