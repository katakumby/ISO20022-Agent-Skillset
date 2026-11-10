---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.26 ProcessingPosition9Choice"]
file_pages: [1558]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.26 ProcessingPosition9Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1558 to 1558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1558

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.26  ProcessingPosition9Choice
Definition: Choice of format for the processing position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1558
Or}   Proprietary <Prtry> [1..1] ± 1558
35.1.16.26.1  Code <Cd>
Presence: [1..1]
Definition: Processing position expressed as an ISO 20022 code.
Datatype: "ProcessingPosition5Code" on page 2113
CodeName Name Definition
INFO Information Specifies that the transactions/
instructions are linked for information
purposes only.
35.1.16.26.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Processing position expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.27  RegistrationReason5
Definition: Reason of registration.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1558 March 2026
```

