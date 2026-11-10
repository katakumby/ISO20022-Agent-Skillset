---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.11 Party Identification", "13.1.11.4 SystemPartyIdentification8", "13.1.11.4.2 ResponsiblePartyIdentification <RspnsblPtyId>"]
file_pages: [491]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.11.4.2 ResponsiblePartyIdentification <RspnsblPtyId>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 491 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 491

```text
Identification <Id> contains the following elements (see "PartyIdentification136" on page 488 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 488
   LEI <LEI> [0..1] IdentifierSet 488
13.1.11.4.2  ResponsiblePartyIdentification <RspnsblPtyId>
Presence: [0..1]
Definition: Unique identification of the party responsible for the maintenance of the party reference data.
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 488 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 488
   LEI <LEI> [0..1] IdentifierSet 488
13.1.12 Postal Address
13.1.12.1  CommunicationAddress3
Definition: Communication device number or electronic address used for communication.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 491
   Phone <Phne> [0..1] Text 491
   Mobile <Mob> [0..1] Text 492
   FaxNumber <FaxNb> [0..1] Text 492
   TelexAddress <TlxAdr> [0..1] Text 492
   URLAddress <URLAdr> [0..1] Text 492
13.1.12.1.1  Email <Email>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 534
13.1.12.1.2  Phone <Phne>
Presence: [0..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 535
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 491 March 2024
```

