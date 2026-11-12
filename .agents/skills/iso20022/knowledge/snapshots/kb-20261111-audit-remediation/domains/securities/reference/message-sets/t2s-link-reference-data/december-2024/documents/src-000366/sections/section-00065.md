---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.7 Party Identification", "8.1.7.2 PartyIdentification136", "8.1.7.2.1 Identification <Id>"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.7.2.1 Identification <Id>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
8.1.7.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 67 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 67
Or   ProprietaryIdentification <PrtryId> [1..1] ± 68
Or}   NameAndAddress <NmAndAdr> [1..1] ± 68
8.1.7.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 77
8.1.7.3  SystemPartyIdentification8
Definition: Unique and unambiguous identification of a party within a system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 69
8.1.7.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
Identification <Id> contains the following elements (see "PartyIdentification136" on page 68 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   LEI <LEI> [0..1] IdentifierSet 69
8.1.7.3.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the maintenance of the party reference data.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 69 December 2024
```

