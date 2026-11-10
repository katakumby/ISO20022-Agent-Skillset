---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.10 Document", "35.1.10.1 DocumentNumber13", "35.1.10.1.1 Number <Nb>"]
file_pages: [1444]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.10.1.1 Number <Nb>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1444 to 1444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1444

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] ± C20 1444
35.1.10.1.1  Number <Nb>
Presence: [1..1]
Definition: Number used to identify a message or document.
Impacted by: C20 "ShortLongNumberRule"
Number <Nb> contains one of the following elements (see "DocumentNumber5Choice" on page 1444
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
35.1.10.2  DocumentNumber5Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
35.1.10.2.1  ShortNumber <ShrtNb>
Presence: [1..1]
Definition: Message type number of the document referenced.
Datatype: "Exact3NumericText" on page 2190
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1444 March 2026
```

