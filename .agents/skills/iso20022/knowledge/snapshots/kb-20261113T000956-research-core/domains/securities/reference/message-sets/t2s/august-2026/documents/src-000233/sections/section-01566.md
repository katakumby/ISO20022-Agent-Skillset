---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["47 reda.027.001.01 CloseLinkCreationRequestV01", "47.4 Message Building Blocks", "47.4.2 CloseLink <ClsLk>", "47.4.2.2 PartyIdentification <PtyId>", "47.4.2.2.1 OrganisationIdentification <OrgId>"]
file_pages: [2191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.027.001.01"]
---

# 47.4.2.2.1 OrganisationIdentification <OrgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2191 to 2191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2191

```text
Definition: Identifies the party for which the close link is defined.
PartyIdentification <PtyId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2191
Or}   CombinedIdentification <CmbndId> [1..1] ± 2191
47.4.2.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
47.4.2.2.2  CombinedIdentification <CmbndId>
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
47.4.2.3  CreditProviderIdentification <CdtPrvdrId>
Presence: [0..1]
Definition: Identifies the credit provider party for which the close link information is provided.
CreditProviderIdentification <CdtPrvdrId> contains one of the following
SystemPartyIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2192
Or}   CombinedIdentification <CmbndId> [1..1] ± 2192
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.027.001.01 CloseLinkCreationRequestV01
Target2-Securities 2191 August 2026
```

