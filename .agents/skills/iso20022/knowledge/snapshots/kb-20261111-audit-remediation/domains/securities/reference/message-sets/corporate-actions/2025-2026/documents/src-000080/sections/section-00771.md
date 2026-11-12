---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.44 CorporateActionChangeTypeFormat6Choice"]
file_pages: [964]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.44 CorporateActionChangeTypeFormat6Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 964 to 964.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 964

```text
16.1.15.44  CorporateActionChangeTypeFormat6Choice
Definition: Choice between a standard code or a proprietary code to specify a type of change.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 964
Or}   Proprietary <Prtry> [1..1] ± 964
16.1.15.44.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of changes.
Datatype: "CorporateActionChangeType2Code" on page 1168
CodeName Name Definition
BERE BearToRegistered Change from bearer into registered form.
CERT Certificates Change of all instruments into
certificates.
DEPH DematerialisedToPhysical Change from dematerialised into
physical form.
GPPH GlobalPermanentToPhysical Change from global permanent to
physical form.
GTGP GlobalTemporaryToGlobalPermanent Change from global temporary to global
permanent form.
GTPH GlobalTemporaryToPhysical Change from global temporary to
physical form.
NAME Name The issuing company changes its name.
CA event shows the change from old
name to new name and may involve
surrendering physical shares with the old
name to the registrar.
PHDE PhysicalToDematerialised Change from physical into
dematerialised form.
REBE RegisteredToBearer Change from registered into bearer form.
TERM Terms Change in the terms of the security.
16.1.15.44.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of changes.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 964 February 2026
```

