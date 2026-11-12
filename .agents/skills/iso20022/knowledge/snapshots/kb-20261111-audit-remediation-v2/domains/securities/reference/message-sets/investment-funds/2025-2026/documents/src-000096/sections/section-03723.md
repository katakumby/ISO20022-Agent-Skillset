---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.23 Intermediary48", "66.1.30.23.3 Role <Role>", "66.1.30.23.3.2 Proprietary <Prtry>"]
file_pages: [5009]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.23.3.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5009 to 5009.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5009

```text
CodeName Name Definition
CACO CashCorrespondent Financial institution that executes cash
transfers on behalf of its clients.
CONC Concentrator Party that acts as an aggregator of
funds, also called a funds hub.
DATP DataProvider Source of financial information. Provides
financial news and data (for example,
facts, statistics and analysis), for
professional and individual investors
through various media, for example, the
Internet, magazines.
66.1.30.23.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Role of the party in the activity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.30.23.4  ContactPerson <CtctPrsn>
Presence: [0..1]
Definition: Contact person and contact information.
ContactPerson <CtctPrsn> contains the following elements (see "ContactIdentification2" on
page 5095 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 5095
   GivenName <GvnNm> [0..1] Text 5095
   Name <Nm> [1..1] Text 5096
   PhoneNumber <PhneNb> [0..1] Text 5096
   MobileNumber <MobNb> [0..1] Text 5096
   FaxNumber <FaxNb> [0..1] Text 5096
   EmailAddress <EmailAdr> [0..1] Text 5096
66.1.30.24  PartyIdentificationAndAccount194
Definition: Party and account details.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5009 May 2026
```

