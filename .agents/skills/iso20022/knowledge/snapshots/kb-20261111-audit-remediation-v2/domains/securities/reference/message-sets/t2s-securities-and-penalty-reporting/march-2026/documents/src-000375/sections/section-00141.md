---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.6 AggregatedAmount <AggtdAmt>", "6.4.6.6.3 GlobalNetAmount <GblNetAmt>"]
file_pages: [199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.6.3 GlobalNetAmount <GblNetAmt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 199 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 199

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.4.6.6.3  GlobalNetAmount <GblNetAmt>
Presence: [0..1]
Definition: Net of all amounts.
GlobalNetAmount <GblNetAmt> contains the following elements (see "AmountAndDirection5" on
page 250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 251
   CreditDebit <CdtDbt> [0..1] CodeSet 251
6.4.6.6.4  CounterpartyCSDAggregatedAmount <CtrPtyCSDAggtdAmt>
Presence: [0..*]
Definition: Aggregated amounts provided per CSD of the counterparty.
CounterpartyCSDAggregatedAmount <CtrPtyCSDAggtdAmt> contains the following
AggregatedPenaltyAmount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 199
   AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 200
   AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 200
   GlobalNetAmount <GblNetAmt> [0..1] ± 200
6.4.6.6.4.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the party for which the aggregated amounts are
referred to.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification136" on page 413
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 199 March 2026
```

