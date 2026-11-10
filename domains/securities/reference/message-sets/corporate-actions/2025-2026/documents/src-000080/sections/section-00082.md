---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.36 AdditionalInformation <AddtlInf>"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.36 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
3.4.10.36  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information. This field may only be used when the information to be
transmitted, cannot be coded.
Impacted by: C4 "AdditionalInformationRule"
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative58 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Offeror <Offerr> [0..*] Text 128
   NewCompanyName <NewCpnyNm> [0..1] Text 128
   URLAddress <URLAdr> [0..*]  128
     Language <Lang> [1..1] CodeSet 129
     URLAddress <URLAdr> [1..1] Text 129
   EventProcessingWebSiteAddress
<EvtPrcgWebSiteAdr>
[0..1] Text 129
Constraints
• AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition.
3.4.10.36.1  Offeror <Offerr>
Presence: [0..*]
Definition: Provides the entity making the offer and is different from the issuing company.
Datatype: "Max350Text" on page 1250
3.4.10.36.2  NewCompanyName <NewCpnyNm>
Presence: [0..1]
Definition: Provides the new name of a company following a name change.
Datatype: "Max350Text" on page 1250
3.4.10.36.3  URLAddress <URLAdr>
Presence: [0..*]
Definition: Provides the web address published for the event, that is, the address for the Universal
Resource Locator (URL), for example, used over the www (HTTP) service.
URLAddress <URLAdr> contains the following UpdatedURLlnformation6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Language <Lang> [1..1] CodeSet 129
   URLAddress <URLAdr> [1..1] Text 129
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 128 February 2026
```

