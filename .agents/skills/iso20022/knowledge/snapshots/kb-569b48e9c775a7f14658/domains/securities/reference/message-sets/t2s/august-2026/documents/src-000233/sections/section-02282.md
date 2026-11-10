---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.5 PartyIdentificationAndAccount197", "82.1.20.5.8 AdditionalInformation <AddtlInf>"]
file_pages: [3063]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.5.8 AdditionalInformation <AddtlInf>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3063 to 3063.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3063

```text
Datatype: "Max35Text" on page 3328
82.1.20.5.8  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C1 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 3080 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 3080
   PartyContactDetails <PtyCtctDtls> [0..1] Text 3080
   RegistrationDetails <RegnDtls> [0..1] Text 3080
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
82.1.20.6  Pledgee3
Definition: Identifies the entity to which the financial instruments are pledged.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PledgeeTypeAndIdentification <PldgeeTpAndId> [0..1]  3064
{Or     TypeAndIdentification <TpAndId> [1..1]  3064
       Identification <Id> [1..1] IdentifierSet C2 3064
       PledgeeType <PldgeeTp> [1..1] CodeSet 3065
Or     Identification <Id> [1..1]  3065
       Identification <Id> [0..1] Text 3065
       PledgeeType <PldgeeTp> [1..1] CodeSet 3065
Or}     Proprietary <Prtry> [1..1] ± 3066
   LEI <LEI> [0..1] IdentifierSet 3066
Constraints
• PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3063 August 2026
```

