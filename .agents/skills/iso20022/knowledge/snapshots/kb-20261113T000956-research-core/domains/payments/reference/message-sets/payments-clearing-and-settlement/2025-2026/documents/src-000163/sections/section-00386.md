---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.8 SecuritiesData <SctiesData>", "4.4.3.27.23.30.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>"]
file_pages: [529]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 529 to 529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 529

```text
SecuritiesData <SctiesData> contains the following SecuritiesAttributes1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 529
   Amount <Amt> [0..1] Amount C1, C11 529
4.4.3.27.23.30.2.8.1  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique transaction identifier will be created at the time a transaction is first executed, shared
with all registered entities and counterparties involved in the transaction, and used to track that
particular transaction during its lifetime. This identifier can also be known as the Unique Swap Identifier
(USI).
Datatype: "UTIIdentifier" on page 1241
4.4.3.27.23.30.2.8.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money for the trade.
Impacted by: C1 "ActiveCurrency", C11 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1222
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.3.27.23.30.2.9  AdditionalRemittanceInformation <AddtlRmtInf>
Presence: [0..3]
Definition: Additional information, in free text form, to complement the structured remittance information.
Datatype: "Max140Text" on page 1244
4.4.3.27.23.31  InstructedAmount <InstdAmt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
529 March 2026
```

