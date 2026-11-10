---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.19 TotalsPerStandingOrder <TtlsPerStgOrdr>", "31.4.2.1.2.1.19.3 SetStandingOrder <SetStgOrdr>", "31.4.2.1.2.1.19.3.1 TotalAmount <TtlAmt>"]
file_pages: [733]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.19.3.1 TotalAmount <TtlAmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 733 to 733.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 733

```text
SetStandingOrder <SetStgOrdr> contains the following TotalAmountAndCurrency1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalAmount <TtlAmt> [1..1] Amount 733
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 733
   Currency <Ccy> [0..1] CodeSet C1 733
31.4.2.1.2.1.19.3.1  TotalAmount <TtlAmt>
Presence: [1..1]
Definition: Total net amount for all operations taken into account in the report.
Datatype: "ImpliedCurrencyAndAmount" on page 848
31.4.2.1.2.1.19.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the total amount is a credit or a debit amount.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
31.4.2.1.2.1.19.3.3  Currency <Ccy>
Presence: [0..1]
Definition: Currency in which the total amount is expressed.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
31.4.2.1.2.1.19.4  PendingStandingOrder <PdgStgOrdr>
Presence: [1..1]
Definition: Total amount of not yet executed standing liquidity transfer orders.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 733 February 2025
```

