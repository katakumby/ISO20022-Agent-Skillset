---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.4 ConfirmationPartyDetails14", "7.1.20.4.7 PartyCapacity <PtyCpcty>"]
file_pages: [398]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.4.7 PartyCapacity <PtyCpcty>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 398 to 398.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 398

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.4.7  PartyCapacity <PtyCpcty>
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
7.1.20.5  AlternatePartyIdentification8
Definition: Alternate identification for a party using an identification type, a country code and a text field.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.20.5.1  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the type of alternate identification of the party identified.
IdentificationType <IdTp> contains one of the following elements (see "IdentificationType43Choice"
on page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 277
Or}   Proprietary <Prtry> [1..1] ± 277
7.1.20.5.2  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 398 February 2025
```

