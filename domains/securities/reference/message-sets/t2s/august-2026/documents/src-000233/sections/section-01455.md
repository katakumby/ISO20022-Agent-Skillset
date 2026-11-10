---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.3 ReturnCriteria <RtrCrit>", "35.4.3.4 PartyIdentification <PtyId>"]
file_pages: [2069]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.3.4 PartyIdentification <PtyId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2069 to 2069.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2069

```text
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.4  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Indicates whether the unique identification to unambiguously identify the party within the
system is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.5  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Indicates whether the responsible party who initially created the party reference data is
requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.6  RestrictionIdentification <RstrctnId>
Presence: [0..1]
Definition: Indicates whether the identification of the restriction is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.7  RestrictedOnDate <RstrctdOnDt>
Presence: [0..1]
Definition: Indicates whether the date at which a restriction for party has been issued is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.8  Name <Nm>
Presence: [0..1]
Definition: Indicates whether the name for the party is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2069 August 2026
```

