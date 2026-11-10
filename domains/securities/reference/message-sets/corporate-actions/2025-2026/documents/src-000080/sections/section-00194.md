---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.12.11 URLAddress <URLAdr>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.12.11 URLAddress <URLAdr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
3.4.12.11  URLAddress <URLAdr>
Presence: [0..*]
Definition: Provides the web address published for the event, that is, the address for the Universal
Resource Locator (URL), for example, used over the www (HTTP) service.
URLAddress <URLAdr> contains the following UpdatedURLlnformation6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 260
   URLAddress <URLAdr> [1..1] Text 260
3.4.12.11.1  Language <Lang>
Presence: [1..1]
Definition: Language used to provide additional information and using the ISO 639-1 language code
standard.
Datatype: "ISO2ALanguageCode" on page 1218
3.4.12.11.2  URLAddress <URLAdr>
Presence: [1..1]
Definition: Provides the web address, that is, the address for the Universal Resource Locator (URL), to
use over the www (HTTP) service where additional information may be found.
Datatype: "Max2048Text" on page 1249
3.4.12.12  ProcessingTextForNextIntermediary <PrcgTxtForNxtIntrmy>
Presence: [0..*]
Definition: Provides additional information from the account servicer or a service provider solely
intended for the next immediate account holder to enable or facilitate event processing between parties.
Impacted by: C7 "AdditionalInformationRule"
ProcessingTextForNextIntermediary <PrcgTxtForNxtIntrmy> contains the following
UpdatedAdditionalInformation20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 260
   AdditionalInformation <AddtlInf> [1..*] Text 261
Constraints
• AdditionalInformationRule
The Additionalnformation element must not contain information that can be provided in a structured
field unless bilaterally agreed.
3.4.12.12.1  Language <Lang>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 260 February 2026
```

