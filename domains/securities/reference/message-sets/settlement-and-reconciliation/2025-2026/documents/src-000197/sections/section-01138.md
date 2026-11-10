---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.46 SettlementStandingInstructionDatabase4Choice"]
file_pages: [1583]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.46 SettlementStandingInstructionDatabase4Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1583 to 1583.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1583

```text
Note: The decimal separator is a dot.
35.1.16.46  SettlementStandingInstructionDatabase4Choice
Definition: Choice of format for the standing settlement instruction information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1583
Or}   Proprietary <Prtry> [1..1] ± 1583
35.1.16.46.1  Code <Cd>
Presence: [1..1]
Definition: Settlement standing instruction database expressed as an ISO 20022 code.
Datatype: "SettlementStandingInstructionDatabase1Code" on page 2161
CodeName Name Definition
INTE InternalDatabase The settlement standing instruction
database to be used is the receiver's
internal database.
BRKR BrokerDatabase The settlement standing instruction
database to be used is the broker's
database.
VEND VendorDatabase The settlement standing instruction
database to be used is the database of
the vendor.
35.1.16.46.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement standing instruction database expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.47  SecurityClassificationType2Choice
Definition: Choice between a CFI code and an other type of identification for the classification of a
financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CFI <CFI> [1..1] IdentifierSet 1584
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 1584
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1583 March 2026
```

