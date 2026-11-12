---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.5 AlternatePartyIdentification8", "7.1.20.5.3 AlternateIdentification <AltrnId>"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.5.3 AlternateIdentification <AltrnId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.20.5.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Alternate identification for a party.
Datatype: "Max35Text" on page 669
7.1.20.6  PartyIdentificationAndAccount150
Definition: Entity involved in an activity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 399
   SafekeepingAccount <SfkpgAcct> [0..1] Text 400
   CashAccount <CshAcct> [0..1] ± 400
   ProcessingIdentification <PrcgId> [0..1] Text 400
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C4 401
   AdditionalInformation <AddtlInf> [0..1] ± C2 401
   AlternateIdentification <AltrnId> [0..1] ± 401
Constraints
• IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
Following Must be True
    /Identification Must be present
 Or    /CountryOfResidence Must be present
7.1.20.6.1  Identification <Id>
Presence: [0..1]
Definition: Information related to an identification, eg, party identification or account identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 399 February 2025
```

