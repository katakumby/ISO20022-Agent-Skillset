---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.5 PartyIdentification <PtyId>"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.2.5 PartyIdentification <PtyId>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
3.4.2.5  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the party within the system.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification136" on page 168
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 168
   LEI <LEI> [0..1] IdentifierSet 168
3.4.2.6  RestrictionIdentification <RstrctnId>
Presence: [0..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 188
3.4.2.7  RestrictionIssueDate <RstrctnIsseDt>
Presence: [0..1]
Definition: Specifies the date when the restriction for the party has been issued.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
26 March 2024
```

