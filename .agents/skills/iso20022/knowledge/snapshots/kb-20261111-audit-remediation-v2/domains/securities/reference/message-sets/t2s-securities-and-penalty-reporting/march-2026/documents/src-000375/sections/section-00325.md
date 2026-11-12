---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.1 AlternatePartyIdentification7", "7.1.19.1.2 Country <Ctry>"]
file_pages: [412]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.1.2 Country <Ctry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 412 to 412.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 412

```text
IdentificationType <IdTp> contains one of the following elements (see "IdentificationType42Choice"
on page 349 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 349
Or}   Proprietary <Prtry> [1..1] ± 350
7.1.19.1.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.19.1.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Alternate identification for a party.
Datatype: "Max35Text" on page 557
7.1.19.2  PartyIdentification144
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 412
   LEI <LEI> [0..1] IdentifierSet 413
7.1.19.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification127Choice" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 413
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 413
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 412 March 2026
```

