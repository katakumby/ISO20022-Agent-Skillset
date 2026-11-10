---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.2 SettlementParties59", "7.1.26.2.4 Party3 <Pty3>"]
file_pages: [563]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.2.4 Party3 <Pty3>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 563 to 563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 563

```text
Datatype: "Max35Text" on page 669
7.1.26.2.4  Party3 <Pty3>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 2.
Impacted by: C5 "AdditionalInforrmationRule"
Party3 <Pty3> contains the following PartyIdentificationAndAccount155 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 563
   AdditionalInformation <AddtlInf> [0..1] Text 564
   AlternateIdentification <AltrnId> [0..1] ± 564
   SafekeepingAccount <SfkpgAcct> [0..1] Text 564
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
7.1.26.2.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 563 February 2025
```

