---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.3 AlternatePartyIdentification10"]
file_pages: [391]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.3 AlternatePartyIdentification10

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 391 to 391.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 391

```text
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 279 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 279
   Issuer <Issr> [1..1] Text 279
   SchemeName <SchmeNm> [0..1] Text 279
7.1.20.3  AlternatePartyIdentification10
Definition: Alternate identification for a party using an id type, a country code and an text field.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TypeOfIdentification <TpOfId> [1..1] ± 391
   Country <Ctry> [1..1] CodeSet C4 391
   AlternateIdentification <AltrnId> [1..1] Text 392
7.1.20.3.1  TypeOfIdentification <TpOfId>
Presence: [1..1]
Definition: Specifies the type of alternate identification which can be used to give an alternate
identification of the party identified.
TypeOfIdentification <TpOfId> contains one of the following elements (see
"IdentificationType42Choice" on page 278 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 278
Or}   Proprietary <Prtry> [1..1] ± 278
7.1.20.3.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which a person resides (the place of a person's home). In the case of a company,
it is the country from which the affairs of that company are directed.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 391 February 2025
```

