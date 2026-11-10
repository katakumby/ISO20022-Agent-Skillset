---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.1 Depository <Dpstry>", "7.1.26.1.1.1 Identification <Id>", "7.1.26.1.1.1.2 NameAndAddress <NmAndAdr>", "7.1.26.1.1.1.2.2 Address <Adr>", "7.1.26.1.1.1.2.2.8 Country <Ctry>"]
file_pages: [530]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.1.1.2.2.8 Country <Ctry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 530 to 530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
7.1.26.1.1.1.2.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.26.1.1.1.3  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.26.1.1.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.26.1.1.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C2 "AdditonalDetailsGuideline"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 530 February 2025
```

