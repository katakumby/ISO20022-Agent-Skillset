---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.26 AdditionalInformation <AddtlInf>", "3.4.11.26.1 AdditionalText <AddtlTxt>"]
file_pages: [246]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.26.1 AdditionalText <AddtlTxt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 246 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative59 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..*]  246
     Language <Lang> [1..1] CodeSet 247
     AdditionalInformation <AddtlInf> [1..1] Text 247
   NarrativeVersion <NrrtvVrsn> [0..*]  247
     Language <Lang> [1..1] CodeSet 247
     AdditionalInformation <AddtlInf> [1..1] Text 247
   InformationConditions <InfConds> [0..*]  248
     Language <Lang> [1..1] CodeSet 248
     AdditionalInformation <AddtlInf> [1..*] Text 248
   InformationToComplyWith <InfToCmplyWth> [0..*]  248
     Language <Lang> [1..1] CodeSet 248
     AdditionalInformation <AddtlInf> [1..*] Text 248
   SecurityRestriction <SctyRstrctn> [0..*]  249
     Language <Lang> [1..1] CodeSet 249
     AdditionalInformation <AddtlInf> [1..*] Text 249
   TaxationConditions <TaxtnConds> [0..*]  249
     Language <Lang> [1..1] CodeSet 249
     AdditionalInformation <AddtlInf> [1..*] Text 250
   Disclaimer <Dsclmr> [0..*]  250
     Language <Lang> [1..1] CodeSet 250
     AdditionalInformation <AddtlInf> [1..*] Text 250
   CertificationBreakdown <CertfctnBrkdwn> [0..*]  250
     Language <Lang> [1..1] CodeSet 250
     AdditionalInformation <AddtlInf> [1..*] Text 251
Constraints
• AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
3.4.11.26.1  AdditionalText <AddtlTxt>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 246 February 2026
```

