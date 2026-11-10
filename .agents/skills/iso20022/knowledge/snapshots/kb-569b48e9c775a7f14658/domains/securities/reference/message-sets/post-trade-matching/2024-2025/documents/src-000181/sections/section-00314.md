---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.53 QueryReference2", "7.1.19.53.1 QueryReference <QryRef>"]
file_pages: [378]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.53.1 QueryReference <QryRef>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 378 to 378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 378

```text
7.1.19.53.1  QueryReference <QryRef>
Presence: [1..1]
Definition: Unique and unambiguous identification of the query.
Datatype: "Max35Text" on page 669
7.1.19.53.2  QueryName <QryNm>
Presence: [0..1]
Definition: Name of the query.
Datatype: "Max35Text" on page 669
7.1.19.54  Registration9Choice
Definition: Choice of format for the registration information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 378
Or}   Proprietary <Prtry> [1..1] ± 378
7.1.19.54.1  Code <Cd>
Presence: [1..1]
Definition: Registration information expressed as an ISO 20022 code.
Datatype: "Registration1Code" on page 639
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
7.1.19.54.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Registration information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 378 February 2025
```

