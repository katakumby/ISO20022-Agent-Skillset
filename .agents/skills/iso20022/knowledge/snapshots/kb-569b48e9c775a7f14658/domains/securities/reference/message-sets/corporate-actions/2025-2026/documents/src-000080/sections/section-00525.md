---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.10 AdditionalInformation <AddtlInf>", "9.4.10.1 AdditionalText <AddtlTxt>"]
file_pages: [689]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.10.1 AdditionalText <AddtlTxt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 689 to 689.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 689

```text
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative31 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..*] Text 689
   NarrativeVersion <NrrtvVrsn> [0..*] Text 689
   PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 689
   TaxationConditions <TaxtnConds> [0..*] Text 689
9.4.10.1  AdditionalText <AddtlTxt>
Presence: [0..*]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
Datatype: "Max350Text" on page 1250
9.4.10.2  NarrativeVersion <NrrtvVrsn>
Presence: [0..*]
Definition: Provides information that can be ignored for automated processing; - reiteration of
information that has been included within structured fields, - or narrative information not needed for
automatic processing.
Datatype: "Max350Text" on page 1250
9.4.10.3  PartyContactNarrative <PtyCtctNrrtv>
Presence: [0..*]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max350Text" on page 1250
9.4.10.4  TaxationConditions <TaxtnConds>
Presence: [0..*]
Definition: Provides taxation conditions that cannot be included within the structured fields of this
message and has not been mentioned in the Service Level Agreement (SLA).
Datatype: "Max350Text" on page 1250
9.4.11 IssuerAgent <IssrAgt>
Presence: [0..*]
Definition: Party appointed to administer the event on behalf of the issuer company/offeror. The party
may be contacted for more information about the event.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 689 February 2026
```

