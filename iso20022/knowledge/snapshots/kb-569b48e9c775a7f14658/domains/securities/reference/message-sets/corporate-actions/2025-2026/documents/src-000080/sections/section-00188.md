---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.2 NarrativeVersion <NrrtvVrsn>"]
file_pages: [254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.2 NarrativeVersion <NrrtvVrsn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 254 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 254

```text
3.4.12.2  NarrativeVersion <NrrtvVrsn>
Presence: [0..*]
Definition: Provides information that can be ignored for automated processing; - reiteration of
information that has been included within structured fields, - or narrative information not needed for
automatic processing.
Impacted by: C7 "AdditionalInformationRule"
NarrativeVersion <NrrtvVrsn> contains the following UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 254
   AdditionalInformation <AddtlInf> [1..*] Text 254
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.2.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.2.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
3.4.12.3  InformationConditions <InfConds>
Presence: [0..*]
Definition: Provides conditional information related to the event, for example, an offer is subject to 50
percent acceptance, the offeror allows the securities holder to set some conditions.
Impacted by: C7 "AdditionalInformationRule"
InformationConditions <InfConds> contains the following UpdatedAdditionalInformation20
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 255
   AdditionalInformation <AddtlInf> [1..*] Text 255
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 254 February 2026
```

