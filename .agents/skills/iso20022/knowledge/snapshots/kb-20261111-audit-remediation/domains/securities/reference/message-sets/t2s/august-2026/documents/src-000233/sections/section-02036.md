---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.3 PartyIdentification <PtyId>", "81.4.6.3.1 Identification <Id>"]
file_pages: [2778]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.3.1 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2778 to 2778.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2778

```text
PartyIdentification <PtyId> contains the following PenaltyPartyIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2778
   Type <Tp> [0..1]  2778
{Or     Code <Cd> [1..1] CodeSet 2778
Or}     Proprietary <Prtry> [1..1] ± 2778
81.4.6.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 3060 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
81.4.6.3.2  Type <Tp>
Presence: [0..1]
Definition: Type of the party.
Type <Tp> contains one of the following PenaltyPartyType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2778
Or}   Proprietary <Prtry> [1..1] ± 2778
81.4.6.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Penalty party type, in a coded form.
Datatype: "ExternalPenaltyPartyType1Code" on page 3243
81.4.6.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Penalty party type, in a proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2778 August 2026
```

