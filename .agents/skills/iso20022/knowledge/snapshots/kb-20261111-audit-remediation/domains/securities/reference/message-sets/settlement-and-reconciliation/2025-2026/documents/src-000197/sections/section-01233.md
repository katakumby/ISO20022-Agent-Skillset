---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.19 PartyIdentification120Choice", "35.1.18.19.3 NameAndAddress <NmAndAdr>"]
file_pages: [1690]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.19.3 NameAndAddress <NmAndAdr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1690 to 1690.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1690

```text
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 1497 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1497
   Issuer <Issr> [1..1] Text 1497
   SchemeName <SchmeNm> [0..1] Text 1497
35.1.18.19.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 1704 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1704
   Address <Adr> [0..1] ± 1704
35.1.18.20  PartyTextInformation1
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
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
35.1.18.20.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: "Max350Text" on page 2192
35.1.18.20.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1690 March 2026
```

