---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.2 PartyIdentification <PtyId>", "6.4.6.11.2.2 Type <Tp>"]
file_pages: [206]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.2.2 Type <Tp>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 206 to 206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
Identification <Id> contains the following elements (see "PartyIdentification136" on page 413 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
6.4.6.11.2.2  Type <Tp>
Presence: [0..1]
Definition: Type of the party.
Type <Tp> contains one of the following PenaltyPartyType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 206
Or}   Proprietary <Prtry> [1..1] ± 206
6.4.6.11.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Penalty party type, in a coded form.
Datatype: "ExternalPenaltyPartyType1Code" on page 506
6.4.6.11.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Penalty party type, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
6.4.6.11.3  AggregatedNetAmount <AggtdNetAmt>
Presence: [1..1]
Definition: Bilateral net amount per party and counterparty.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 206 March 2026
```

