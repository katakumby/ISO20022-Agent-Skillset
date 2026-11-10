---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.10 StandingOrder <StgOrdr>", "3.4.2.1.2.1.10.19 TotalsPerStandingOrder <TtlsPerStgOrdr>", "3.4.2.1.2.1.10.19.4 PendingStandingOrder <PdgStgOrdr>", "3.4.2.1.2.1.10.19.4.1 TotalAmount <TtlAmt>"]
file_pages: [94]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.10.19.4.1 TotalAmount <TtlAmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 94 to 94.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 94

```text
PendingStandingOrder <PdgStgOrdr> contains the following TotalAmountAndCurrency1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalAmount <TtlAmt> [1..1] Amount 94
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 94
   Currency <Ccy> [0..1] CodeSet C1 94
3.4.2.1.2.1.10.19.4.1  TotalAmount <TtlAmt>
Presence: [1..1]
Definition: Total net amount for all operations taken into account in the report.
Datatype: "ImpliedCurrencyAndAmount" on page 848
3.4.2.1.2.1.10.19.4.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the total amount is a credit or a debit amount.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.1.2.1.10.19.4.3  Currency <Ccy>
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
3.4.2.1.2.1.10.20  ZeroSweepIndicator <ZeroSweepInd>
Presence: [0..1]
Definition: Indicates whether the liquidity transfer standing order is defined as a zero sweeping order.
When true, the liquidity transfer standing order will transfer all amount of money out of the account so
the resulting balance is zero.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 886):
• Meaning When True: True
• Meaning When False: False
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 94 February 2025
```

