---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.2 PartyIdentification <PtyId>", "81.4.6.11.2.2 Type <Tp>"]
file_pages: [2788]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.2.2 Type <Tp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2788 to 2788.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2788

```text
Identification <Id> contains the following elements (see "PartyIdentification136" on page 3060 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
81.4.6.11.2.2  Type <Tp>
Presence: [0..1]
Definition: Type of the party.
Type <Tp> contains one of the following PenaltyPartyType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2788
Or}   Proprietary <Prtry> [1..1] ± 2788
81.4.6.11.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Penalty party type, in a coded form.
Datatype: "ExternalPenaltyPartyType1Code" on page 3243
81.4.6.11.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Penalty party type, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
81.4.6.11.3  AggregatedNetAmount <AggtdNetAmt>
Presence: [1..1]
Definition: Bilateral net amount per party and counterparty.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2788 August 2026
```

