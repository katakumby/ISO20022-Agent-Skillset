---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.5 AdditionalText <AddtlTxt>"]
file_pages: [715]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.5 AdditionalText <AddtlTxt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 715 to 715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 715

```text
11.4.5 AdditionalText <AddtlTxt>
Presence: [0..*]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
Datatype: "Max8000Text" on page 1252
11.4.6 IssuerAgent <IssrAgt>
Presence: [0..*]
Definition: Party appointed to administer the event on behalf of the issuer company/offeror. The party
may be contacted for more information about the event.
IssuerAgent <IssrAgt> contains one of the following elements (see "PartyIdentification120Choice" on
page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
11.4.7 PayingAgent <PngAgt>
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
11.4.8 SubPayingAgent <SubPngAgt>
Presence: [0..*]
Definition: Sub-agent appointed to execute the payment for the corporate action event on behalf of the
issuer company/offeror.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 715 February 2026
```

