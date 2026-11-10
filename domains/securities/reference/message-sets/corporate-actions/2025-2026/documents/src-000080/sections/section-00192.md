---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.8 RegistrationDetails <RegnDtls>"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.8 RegistrationDetails <RegnDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
Datatype: "Max8000Text" on page 1252
3.4.12.8  RegistrationDetails <RegnDtls>
Presence: [0..*]
Definition: Provides information required for the registration.
Impacted by: C7 "AdditionalInformationRule"
RegistrationDetails <RegnDtls> contains the following UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 258
   AdditionalInformation <AddtlInf> [1..*] Text 258
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.8.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.8.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max8000Text" on page 1252
3.4.12.9  BasketOrIndexInformation <BsktOrIndxInf>
Presence: [0..*]
Definition: Provides additional information on the basket or index underlying a security, for example a
warrant.
Impacted by: C7 "AdditionalInformationRule"
BasketOrIndexInformation <BsktOrIndxInf> contains the following
UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 259
   AdditionalInformation <AddtlInf> [1..*] Text 259
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 258 February 2026
```

