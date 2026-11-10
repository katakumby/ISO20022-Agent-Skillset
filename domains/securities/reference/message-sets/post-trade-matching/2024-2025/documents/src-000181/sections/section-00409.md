---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.24 PartyIdentification117", "7.1.20.24.3 NameAndAddress <NmAndAdr>", "7.1.20.24.3.2 Address <Adr>", "7.1.20.24.3.2.8 Country <Ctry>"]
file_pages: [475]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.24.3.2.8 Country <Ctry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 475 to 475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 475

```text
7.1.20.24.3.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.20.25  PartyIdentificationAndAccount152
Definition: Entity involved in an activity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 475
   ProcessingIdentification <PrcgId> [0..1] Text 475
   AdditionalInformation <AddtlInf> [0..1] ± C2 475
   AlternateIdentification <AltrnId> [0..1] ± 476
7.1.20.25.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Identification <Id> contains one of the following elements (see "PartyIdentification245Choice" on
page 464 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 464
Or   ProprietaryIdentification <PrtryId> [1..1] ± 464
Or}   NameAndAddress <NmAndAdr> [1..1] ± 464
7.1.20.25.2  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Reference meaningful to the party identified.
Datatype: "Max35Text" on page 669
7.1.20.25.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C2 "AdditonalDetailsGuideline"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 475 February 2025
```

