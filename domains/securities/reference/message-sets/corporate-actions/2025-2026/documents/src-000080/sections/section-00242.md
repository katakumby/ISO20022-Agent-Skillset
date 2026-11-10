---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.11 AdditionalInformation <AddtlInf>", "5.4.11.1 RegistrationDetails <RegnDtls>"]
file_pages: [319]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.11.1 RegistrationDetails <RegnDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 319 to 319.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 319

```text
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative30 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RegistrationDetails <RegnDtls> [0..*] Text 319
   PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 319
   CertificationBreakdown <CertfctnBrkdwn> [0..*] Text 319
5.4.11.1  RegistrationDetails <RegnDtls>
Presence: [0..*]
Definition: Provides information required for the registration.
Datatype: "Max350Text" on page 1250
5.4.11.2  PartyContactNarrative <PtyCtctNrrtv>
Presence: [0..*]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max350Text" on page 1250
5.4.11.3  CertificationBreakdown <CertfctnBrkdwn>
Presence: [0..*]
Definition: Provides information required for the certification/breakdown.
Datatype: "Max350Text" on page 1250
5.4.12 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C30 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 924
   Envelope <Envlp> [1..1] (External Schema) 924
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 319 February 2026
```

