---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks", "21.4.4 TransactionDetails <TxDtls>", "21.4.4.7 DigitalPaymentSettlement <DgtlPmtSttlm>", "21.4.4.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [721]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4.4.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 721 to 721.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 721

```text
DigitalPaymentSettlement <DgtlPmtSttlm> contains the following DigitalPaymentSettlement2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
721
   ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 722
   CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  722
{Or     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 722
Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 722
Or}     LEI <LEI> [1..1] IdentifierSet 723
21.4.4.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C8 "DescriptionPresenceRule", C9 "DescriptionUsageRule", C11 "ISINGuideline", C12
"ISINPresenceRule", C14 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 721 March 2026
```

