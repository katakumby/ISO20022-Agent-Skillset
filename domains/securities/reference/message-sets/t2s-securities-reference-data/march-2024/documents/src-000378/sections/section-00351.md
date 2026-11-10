---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.44 Restriction <Rstrctn>", "13.1.6.4.44.3 LegalRestrictionType <LglRstrctnTp>", "13.1.6.4.44.3.2 Proprietary <Prtry>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.44.3.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

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
13.1.6.4.44.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Legal restrictions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.44.4  InvestorRestrictionType <InvstrRstrctnTp>
Presence: [0..*]
Definition: Specifies whether the restriction to be applied is relevant for citizen, resident, country.
InvestorRestrictionType <InvstrRstrctnTp> contains one of the following
InvestorRestrictionType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 444
Or}   Proprietary <Prtry> [1..1] ± 445
13.1.6.4.44.4.1  Code <Cd>
Presence: [1..1]
Definition: Investor restriction type expressed as an ISO 20022 code.
Datatype: "InvestorRestrictionType1Code" on page 517
CodeName Name Definition
LERE LegalResident Restriction applies to a legal resident.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 444 March 2024
```

