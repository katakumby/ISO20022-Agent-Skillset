---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.19 ConfirmationPartyDetails7", "7.1.20.19.3 ProcessingIdentification <PrcgId>"]
file_pages: [446]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.19.3 ProcessingIdentification <PrcgId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 446 to 446.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.20.19.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 669
7.1.20.19.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C1 "AdditonalDetailsGuideline"
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
7.1.20.19.5  InvestorCapacity <InvstrCpcty>
Presence: [0..1]
Definition: Capacity of customer placing the order. Primarily used by futures exchanges to indicate the
CTI code (customer type indicator) as required by the US CFTC (Commodity Futures Trading
Commission).
InvestorCapacity <InvstrCpcty> contains one of the following elements (see
"InvestorCapacity4Choice" on page 302 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 302
Or}   Proprietary <Prtry> [1..1] ± 302
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 446 February 2025
```

