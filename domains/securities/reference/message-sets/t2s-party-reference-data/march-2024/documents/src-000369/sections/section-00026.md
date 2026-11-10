---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.3 ReturnCriteria <RtrCrit>", "3.4.3.4 PartyIdentification <PtyId>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.3.4 PartyIdentification <PtyId>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.4  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Indicates whether the unique identification to unambiguously identify the party within the
system is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.5  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Indicates whether the responsible party who initially created the party reference data is
requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.6  RestrictionIdentification <RstrctnId>
Presence: [0..1]
Definition: Indicates whether the identification of the restriction is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.7  RestrictedOnDate <RstrctdOnDt>
Presence: [0..1]
Definition: Indicates whether the date at which a restriction for party has been issued is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.8  Name <Nm>
Presence: [0..1]
Definition: Indicates whether the name for the party is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
32 March 2024
```

