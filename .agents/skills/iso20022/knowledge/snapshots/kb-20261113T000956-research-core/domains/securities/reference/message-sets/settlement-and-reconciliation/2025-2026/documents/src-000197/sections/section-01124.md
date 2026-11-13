---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.35 CurrencyToBuyOrSell1Choice", "35.1.16.35.2 CurrencyToSell <CcyToSell>"]
file_pages: [1569]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.35.2 CurrencyToSell <CcyToSell>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1569 to 1569.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1569

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.1.16.35.2  CurrencyToSell <CcyToSell>
Presence: [1..1]
Definition: Account servicer is instructed to sell the indicated currency in order to obtain the necessary
currency to fund the transaction.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 2044
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.1.16.36  Statement79
Definition: Characteristics of the statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 1570
   QueryReference <QryRef> [0..1] Text 1570
   StatementIdentification <StmtId> [0..1] Text 1570
   StatementPeriod <StmtPrd> [1..1] ± 1570
   Frequency <Frqcy> [0..1] ± 1570
   UpdateType <UpdTp> [0..1] ± 1571
   StatementBasis <StmtBsis> [1..1] ± 1571
   ActivityIndicator <ActvtyInd> [1..1] Indicator 1571
   SubAccountIndicator <SubAcctInd> [1..1] Indicator 1571
Constraints
• ReportNumberRule
If ReportNumber/Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1569 March 2026
```

