---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.5 TaxationConditions <TaxtnConds>"]
file_pages: [256]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.5 TaxationConditions <TaxtnConds>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 256 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
3.4.12.5  TaxationConditions <TaxtnConds>
Presence: [0..*]
Definition: Provides taxation conditions that cannot be included within the structured fields of this
message and has not been mentioned in the Service Level Agreement (SLA).
Impacted by: C7 "AdditionalInformationRule"
TaxationConditions <TaxtnConds> contains the following UpdatedAdditionalInformation20
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 256
   AdditionalInformation <AddtlInf> [1..*] Text 256
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.5.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.5.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
3.4.12.6  Disclaimer <Dsclmr>
Presence: [0..*]
Definition: Provides a disclaimer relative to the information provided in the message. It may be ignored
for automated processing.
Impacted by: C7 "AdditionalInformationRule"
Disclaimer <Dsclmr> contains the following UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 257
   AdditionalInformation <AddtlInf> [1..*] Text 257
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 256 February 2026
```

