---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.4 CounterpartyCSD <CtrPtyCSD>"]
file_pages: [197]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.4 CounterpartyCSD <CtrPtyCSD>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 197 to 197.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 197

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
6.4.6.4  CounterpartyCSD <CtrPtyCSD>
Presence: [0..1]
Definition: Unique and unambiguous identification of the party for which the aggregated amounts are
referred to.
CounterpartyCSD <CtrPtyCSD> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
6.4.6.5  CSDDepository <CSDDpstry>
Presence: [0..1]
Definition: Depository/intermediary that is used by an ICSD to access a specific counterparty's CSD,
that is the party that services the account.
CSDDepository <CSDDpstry> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
6.4.6.6  AggregatedAmount <AggtdAmt>
Presence: [0..1]
Definition: Aggregated penalty amount.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 197 March 2026
```

