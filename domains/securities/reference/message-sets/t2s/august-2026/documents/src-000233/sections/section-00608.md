---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.44 Restriction <Rstrctn>", "27.4.2.3.44.2 RestrictionType <RstrctnTp>", "27.4.2.3.44.2.1 RestrictionType <RstrctnTp>"]
file_pages: [793]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.44.2.1 RestrictionType <RstrctnTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 793 to 793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 793

```text
27.4.2.3.44.2.1  RestrictionType <RstrctnTp>
Presence: [1..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
Datatype: "RestrictionType1Code" on page 3289
CodeName Name Definition
SELR Selling Selling restriction.
BUYR Buying Buying restriction.
PLAR Placing Placing restriction.
HOLR Holding Holding restriction.
VOTR Voting Voting restriction.
27.4.2.3.44.2.2  ProprietaryRestriction <PrtryRstrctn>
Presence: [1..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
ProprietaryRestriction <PrtryRstrctn> contains the following elements (see "GenericIdentification30"
on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
27.4.2.3.44.3  LegalRestrictionType <LglRstrctnTp>
Presence: [0..1]
Definition: Specifies the regulatory restrictions applicable to a security.
LegalRestrictionType <LglRstrctnTp> contains one of the following LegalRestrictions5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 793
Or}   Proprietary <Prtry> [1..1] ± 794
27.4.2.3.44.3.1  Code <Cd>
Presence: [1..1]
Definition: Legal restrictions expressed as an ISO 20022 code.
Datatype: "LegalRestrictions2Code" on page 3261
CodeName Name Definition
JURO JurisdictionOwnership Investors outside this jurisdiction can
purchase this security, for example, a
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 793 August 2026
```

