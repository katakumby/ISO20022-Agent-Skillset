---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.42 Restriction <Rstrctn>", "13.1.6.3.42.2 RestrictionType <RstrctnTp>", "13.1.6.3.42.2.1 RestrictionType <RstrctnTp>"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.42.2.1 RestrictionType <RstrctnTp>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
13.1.6.3.42.2.1  RestrictionType <RstrctnTp>
Presence: [1..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
Datatype: "RestrictionType1Code" on page 522
CodeName Name Definition
SELR Selling Selling restriction.
BUYR Buying Buying restriction.
PLAR Placing Placing restriction.
HOLR Holding Holding restriction.
VOTR Voting Voting restriction.
13.1.6.3.42.2.2  ProprietaryRestriction <PrtryRstrctn>
Presence: [1..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
ProprietaryRestriction <PrtryRstrctn> contains the following elements (see "GenericIdentification30"
on page 478 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.3.42.3  LegalRestrictionType <LglRstrctnTp>
Presence: [0..1]
Definition: Specifies the regulatory restrictions applicable to a security.
LegalRestrictionType <LglRstrctnTp> contains one of the following LegalRestrictions5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 366
Or}   Proprietary <Prtry> [1..1] ± 367
13.1.6.3.42.3.1  Code <Cd>
Presence: [1..1]
Definition: Legal restrictions expressed as an ISO 20022 code.
Datatype: "LegalRestrictions2Code" on page 518
CodeName Name Definition
JURO JurisdictionOwnership Investors outside this jurisdiction can
purchase this security, for example, a
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 366 March 2024
```

