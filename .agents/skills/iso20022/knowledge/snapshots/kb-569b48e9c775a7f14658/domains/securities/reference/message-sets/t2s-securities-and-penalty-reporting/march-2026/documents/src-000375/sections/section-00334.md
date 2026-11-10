---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.7 PartyIdentification148", "7.1.19.7.1 Identification <Id>", "7.1.19.7.1.3 Country <Ctry>"]
file_pages: [421]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.7.1.3 Country <Ctry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 421 to 421.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 421

```text
Definition: Unique and unambiguous way to identify an organisation.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 443 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 443
   Address <Adr> [0..1] ± 444
7.1.19.7.1.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.19.7.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 552
7.1.19.7.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 557
7.1.19.8  PartyIdentification272
Definition: Specifies the identification of a person or an organisation.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 421 March 2026
```

