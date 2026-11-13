---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.26 AdditionalInformation <AddtlInf>", "3.4.11.26.6 TaxationConditions <TaxtnConds>", "3.4.11.26.6.2 AdditionalInformation <AddtlInf>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.26.6.2 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
3.4.11.26.6.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
3.4.11.26.7  Disclaimer <Dsclmr>
Presence: [0..*]
Definition: Provides a disclaimer relative to the information provided in the message. It may be ignored
for automated processing.
Disclaimer <Dsclmr> contains the following UpdatedAdditionalInformation21 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 250
   AdditionalInformation <AddtlInf> [1..*] Text 250
3.4.11.26.7.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.11.26.7.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
3.4.11.26.8  CertificationBreakdown <CertfctnBrkdwn>
Presence: [0..*]
Definition: Provides additional information about the type of certification/breakdown required.
CertificationBreakdown <CertfctnBrkdwn> contains the following UpdatedAdditionalInformation21
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 250
   AdditionalInformation <AddtlInf> [1..*] Text 251
3.4.11.26.8.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 250 February 2026
```

