---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.42 Restriction <Rstrctn>", "13.1.6.3.42.4 InvestorRestrictionType <InvstrRstrctnTp>", "13.1.6.3.42.4.2 Proprietary <Prtry>"]
file_pages: [368]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.42.4.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 368 to 368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
CodeName Name Definition
CITI Citizen Restriction applies to a citizen.
INDV Individual Restriction applies to an individual.
13.1.6.3.42.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor restriction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.3.42.5  InvestorType <InvstrTp>
Presence: [0..*]
Definition: Type of investor that is allowed to hold the security.
InvestorType <InvstrTp> contains one of the following InvestorType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 368
Or}   Proprietary <Prtry> [1..1] ± 368
13.1.6.3.42.5.1  Code <Cd>
Presence: [1..1]
Definition: Investor type expressed as an ISO 20022 code.
Datatype: "InvestorType1Code" on page 518
CodeName Name Definition
RETL Retail Investor is a retail investor.
PROF Professional Investor is a professional or institutional
investor.
STAF Staff Investor is an employee.
PPER PhysicalPerson Investor is a physical person.
13.1.6.3.42.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor type expressed as a proprietary code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 368 March 2024
```

