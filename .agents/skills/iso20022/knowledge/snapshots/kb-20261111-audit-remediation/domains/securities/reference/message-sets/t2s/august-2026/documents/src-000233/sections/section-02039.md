---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.6 AggregatedAmount <AggtdAmt>", "81.4.6.6.3 GlobalNetAmount <GblNetAmt>"]
file_pages: [2781]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.6.3 GlobalNetAmount <GblNetAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2781 to 2781.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2781

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
81.4.6.6.3  GlobalNetAmount <GblNetAmt>
Presence: [0..1]
Definition: Net of all amounts.
GlobalNetAmount <GblNetAmt> contains the following elements (see "AmountAndDirection5" on
page 2841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
81.4.6.6.4  CounterpartyCSDAggregatedAmount <CtrPtyCSDAggtdAmt>
Presence: [0..*]
Definition: Aggregated amounts provided per CSD of the counterparty.
CounterpartyCSDAggregatedAmount <CtrPtyCSDAggtdAmt> contains the following
AggregatedPenaltyAmount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 2781
   AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 2782
   AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 2782
   GlobalNetAmount <GblNetAmt> [0..1] ± 2782
81.4.6.6.4.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the party for which the aggregated amounts are
referred to.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2781 August 2026
```

