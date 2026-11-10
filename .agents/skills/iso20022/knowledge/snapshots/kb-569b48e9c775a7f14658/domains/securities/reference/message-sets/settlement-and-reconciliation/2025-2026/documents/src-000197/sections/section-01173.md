---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.77 LegalFramework3Choice", "35.1.16.77.2 Proprietary <Prtry>"]
file_pages: [1623]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.77.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1623 to 1623.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1623

```text
35.1.16.77.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Legal framework expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.78  Registration9Choice
Definition: Choice of format for the registration information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1623
Or}   Proprietary <Prtry> [1..1] ± 1623
35.1.16.78.1  Code <Cd>
Presence: [1..1]
Definition: Registration information expressed as an ISO 20022 code.
Datatype: "Registration1Code" on page 2113
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
35.1.16.78.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Registration information expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1623 March 2026
```

