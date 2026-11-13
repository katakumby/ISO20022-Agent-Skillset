---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.18 Restriction5Choice"]
file_pages: [308]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.18 Restriction5Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 308 to 308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 308

```text
7.1.19.18  Restriction5Choice
Definition: Choice of format for the securities restriction information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 308
Or}   Proprietary <Prtry> [1..1] ± 308
7.1.19.18.1  Code <Cd>
Presence: [1..1]
Definition: Restrictions expressed as an ISO 20022 code.
Datatype: "OwnershipLegalRestrictions1Code" on page 637
CodeName Name Definition
A144 USLegal144A Ownership or transfer of an unregistered
security issued, pursuant to US legal
restrictions 144A.
NRST NoRestrictions Ownership or transfer of a security that
is not subject to restrictions.
RSTR Restrictions Ownership or transfer of a security that
is subject to restrictions, and not
pursuant to 144A.
7.1.19.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Restrictions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.19  PurposeCode9Choice
Definition: Choice between a code and or a data source scheme to determine the account type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 308
Or}   Proprietary <Prtry> [1..1] ± 309
7.1.19.19.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 308 February 2025
```

