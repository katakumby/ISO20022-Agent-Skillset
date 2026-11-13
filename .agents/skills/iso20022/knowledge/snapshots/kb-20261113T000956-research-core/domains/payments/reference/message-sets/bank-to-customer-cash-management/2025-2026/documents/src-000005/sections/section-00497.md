---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.8 SecuritiesData <SctiesData>", "4.4.2.14.18.2.15.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>"]
file_pages: [725]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 725 to 725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 725

```text
SecuritiesData <SctiesData> contains the following SecuritiesAttributes1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 725
   Amount <Amt> [0..1] Amount C1, C7 725
4.4.2.14.18.2.15.2.8.1  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique transaction identifier will be created at the time a transaction is first executed, shared
with all registered entities and counterparties involved in the transaction, and used to track that
particular transaction during its lifetime. This identifier can also be known as the Unique Swap Identifier
(USI).
Datatype: "UTIIdentifier" on page 911
4.4.2.14.18.2.15.2.8.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money for the trade.
Impacted by: C1 "ActiveCurrency", C7 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 885
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.2.14.18.2.15.2.9  AdditionalRemittanceInformation <AddtlRmtInf>
Presence: [0..3]
Definition: Additional information, in free text form, to complement the structured remittance information.
Datatype: "Max140Text" on page 914
4.4.2.14.18.2.16  RelatedDates <RltdDts>
Presence: [0..1]
Definition: Set of elements used to identify the dates related to the underlying transactions.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
725 March 2026
```

