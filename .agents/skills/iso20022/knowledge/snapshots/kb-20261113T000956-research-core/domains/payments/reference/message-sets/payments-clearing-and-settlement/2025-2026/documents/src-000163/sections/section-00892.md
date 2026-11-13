---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.10 Mandate", "10.1.10.2 MandateTypeInformation2", "10.1.10.2.1 ServiceLevel <SvcLvl>"]
file_pages: [1187]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.10.2.1 ServiceLevel <SvcLvl>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1187 to 1187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1187

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ServiceLevel <SvcLvl> [0..1]  1187
{Or     Code <Cd> [1..1] CodeSet 1187
Or}     Proprietary <Prtry> [1..1] Text 1187
   LocalInstrument <LclInstrm> [0..1]  1187
{Or     Code <Cd> [1..1] CodeSet 1188
Or}     Proprietary <Prtry> [1..1] Text 1188
   CategoryPurpose <CtgyPurp> [0..1]  1188
{Or     Code <Cd> [1..1] CodeSet 1188
Or}     Proprietary <Prtry> [1..1] Text 1188
   Classification <Clssfctn> [0..1] ± 1188
10.1.10.2.1  ServiceLevel <SvcLvl>
Presence: [0..1]
Definition: Agreement under which or rules under which the mandate resides.
ServiceLevel <SvcLvl> contains one of the following ServiceLevel8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1187
Or}   Proprietary <Prtry> [1..1] Text 1187
10.1.10.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as published in an
external service level code list.
Datatype: "ExternalServiceLevel1Code" on page 1233
10.1.10.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.
Datatype: "Max35Text" on page 1246
10.1.10.2.2  LocalInstrument <LclInstrm>
Presence: [0..1]
Definition: User community specific instrument.
Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the
service or service level.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1187 March 2026
```

