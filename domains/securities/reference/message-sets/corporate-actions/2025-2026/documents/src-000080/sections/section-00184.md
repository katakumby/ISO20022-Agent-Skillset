---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.26 AdditionalInformation <AddtlInf>", "3.4.11.26.5 SecurityRestriction <SctyRstrctn>"]
file_pages: [249]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.26.5 SecurityRestriction <SctyRstrctn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 249 to 249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 249

```text
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
3.4.11.26.5  SecurityRestriction <SctyRstrctn>
Presence: [0..*]
Definition: Provides restriction(s) on securities.
SecurityRestriction <SctyRstrctn> contains the following UpdatedAdditionalInformation21
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 249
   AdditionalInformation <AddtlInf> [1..*] Text 249
3.4.11.26.5.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.11.26.5.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
3.4.11.26.6  TaxationConditions <TaxtnConds>
Presence: [0..*]
Definition: Provides taxation conditions that cannot be included within the structured fields of this
message and has not been mentioned in the Service Level Agreement (SLA).
TaxationConditions <TaxtnConds> contains the following UpdatedAdditionalInformation21
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 249
   AdditionalInformation <AddtlInf> [1..*] Text 250
3.4.11.26.6.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 249 February 2026
```

