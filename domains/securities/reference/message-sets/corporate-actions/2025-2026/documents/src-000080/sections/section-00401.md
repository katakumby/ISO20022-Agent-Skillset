---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.14 AdditionalInformation <AddtlInf>", "7.4.14.1 AdditionalText <AddtlTxt>"]
file_pages: [530]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.14.1 AdditionalText <AddtlTxt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 530 to 530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative56 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..1]  530
     AdditionalInformation <AddtlInf> [1..*] Text 531
   NarrativeVersion <NrrtvVrsn> [0..1]  531
     AdditionalInformation <AddtlInf> [1..*] Text 531
   InformationConditions <InfConds> [0..1]  531
     AdditionalInformation <AddtlInf> [1..*] Text 531
   InformationToComplyWith <InfToCmplyWth> [0..1]  532
     AdditionalInformation <AddtlInf> [1..*] Text 532
   TaxationConditions <TaxtnConds> [0..1]  532
     AdditionalInformation <AddtlInf> [1..*] Text 532
   Disclaimer <Dsclmr> [0..1]  532
     AdditionalInformation <AddtlInf> [1..*] Text 533
   PartyContactNarrative <PtyCtctNrrtv> [0..1]  533
     AdditionalInformation <AddtlInf> [1..*] Text 533
   RegistrationDetails <RegnDtls> [0..1]  533
     AdditionalInformation <AddtlInf> [1..*] Text 533
   BasketOrIndexInformation <BsktOrIndxInf> [0..1]  533
     AdditionalInformation <AddtlInf> [1..*] Text 534
   CertificationBreakdown <CertfctnBrkdwn> [0..1]  534
     AdditionalInformation <AddtlInf> [1..*] Text 534
   ProcessingTextForNextIntermediary
<PrcgTxtForNxtIntrmy>
[0..1]  534
     AdditionalInformation <AddtlInf> [1..*] Text 534
Constraints
• AdditionalInformationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
7.4.14.1  AdditionalText <AddtlTxt>
Presence: [0..1]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 530 February 2026
```

