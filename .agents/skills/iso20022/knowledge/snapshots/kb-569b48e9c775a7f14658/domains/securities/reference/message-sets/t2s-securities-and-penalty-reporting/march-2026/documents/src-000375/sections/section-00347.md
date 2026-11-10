---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.13 PartyTextInformation1"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.13 PartyTextInformation1

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 443 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 443
   Address <Adr> [0..1] ± 444
7.1.19.13  PartyTextInformation1
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 434
   PartyContactDetails <PtyCtctDtls> [0..1] Text 434
   RegistrationDetails <RegnDtls> [0..1] Text 434
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
7.1.19.13.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: "Max350Text" on page 557
7.1.19.13.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max140Text" on page 556
7.1.19.13.3  RegistrationDetails <RegnDtls>
Presence: [0..1]
Definition: Provides information required for the registration.
Datatype: "Max350Text" on page 557
7.1.20 Person Identification
7.1.20.1  Contact13
Definition: Specifies the details of the contact person.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 434 March 2026
```

