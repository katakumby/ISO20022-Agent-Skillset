---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.24 AdditionalInformation <AddtlInf>", "7.4.13.24.1 AdditionalText <AddtlTxt>"]
file_pages: [526]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.24.1 AdditionalText <AddtlTxt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 526 to 526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 526

```text
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..1]  526
     AdditionalInformation <AddtlInf> [1..1] Text 526
   NarrativeVersion <NrrtvVrsn> [0..1]  527
     AdditionalInformation <AddtlInf> [1..1] Text 527
   InformationConditions <InfConds> [0..1]  527
     AdditionalInformation <AddtlInf> [1..*] Text 527
   InformationToComplyWith <InfToCmplyWth> [0..1]  527
     AdditionalInformation <AddtlInf> [1..*] Text 528
   SecurityRestriction <SctyRstrctn> [0..1]  528
     AdditionalInformation <AddtlInf> [1..*] Text 528
   TaxationConditions <TaxtnConds> [0..1]  528
     AdditionalInformation <AddtlInf> [1..*] Text 528
   Disclaimer <Dsclmr> [0..1]  528
     AdditionalInformation <AddtlInf> [1..*] Text 529
   CertificationBreakdown <CertfctnBrkdwn> [0..1]  529
     AdditionalInformation <AddtlInf> [1..*] Text 529
Constraints
• AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
7.4.13.24.1  AdditionalText <AddtlTxt>
Presence: [0..1]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
AdditionalText <AddtlTxt> contains the following UpdatedAdditionalInformation18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalInformation <AddtlInf> [1..1] Text 526
7.4.13.24.1.1  AdditionalInformation <AddtlInf>
Presence: [1..1]
Definition: Provides additional textual information.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 526 February 2026
```

