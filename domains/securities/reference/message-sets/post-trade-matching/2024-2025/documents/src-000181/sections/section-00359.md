---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.12 ConfirmationPartyDetails9", "7.1.20.12.5 InvestorProtectionAssociationMembership <InvstrPrtcnAssoctnMmbsh>"]
file_pages: [424]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.12.5 InvestorProtectionAssociationMembership <InvstrPrtcnAssoctnMmbsh>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 424 to 424.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 424

```text
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation5" on
page 441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 442
   PartyContactDetails <PtyCtctDtls> [0..1] Text 442
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.12.5  InvestorProtectionAssociationMembership <InvstrPrtcnAssoctnMmbsh>
Presence: [0..1]
Definition: Indicates whether the confirmation party is a member of the investor protection association
required, eg, as per regulation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.20.13  PartyIdentification118
Definition: Identification of an entity involved in an activity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 424
   AlternateIdentification <AltrnId> [0..1] ± 425
   AdditionalInformation <AddtlInf> [0..1] ± C2 425
7.1.20.13.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 424 February 2025
```

