---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.1 AdditionalText <AddtlTxt>"]
file_pages: [253]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.1 AdditionalText <AddtlTxt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 253 to 253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 253

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Language <Lang> [1..1] CodeSet 260
     URLAddress <URLAdr> [1..1] Text 260
   ProcessingTextForNextIntermediary
<PrcgTxtForNxtIntrmy>
[0..*]  C7 260
     Language <Lang> [1..1] CodeSet 260
     AdditionalInformation <AddtlInf> [1..*] Text 261
Constraints
• AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
3.4.12.1  AdditionalText <AddtlTxt>
Presence: [0..*]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
Impacted by: C7 "AdditionalInformationRule"
AdditionalText <AddtlTxt> contains the following UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 253
   AdditionalInformation <AddtlInf> [1..*] Text 253
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.1.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.1.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 253 February 2026
```

