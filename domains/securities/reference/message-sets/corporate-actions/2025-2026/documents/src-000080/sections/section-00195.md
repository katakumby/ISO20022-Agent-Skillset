---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.12 ProcessingTextForNextIntermediary <PrcgTxtForNxtIntrmy>", "3.4.12.12.2 AdditionalInformation <AddtlInf>"]
file_pages: [261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.12.2 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 261 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.12.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
3.4.13 IssuerAgent <IssrAgt>
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
3.4.14 PayingAgent <PngAgt>
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
3.4.15 SubPayingAgent <SubPngAgt>
Presence: [0..*]
Definition: Sub-agent appointed to execute the payment for the corporate action event on behalf of the
issuer company/offeror.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 261 February 2026
```

