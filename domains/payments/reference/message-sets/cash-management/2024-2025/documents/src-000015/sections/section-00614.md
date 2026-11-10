---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.3 ActiveAmountRange3Choice"]
file_pages: [791]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.3 ActiveAmountRange3Choice

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 791 to 791.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 791

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
37.1.4.3  ActiveAmountRange3Choice
Definition: Choice between a range of amount values with or without the currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ImpliedCurrencyAndAmountRange
<ImpldCcyAndAmtRg>
[1..1] ± 791
Or}   CurrencyAndAmountRange <CcyAndAmtRg> [1..1] ± 791
37.1.4.3.1  ImpliedCurrencyAndAmountRange <ImpldCcyAndAmtRg>
Presence: [1..1]
Definition: Expresses an amount or an amount range with an explicit debit/credit indicator and where
the currency is implied.
ImpliedCurrencyAndAmountRange <ImpldCcyAndAmtRg> contains the following elements (see
"ImpliedCurrencyAndAmountRange1" on page 789 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 789
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 789
37.1.4.3.2  CurrencyAndAmountRange <CcyAndAmtRg>
Presence: [1..1]
Definition: Expresses an amount or an amount range with the currency and where the credit/debit
indicator is explicit.
CurrencyAndAmountRange <CcyAndAmtRg> contains the following elements (see
"ActiveCurrencyAndAmountRange3" on page 790 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 790
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 790
   Currency <Ccy> [1..1] CodeSet C1 790
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 791 February 2025
```

