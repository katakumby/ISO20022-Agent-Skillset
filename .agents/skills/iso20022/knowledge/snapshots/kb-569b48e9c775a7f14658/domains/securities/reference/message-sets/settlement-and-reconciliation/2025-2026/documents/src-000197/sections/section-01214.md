---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.7 PartyIdentificationAndAccount165", "35.1.18.7.3 AlternateIdentification <AltrnId>"]
file_pages: [1671]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.7.3 AlternateIdentification <AltrnId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1671 to 1671.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1671

```text
Datatype: "LEIIdentifier" on page 2187
35.1.18.7.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1691 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1691
   Country <Ctry> [1..1] CodeSet C7 1691
   AlternateIdentification <AltrnId> [1..1] Text 1691
35.1.18.7.4  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 2192
35.1.18.7.5  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C5 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 1690 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 1690
   PartyContactDetails <PtyCtctDtls> [0..1] Text 1690
   RegistrationDetails <RegnDtls> [0..1] Text 1691
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
35.1.18.8  PartyIdentification136
Definition: Identification of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1671 March 2026
```

