---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.6 IntermediaryInformation <IntrmyInf>", "8.4.7.7 Transaction <Tx>", "8.4.7.7.19 TransactionDetails <TxDtls>", "8.4.7.7.19.12 DigitalPaymentSettlement <DgtlPmtSttlm>", "8.4.7.7.19.12.2 ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.7.7.19.12.2 ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

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
8.4.7.7.19.12.2  ElectronicMoneyTokenSettlementQuantity <ElctrncMnyTknSttlmQty>
Presence: [1..1]
Definition: Quantity of E-money token for the settlement payment.
Datatype: "Max30DecimalNumber" on page 2189
8.4.7.7.19.12.3  CashSettlementSystemPlace <CshSttlmSysPlc>
Presence: [0..1]
Definition: Location where the payment is/will be taking place.
CashSettlementSystemPlace <CshSttlmSysPlc> contains one of the following
CashSettlementSystemPlace1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 237
Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 237
Or}   LEI <LEI> [1..1] IdentifierSet 238
8.4.7.7.19.12.3.1  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 2186
8.4.7.7.19.12.3.2  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C4 "AnyBIC"
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 237 March 2026
```

