---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.5 ActiveOrHistoricCurrencyAndAmountRange2", "37.1.4.5.1 Amount <Amt>"]
file_pages: [793]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.5.1 Amount <Amt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 793 to 793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 793

```text
37.1.4.5.1  Amount <Amt>
Presence: [1..1]
Definition: Specified amount or amount range.
Amount <Amt> contains one of the following elements (see "ImpliedCurrencyAmountRange1Choice"
on page 794 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 794
Or   ToAmount <ToAmt> [1..1] ± 795
Or   FromToAmount <FrToAmt> [1..1]  795
     FromAmount <FrAmt> [1..1] ± 795
     ToAmount <ToAmt> [1..1] ± 795
Or   EqualAmount <EQAmt> [1..1] Amount 796
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 796
37.1.4.5.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the amount is a credited or debited amount.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
37.1.4.5.3  Currency <Ccy>
Presence: [1..1]
Definition: Medium of exchange of value, used to qualify an amount.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
37.1.4.6  AmountRangeBoundary1
Definition: Limit for an amount range.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 793 February 2025
```

