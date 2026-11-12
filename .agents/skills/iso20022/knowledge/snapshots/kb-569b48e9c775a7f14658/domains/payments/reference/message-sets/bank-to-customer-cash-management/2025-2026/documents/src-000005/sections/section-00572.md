---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount", "6.1.3.2 AmountAndDirection35"]
file_pages: [805]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3.2 AmountAndDirection35

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 805 to 805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 805

```text
ProprietaryAmount <PrtryAmt> contains the following elements (see
"AmountAndCurrencyExchangeDetails6" on page 808 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 809
   Amount <Amt> [1..1] Amount C1, C5 809
   CurrencyExchange <CcyXchg> [0..1]  C13 809
     SourceCurrency <SrcCcy> [1..1] CodeSet C1 810
     TargetCurrency <TrgtCcy> [0..1] CodeSet C1 810
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 811
     ExchangeRate <XchgRate> [1..1] Rate 811
     ContractIdentification <CtrctId> [0..1] Text 811
     QuotationDate <QtnDt> [0..1] DateTime 811
     ExchangeRateBase <XchgRateBase> [0..1] Quantity 811
6.1.3.2  AmountAndDirection35
Definition: Resulting debit or credit amount of the netted amounts for all debit and credit entries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Quantity 805
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 805
6.1.3.2.1  Amount <Amt>
Presence: [1..1]
Definition: Resulting amount of the netted amounts for all debit and credit entries.
Datatype: "NonNegativeDecimalNumber" on page 912
6.1.3.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the amount is a credit or a debit amount.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.1.3.3  AmountAndCurrencyExchangeDetails5
Definition: Set of elements used to provide information on the original amount and currency exchange.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
805 March 2026
```

