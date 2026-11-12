---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.18 PartyIdentificationAndAccount149", "7.1.20.18.4 ClearingAccount <ClrAcct>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.18.4 ClearingAccount <ClrAcct>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
CodeName Name Definition
BORW Borrow Clearing member is on the borrowing
side.
7.1.20.18.4  ClearingAccount <ClrAcct>
Presence: [0..1]
Definition: Identifies the clearing member account at the CCP through which the trade must be cleared
(sometimes called position account).
ClearingAccount <ClrAcct> contains the following elements (see "SecuritiesAccount20" on page 222
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 222
   Type <Tp> [1..1] CodeSet 222
   Name <Nm> [0..1] Text 222
7.1.20.18.5  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 669
7.1.20.18.6  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C2 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation1" on
page 484 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 484
   PartyContactDetails <PtyCtctDtls> [0..1] Text 484
   RegistrationDetails <RegnDtls> [0..1] Text 484
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.19  ConfirmationPartyDetails7
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 444 February 2025
```

