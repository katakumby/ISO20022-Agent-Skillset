---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.84 SecuritiesCertificate4", "35.1.16.84.1 Number <Nb>"]
file_pages: [1631]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.84.1 Number <Nb>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1631 to 1631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1631

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Text 1631
   Issuer <Issr> [0..1] Text 1631
   SchemeName <SchmeNm> [0..1] Text 1631
Constraints
• ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
35.1.16.84.1  Number <Nb>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Datatype: "Max35Text" on page 2192
35.1.16.84.2  Issuer <Issr>
Presence: [0..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Datatype: "Max35Text" on page 2192
35.1.16.84.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 2192
35.1.16.85  SettlingCapacity7Choice
Definition: Choice of format for the settlement capacity information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1631
Or}   Proprietary <Prtry> [1..1] ± 1632
35.1.16.85.1  Code <Cd>
Presence: [1..1]
Definition: Settlement capacity expressed as an ISO 20022 code.
Datatype: "SettlingCapacity2Code" on page 2170
CodeName Name Definition
SAGE SettlingAgent Settlement party is trading and settling
transactions in financial instruments on
behalf of its client(s).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1631 March 2026
```

