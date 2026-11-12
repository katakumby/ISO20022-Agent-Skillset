---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.15 IssuerAgent <IssrAgt>"]
file_pages: [535]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.15 IssuerAgent <IssrAgt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 535 to 535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 535

```text
7.4.15 IssuerAgent <IssrAgt>
Presence: [0..*]
Definition: Party appointed to administer the event on behalf of the issuer company/offeror. The party
may be contacted for more information about the event.
IssuerAgent <IssrAgt> contains one of the following elements (see "PartyIdentification129Choice" on
page 1042 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1043
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1043
Or   NameAndAddress <NmAndAdr> [1..1] ± 1043
Or}   LEI <LEI> [1..1] IdentifierSet 1043
7.4.16 PayingAgent <PngAgt>
Presence: [0..*]
Definition: Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate
action event on behalf of the issuer company/offeror.
PayingAgent <PngAgt> contains one of the following elements (see "PartyIdentification120Choice" on
page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
7.4.17 SubPayingAgent <SubPngAgt>
Presence: [0..*]
Definition: Sub-agent appointed to execute the payment for the corporate action event on behalf of the
issuer company/offeror.
SubPayingAgent <SubPngAgt> contains one of the following elements (see
"PartyIdentification120Choice" on page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 535 February 2026
```

