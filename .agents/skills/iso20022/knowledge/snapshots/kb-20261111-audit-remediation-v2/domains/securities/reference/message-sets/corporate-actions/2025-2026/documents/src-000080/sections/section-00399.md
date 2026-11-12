---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.24 AdditionalInformation <AddtlInf>", "7.4.13.24.4 InformationToComplyWith <InfToCmplyWth>", "7.4.13.24.4.1 AdditionalInformation <AddtlInf>"]
file_pages: [528]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.24.4.1 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 528 to 528.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 528

```text
7.4.13.24.4.1  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
7.4.13.24.5  SecurityRestriction <SctyRstrctn>
Presence: [0..1]
Definition: Provides restriction(s) on securities.
SecurityRestriction <SctyRstrctn> contains the following UpdatedAdditionalInformation17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalInformation <AddtlInf> [1..*] Text 528
7.4.13.24.5.1  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
7.4.13.24.6  TaxationConditions <TaxtnConds>
Presence: [0..1]
Definition: Provides taxation conditions that cannot be included within the structured fields of this
message and has not been mentioned in the Service Level Agreement (SLA).
TaxationConditions <TaxtnConds> contains the following UpdatedAdditionalInformation17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalInformation <AddtlInf> [1..*] Text 528
7.4.13.24.6.1  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
7.4.13.24.7  Disclaimer <Dsclmr>
Presence: [0..1]
Definition: Provides a disclaimer relative to the information provided in the message. It may be ignored
for automated processing.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 528 February 2026
```

