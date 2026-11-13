---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks", "21.4.4 TransactionDetails <TxDtls>", "21.4.4.7 DigitalPaymentSettlement <DgtlPmtSttlm>", "21.4.4.7.2 ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>"]
file_pages: [722]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4.4.7.2 ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 722 to 722.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 722

```text
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
21.4.4.7.2  ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>
Presence: [1..1]
Definition: Quantity of E-money token for the settlement payment.
Datatype: "Max30DecimalNumber" on page 2189
21.4.4.7.3  CashSettlementSystemPlace <CshSttlmSysPlc>
Presence: [0..1]
Definition: Location where the payment is/will be taking place.
CashSettlementSystemPlace <CshSttlmSysPlc> contains one of the following
CashSettlementSystemPlace1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 722
Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 722
Or}   LEI <LEI> [1..1] IdentifierSet 723
21.4.4.7.3.1  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 2186
21.4.4.7.3.2  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C4 "AnyBIC"
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 722 March 2026
```

