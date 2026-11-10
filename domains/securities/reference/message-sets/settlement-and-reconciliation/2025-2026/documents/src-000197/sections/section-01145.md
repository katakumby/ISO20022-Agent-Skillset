---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.54 Reporting6Choice"]
file_pages: [1592]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.54 Reporting6Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1592 to 1592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1592

```text
CodeName Name Definition
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
35.1.16.54  Reporting6Choice
Definition: Choice of format for the reporting type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1592
Or}   Proprietary <Prtry> [1..1] ± 1592
35.1.16.54.1  Code <Cd>
Presence: [1..1]
Definition: Third party reporting information expressed as an ISO 20022 code.
Datatype: "Reporting2Code" on page 2134
CodeName Name Definition
STEX StockExchange Trade details are to be reported to a
stock exchange.
REGU RegulatoryOrganisation Trade details are to be reported to a
regulatory organisation.
DEFR DeferredReport Report is deferred, for example, because
the order was executed in partial fills.
35.1.16.54.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Third party reporting information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.55  HoldIndicator6
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1592 March 2026
```

