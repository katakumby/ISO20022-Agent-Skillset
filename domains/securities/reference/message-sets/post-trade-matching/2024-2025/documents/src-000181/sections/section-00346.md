---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.8 ConfirmationPartyDetails16", "7.1.20.8.7 PartyCapacity <PtyCpcty>"]
file_pages: [410]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.8.7 PartyCapacity <PtyCpcty>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 410 to 410.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 410

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.8.7  PartyCapacity <PtyCpcty>
Presence: [0..1]
Definition: Capacity of customer placing the order. Primarily used by futures exchanges to indicate the
CTI code (customer type indicator) as required by the US CFTC (Commodity Futures Trading
Commission).
PartyCapacity <PtyCpcty> contains one of the following elements (see
"TradingPartyCapacity3Choice" on page 389 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 389
Or}   Proprietary <Prtry> [1..1] ± 390
7.1.20.8.8  InvestorProtectionAssociationMembership <InvstrPrtcnAssoctnMmbsh>
Presence: [0..1]
Definition: Indicates whether the confirmation party is a member of the investor protection association
required, eg, as per regulation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.20.9  PartyIdentification116Choice
Definition: Choice of identification of a party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 410 February 2025
```

