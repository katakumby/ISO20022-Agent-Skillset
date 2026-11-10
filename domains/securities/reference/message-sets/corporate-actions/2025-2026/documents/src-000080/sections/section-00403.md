---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.14 AdditionalInformation <AddtlInf>", "7.4.14.4 InformationToComplyWith <InfToCmplyWth>"]
file_pages: [532]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.14.4 InformationToComplyWith <InfToCmplyWth>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 532 to 532.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 532

```text
7.4.14.4  InformationToComplyWith <InfToCmplyWth>
Presence: [0..1]
Definition: Provides information conditions to the account owner that are to be complied with, for
example, not open to US/Canadian residents, Qualified Institutional Buyers (QIB) or SIL (Sophisticated
Investor Letter) to be provided.
InformationToComplyWith <InfToCmplyWth> contains the following
UpdatedAdditionalInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalInformation <AddtlInf> [1..*] Text 532
7.4.14.4.1  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
7.4.14.5  TaxationConditions <TaxtnConds>
Presence: [0..1]
Definition: Provides taxation conditions that cannot be included within the structured fields of this
message and has not been mentioned in the Service Level Agreement (SLA).
TaxationConditions <TaxtnConds> contains the following UpdatedAdditionalInformation17
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalInformation <AddtlInf> [1..*] Text 532
7.4.14.5.1  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
7.4.14.6  Disclaimer <Dsclmr>
Presence: [0..1]
Definition: Provides a disclaimer relative to the information provided in the message. It may be ignored
for automated processing.
Disclaimer <Dsclmr> contains the following UpdatedAdditionalInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalInformation <AddtlInf> [1..*] Text 533
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 532 February 2026
```

