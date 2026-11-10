---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.2 SettlementParties59", "7.1.26.2.2 Party1 <Pty1>"]
file_pages: [559]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.2.2 Party1 <Pty1>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 559 to 559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 559

```text
Depository <Dpstry> contains the following elements (see "PartyIdentification118" on page 424 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 424
   AlternateIdentification <AltrnId> [0..1] ± 425
   AdditionalInformation <AddtlInf> [0..1] ± C2 425
7.1.26.2.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the depository.
Impacted by: C5 "AdditionalInforrmationRule"
Party1 <Pty1> contains the following PartyIdentificationAndAccount155 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 559
   AdditionalInformation <AddtlInf> [0..1] Text 560
   AlternateIdentification <AltrnId> [0..1] ± 560
   SafekeepingAccount <SfkpgAcct> [0..1] Text 560
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
7.1.26.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 559 February 2025
```

