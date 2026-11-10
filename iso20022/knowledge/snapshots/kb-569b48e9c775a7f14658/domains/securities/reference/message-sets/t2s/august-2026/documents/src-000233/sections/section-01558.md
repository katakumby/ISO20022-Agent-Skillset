---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "46.4 Message Building Blocks", "46.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>", "46.4.2.1 IssuerIdentification <IssrId>"]
file_pages: [2182]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 46.4.2.1 IssuerIdentification <IssrId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2182 to 2182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2182

```text
46.4.2.1  IssuerIdentification <IssrId>
Presence: [1..1]
Definition: Unique business identifier code used to identify the party providing the eligible counterpart
information.
IssuerIdentification <IssrId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2182
Or}   CombinedIdentification <CmbndId> [1..1] ± 2182
46.4.2.1.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
46.4.2.1.2  CombinedIdentification <CmbndId>
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
46.4.2.2  EligibleCounterpartIdentification <ElgblCntrptId>
Presence: [1..1]
Definition: Unique business identifier code used to identify the central securities depository to be
defined as eligible.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities 2182 August 2026
```

