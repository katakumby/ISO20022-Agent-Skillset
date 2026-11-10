---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.1 References <Refs>", "2.4.2.15.18.2.1.16 Proprietary <Prtry>"]
file_pages: [124]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.1.16 Proprietary <Prtry>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 124 to 124.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.16  Proprietary <Prtry>
Presence: [0..*]
Definition: Proprietary reference related to the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryReference1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 124
   Reference <Ref> [1..1] Text 124
2.4.2.15.18.2.1.16.1  Type <Tp>
Presence: [1..1]
Definition: Identifies the type of reference reported.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.16.2  Reference <Ref>
Presence: [1..1]
Definition: Proprietary reference specification related to the underlying transaction.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money in the cash transaction.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
2.4.2.15.18.2.3  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the transaction is a credit or a debit transaction.
Datatype: "CreditDebitCode" on page 892
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
124 March 2026
```

