---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.26 AdditionalInformation <AddtlInf>", "3.4.11.26.1 AdditionalText <AddtlTxt>", "3.4.11.26.1.1 Language <Lang>"]
file_pages: [247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.26.1.1 Language <Lang>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 247 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
AdditionalText <AddtlTxt> contains the following UpdatedAdditionalInformation19 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 247
   AdditionalInformation <AddtlInf> [1..1] Text 247
3.4.11.26.1.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.11.26.1.2  AdditionalInformation <AddtlInf>
Presence: [1..1]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
3.4.11.26.2  NarrativeVersion <NrrtvVrsn>
Presence: [0..*]
Definition: Provides information that can be ignored for automated processing; - reiteration of
information that has been included within structured fields, - or narrative information not needed for
automatic processing.
NarrativeVersion <NrrtvVrsn> contains the following UpdatedAdditionalInformation19 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 247
   AdditionalInformation <AddtlInf> [1..1] Text 247
3.4.11.26.2.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.11.26.2.2  AdditionalInformation <AddtlInf>
Presence: [1..1]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 247 February 2026
```

