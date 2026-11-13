---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.32 TaxCapacityParty4Choice"]
file_pages: [1564]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.32 TaxCapacityParty4Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1564 to 1564.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1564

```text
Definition: Provides additional settlement processing information which can not be included within the
structured fields of the message.
Datatype: "Max350Text" on page 2192
35.1.16.32  TaxCapacityParty4Choice
Definition: Choice of format for the tax capacity information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1564
Or}   Proprietary <Prtry> [1..1] ± 1564
35.1.16.32.1  Code <Cd>
Presence: [1..1]
Definition: Party tax capacity expressed as an ISO 20022 code.
Datatype: "TaxLiability1Code" on page 2172
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
35.1.16.32.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Party tax capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.33  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1564 March 2026
```

