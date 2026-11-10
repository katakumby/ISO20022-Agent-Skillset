---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.6 Pledgee3"]
file_pages: [417]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.6 Pledgee3

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 417 to 417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 417

```text
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 434 for details)
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
7.1.19.6  Pledgee3
Definition: Identifies the entity to which the financial instruments are pledged.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PledgeeTypeAndIdentification <PldgeeTpAndId> [0..1]  417
{Or     TypeAndIdentification <TpAndId> [1..1]  418
       Identification <Id> [1..1] IdentifierSet C2 418
       PledgeeType <PldgeeTp> [1..1] CodeSet 418
Or     Identification <Id> [1..1]  419
       Identification <Id> [0..1] Text 419
       PledgeeType <PldgeeTp> [1..1] CodeSet 419
Or}     Proprietary <Prtry> [1..1] ± 419
   LEI <LEI> [0..1] IdentifierSet 420
Constraints
• PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
Following Must be True
    /PledgeeTypeAndIdentification Must be present
 Or    /LEI Must be present
7.1.19.6.1  PledgeeTypeAndIdentification <PldgeeTpAndId>
Presence: [0..1]
Definition: Unique identification of the party.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 417 March 2026
```

