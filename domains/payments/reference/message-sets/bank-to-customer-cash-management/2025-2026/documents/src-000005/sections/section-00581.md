---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.4 Amount Range", "6.1.4.2 ActiveOrHistoricCurrencyAndAmountRange2", "6.1.4.2.1 Amount <Amt>"]
file_pages: [814]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.4.2.1 Amount <Amt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 814 to 814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 814

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 814
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 814
   Currency <Ccy> [1..1] CodeSet C1 814
6.1.4.2.1  Amount <Amt>
Presence: [1..1]
Definition: Specified amount or amount range.
Amount <Amt> contains one of the following elements (see "ImpliedCurrencyAmountRange1Choice"
on page 812 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 812
Or   ToAmount <ToAmt> [1..1] ± 812
Or   FromToAmount <FrToAmt> [1..1]  812
     FromAmount <FrAmt> [1..1] ± 813
     ToAmount <ToAmt> [1..1] ± 813
Or   EqualAmount <EQAmt> [1..1] Amount 813
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 813
6.1.4.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the amount is a credited or debited amount.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.1.4.2.3  Currency <Ccy>
Presence: [1..1]
Definition: Medium of exchange of value, used to qualify an amount.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 887
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
814 March 2026
```

