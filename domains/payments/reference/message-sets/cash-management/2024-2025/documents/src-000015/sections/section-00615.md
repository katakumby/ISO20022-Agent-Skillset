---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.4 ActiveOrHistoricAmountRange2Choice"]
file_pages: [792]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.4 ActiveOrHistoricAmountRange2Choice

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 792 to 792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 792

```text
37.1.4.4  ActiveOrHistoricAmountRange2Choice
Definition: Choice between a range of amount values with or without the currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ImpliedCurrencyAndAmountRange
<ImpldCcyAndAmtRg>
[1..1] ± 792
Or}   CurrencyAndAmountRange <CcyAndAmtRg> [1..1] ± 792
37.1.4.4.1  ImpliedCurrencyAndAmountRange <ImpldCcyAndAmtRg>
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
37.1.4.4.2  CurrencyAndAmountRange <CcyAndAmtRg>
Presence: [1..1]
Definition: Expresses an amount or an amount range with the currency and where the credit/debit
indicator is explicit.
CurrencyAndAmountRange <CcyAndAmtRg> contains the following elements (see
"ActiveOrHistoricCurrencyAndAmountRange2" on page 792 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 793
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 793
   Currency <Ccy> [1..1] CodeSet C1 793
37.1.4.5  ActiveOrHistoricCurrencyAndAmountRange2
Definition: Range of amount values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 793
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 793
   Currency <Ccy> [1..1] CodeSet C1 793
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 792 February 2025
```

