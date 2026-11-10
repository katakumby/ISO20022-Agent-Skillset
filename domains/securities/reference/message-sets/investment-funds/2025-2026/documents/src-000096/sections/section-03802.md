---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.16 PoliticallyExposedPerson <PltclyXpsdPrsn>", "66.1.32.7.16.2 PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts>", "66.1.32.7.16.2.2 Proprietary <Prtry>"]
file_pages: [5091]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.16.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5091 to 5091.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5091

```text
Definition: Status of the politically exposed person expressed as a code.
Datatype: "PoliticallyExposedPersonStatus1Code" on page 5342
CodeName Name Definition
PE03 CloseAssociate Person known to be a close associate of
the politically exposed person. A person
known to be a close associate includes:
(a) a natural person who is known to
have joint beneficial ownership of legal
entities or legal arrangements, or any
other close business relations, with the
politically exposed person,
(b) a natural person who has sole
beneficial ownership of a legal entity or
legal arrangement which is known to
have been set up for the de facto benefit
of a politically exposed person.
PE01 NaturalPersonEntrusted Natural person who is or who has been
entrusted with prominent public
functions.
PE02 FamilyMember Family member of the politically exposed
person. A family member includes:
(a) the spouse, or a person considered
to be equivalent to a spouse, of the
politically exposed person,
(b) the children and their spouses, or
persons considered to be equivalent to a
spouse, of the politically exposed
person,
(c) the parents of the politically exposed
person.
66.1.32.7.16.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Status of the politically exposed person expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.7.17  DeathDate <DthDt>
Presence: [0..1]
Definition: Date of death.
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5091 May 2026
```

