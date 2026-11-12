---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.3 InformationConditions <InfConds>", "3.4.12.3.1 Language <Lang>"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.3.1 Language <Lang>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.3.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.3.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
3.4.12.4  InformationToComplyWith <InfToCmplyWth>
Presence: [0..*]
Definition: Provides information conditions to the account owner that are to be complied with, for
example, not open to US/Canadian residents, Qualified Institutional Buyers (QIB) or SIL (Sophisticated
Investor Letter) to be provided.
Impacted by: C7 "AdditionalInformationRule"
InformationToComplyWith <InfToCmplyWth> contains the following
UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 255
   AdditionalInformation <AddtlInf> [1..*] Text 255
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.4.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.4.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 255 February 2026
```

