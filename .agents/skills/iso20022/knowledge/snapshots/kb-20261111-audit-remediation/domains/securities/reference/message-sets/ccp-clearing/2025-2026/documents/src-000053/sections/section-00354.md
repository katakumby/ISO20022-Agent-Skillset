---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.4 PartyIdentification34Choice", "12.1.14.4.2 NameAndAddress <NmAndAdr>"]
file_pages: [447]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.4.2 NameAndAddress <NmAndAdr>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 447 to 447.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 447

```text
– Error Text: Invalid BIC.
12.1.14.4.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation, using the name and address.
NameAndAddress <NmAndAdr> contains the following elements (see NameAndAddress5 on
page 460 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 460
   Address <Adr> [0..1] ± 460
12.1.14.4.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation using the country code, using the
country code.
Impacted by:   'C5 Country  '
Datatype: CountryCode on page 475
Constraints
• Country
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
12.1.14.5  PartyIdentification33Choice
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 448
Or   ProprietaryIdentification <PrtryId> [1..1] ± 448
Or}   NameAndAddress <NmAndAdr> [1..1]  448
     Name <Nm> [1..1] Text 449
     Address <Adr> [1..1] ± 449
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 447
```

