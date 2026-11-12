---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.15 Party Identification", "9.1.15.4 PartyIdentification148", "9.1.15.4.1 Identification <Id>", "9.1.15.4.1.1 AnyBIC <AnyBIC>"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.15.4.1.1 AnyBIC <AnyBIC>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
Identification <Id> contains one of the following PartyIdentification122Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C6 255
Or   NameAndAddress <NmAndAdr> [1..1] ± 255
Or}   Country <Ctry> [1..1] CodeSet C7 255
9.1.15.4.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C6 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 341
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
9.1.15.4.1.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 258 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 258
   Address <Adr> [0..1] ± 258
9.1.15.4.1.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 323
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 255 September 2025
```

