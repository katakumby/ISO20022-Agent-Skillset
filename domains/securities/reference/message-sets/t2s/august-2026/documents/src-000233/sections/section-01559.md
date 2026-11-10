---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "46.4 Message Building Blocks", "46.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>", "46.4.2.2 EligibleCounterpartIdentification <ElgblCntrptId>", "46.4.2.2.1 OrganisationIdentification <OrgId>"]
file_pages: [2183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 46.4.2.2.1 OrganisationIdentification <OrgId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2183 to 2183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2183

```text
EligibleCounterpartIdentification <ElgblCntrptId> contains one of the following
SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2183
Or}   CombinedIdentification <CmbndId> [1..1] ± 2183
46.4.2.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
46.4.2.2.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
46.4.2.3  ValidFrom <VldFr>
Presence: [1..1]
Definition: Date from when the eligible counterpart is valid.
Datatype: "ISODate" on page 3319
46.4.2.4  ValidTo <VldTo>
Presence: [0..1]
Definition: Date until when the eligible counterpart is valid.
Datatype: "ISODate" on page 3319
46.4.2.5  EligibilityType <ElgbltyTp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities 2183 August 2026
```

