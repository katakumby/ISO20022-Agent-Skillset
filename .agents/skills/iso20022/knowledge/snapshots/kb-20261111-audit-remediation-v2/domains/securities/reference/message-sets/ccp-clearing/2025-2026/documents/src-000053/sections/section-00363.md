---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.11 PartyIdentification254Choice", "12.1.14.11.2 ProprietaryIdentification <PrtryId>"]
file_pages: [456]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.11.2 ProprietaryIdentification <PrtryId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 456 to 456.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 456

```text
– Error Text: Invalid BIC.
12.1.14.11.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see GenericIdentification36 on
page 399 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 399
   Issuer <Issr> [1..1] Text 400
   SchemeName <SchmeNm> [0..1] Text 400
12.1.14.11.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
NameAndAddress <NmAndAdr> contains the following NameAndAddress6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 456
   Address <Adr> [1..1] ± 456
12.1.14.11.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: Max70Text on page 493
12.1.14.11.3.2  Address <Adr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Address <Adr> contains the following elements (see PostalAddress2 on page 467 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StreetName <StrtNm> [0..1] Text 467
   PostCodeIdentification <PstCdId> [1..1] Text 467
   TownName <TwnNm> [1..1] Text 467
   CountrySubDivision <CtrySubDvsn> [0..1] Text 467
   Country <Ctry> [1..1] CodeSet   'C5 467
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 456
```

