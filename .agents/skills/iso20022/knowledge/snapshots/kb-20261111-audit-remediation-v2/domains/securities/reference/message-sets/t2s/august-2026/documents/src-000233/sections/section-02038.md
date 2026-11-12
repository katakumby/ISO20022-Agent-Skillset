---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.6 AggregatedAmount <AggtdAmt>", "81.4.6.6.1 AggregatedDebitAmount <AggtdDbtAmt>"]
file_pages: [2780]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.6.1 AggregatedDebitAmount <AggtdDbtAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2780 to 2780.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2780

```text
AggregatedAmount <AggtdAmt> contains the following AggregatedPenaltyAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 2780
   AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 2780
   GlobalNetAmount <GblNetAmt> [0..1] ± 2781
   CounterpartyCSDAggregatedAmount
<CtrPtyCSDAggtdAmt>
[0..*]  2781
     PartyIdentification <PtyId> [1..1] ± 2781
     AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 2782
     AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 2782
     GlobalNetAmount <GblNetAmt> [0..1] ± 2782
81.4.6.6.1  AggregatedDebitAmount <AggtdDbtAmt>
Presence: [0..1]
Definition: Sum of all debit amounts.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
81.4.6.6.2  AggregatedCreditAmount <AggtdCdtAmt>
Presence: [0..1]
Definition: Sum of all credit amounts.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2780 August 2026
```

