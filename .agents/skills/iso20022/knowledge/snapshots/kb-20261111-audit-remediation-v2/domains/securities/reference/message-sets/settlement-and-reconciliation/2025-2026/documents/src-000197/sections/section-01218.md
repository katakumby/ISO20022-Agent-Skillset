---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.10 Pledgee3"]
file_pages: [1675]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.10 Pledgee3

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1675 to 1675.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1675

```text
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
35.1.18.10  Pledgee3
Definition: Identifies the entity to which the financial instruments are pledged.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PledgeeTypeAndIdentification <PldgeeTpAndId> [0..1]  1675
{Or     TypeAndIdentification <TpAndId> [1..1]  1676
       Identification <Id> [1..1] IdentifierSet C5 1676
       PledgeeType <PldgeeTp> [1..1] CodeSet 1676
Or     Identification <Id> [1..1]  1677
       Identification <Id> [0..1] Text 1677
       PledgeeType <PldgeeTp> [1..1] CodeSet 1677
Or}     Proprietary <Prtry> [1..1] ± 1677
   LEI <LEI> [0..1] IdentifierSet 1678
Constraints
• PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
Following Must be True
    /PledgeeTypeAndIdentification Must be present
 Or    /LEI Must be present
35.1.18.10.1  PledgeeTypeAndIdentification <PldgeeTpAndId>
Presence: [0..1]
Definition: Unique identification of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1675 March 2026
```

