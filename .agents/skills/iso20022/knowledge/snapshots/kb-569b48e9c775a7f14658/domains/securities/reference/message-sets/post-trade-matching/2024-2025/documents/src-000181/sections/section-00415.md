---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.27 ConfirmationPartyDetails10", "7.1.20.27.7 PartyCapacity <PtyCpcty>"]
file_pages: [481]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.27.7 PartyCapacity <PtyCpcty>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 481 to 481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 481

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.27.7  PartyCapacity <PtyCpcty>
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
7.1.20.28  ConfirmationPartyDetails8
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 481
   AlternateIdentification <AltrnId> [0..1] ± 482
   ProcessingIdentification <PrcgId> [0..1] Text 482
   AdditionalInformation <AddtlInf> [0..1] ± C1 482
7.1.20.28.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 481 February 2025
```

