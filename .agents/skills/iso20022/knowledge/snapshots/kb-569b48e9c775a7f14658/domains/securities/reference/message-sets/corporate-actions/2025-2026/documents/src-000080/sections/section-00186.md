---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.26 AdditionalInformation <AddtlInf>", "3.4.11.26.8 CertificationBreakdown <CertfctnBrkdwn>", "3.4.11.26.8.2 AdditionalInformation <AddtlInf>"]
file_pages: [251, 252]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.26.8.2 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 251 to 252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 251

```text
3.4.11.26.8.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Provides additional textual information.
Datatype: "Max350Text" on page 1250
3.4.12 AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information on the event.
Impacted by: C6 "AdditionalInformationRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 251 February 2026
```

## File page 252

```text
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative60 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..*]  C7 253
     Language <Lang> [1..1] CodeSet 253
     AdditionalInformation <AddtlInf> [1..*] Text 253
   NarrativeVersion <NrrtvVrsn> [0..*]  C7 254
     Language <Lang> [1..1] CodeSet 254
     AdditionalInformation <AddtlInf> [1..*] Text 254
   InformationConditions <InfConds> [0..*]  C7 254
     Language <Lang> [1..1] CodeSet 255
     AdditionalInformation <AddtlInf> [1..*] Text 255
   InformationToComplyWith <InfToCmplyWth> [0..*]  C7 255
     Language <Lang> [1..1] CodeSet 255
     AdditionalInformation <AddtlInf> [1..*] Text 255
   TaxationConditions <TaxtnConds> [0..*]  C7 256
     Language <Lang> [1..1] CodeSet 256
     AdditionalInformation <AddtlInf> [1..*] Text 256
   Disclaimer <Dsclmr> [0..*]  C7 256
     Language <Lang> [1..1] CodeSet 257
     AdditionalInformation <AddtlInf> [1..*] Text 257
   PartyContactNarrative <PtyCtctNrrtv> [0..*]  C7 257
     Language <Lang> [1..1] CodeSet 257
     AdditionalInformation <AddtlInf> [1..*] Text 257
   RegistrationDetails <RegnDtls> [0..*]  C7 258
     Language <Lang> [1..1] CodeSet 258
     AdditionalInformation <AddtlInf> [1..*] Text 258
   BasketOrIndexInformation <BsktOrIndxInf> [0..*]  C7 258
     Language <Lang> [1..1] CodeSet 259
     AdditionalInformation <AddtlInf> [1..*] Text 259
   CertificationBreakdown <CertfctnBrkdwn> [0..*]  C7 259
     Language <Lang> [1..1] CodeSet 259
     AdditionalInformation <AddtlInf> [1..*] Text 259
   URLAddress <URLAdr> [0..*]  260
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 252 February 2026
```

