---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.42 Restriction <Rstrctn>", "32.4.3.1.1.3.42.3 LegalRestrictionType <LglRstrctnTp>", "32.4.3.1.1.3.42.3.2 Proprietary <Prtry>"]
file_pages: [1998]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.42.3.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1998 to 1998.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1998

```text
CodeName Name Definition
Reg S security can only be held by an
investor outside the US.
PPLA PrivatePlacements Only investors qualified by the issuer in
this jurisdiction may purchase this
security.
ACRI AccreditedInvestor Only investors qualified by the regulator
in this jurisdiction may purchase this
security.
MARG Margin Issuer defines whether the security may
be purchased with borrowed money (US
and Japan).
PRIV Privilege Privileges, for example, voting rights, of
holding the security may be restricted by
the issuer.
32.4.3.1.1.3.42.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Legal restrictions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.3.42.4  InvestorRestrictionType <InvstrRstrctnTp>
Presence: [0..*]
Definition: Specifies whether the restriction to be applied is relevant for citizen, resident, country.
InvestorRestrictionType <InvstrRstrctnTp> contains one of the following
InvestorRestrictionType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1998
Or}   Proprietary <Prtry> [1..1] ± 1999
32.4.3.1.1.3.42.4.1  Code <Cd>
Presence: [1..1]
Definition: Investor restriction type expressed as an ISO 20022 code.
Datatype: "InvestorRestrictionType1Code" on page 3260
CodeName Name Definition
LERE LegalResident Restriction applies to a legal resident.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1998 August 2026
```

