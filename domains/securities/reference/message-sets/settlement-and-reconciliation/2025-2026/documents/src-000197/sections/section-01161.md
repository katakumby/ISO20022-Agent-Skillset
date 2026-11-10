---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.68 Number22Choice"]
file_pages: [1608]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.68 Number22Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1608 to 1608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1608

```text
35.1.16.68  Number22Choice
Definition: Choice number format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 1608
Or}   Long <Lng> [1..1] ± 1608
35.1.16.68.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 2190
35.1.16.68.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 35 text, with the possibility to provide an issuer for the number
identification.
Long <Lng> contains the following elements (see "GenericIdentification1" on page 1500 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1500
   SchemeName <SchmeNm> [0..1] Text 1501
   Issuer <Issr> [0..1] Text 1501
35.1.16.69  OpeningClosing3Choice
Definition: Choice of format for the opening closing information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1608
Or}   Proprietary <Prtry> [1..1] ± 1609
35.1.16.69.1  Code <Cd>
Presence: [1..1]
Definition: Opening closing information expressed as an ISO 20022 code.
Datatype: "OpeningClosing1Code" on page 2088
CodeName Name Definition
CLOP ClosePosition Indicates that the trade is to close a
position.
OPEP OpenPosition Indicates that the trade is to open a
position.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1608 March 2026
```

