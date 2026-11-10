---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.42 Restriction <Rstrctn>", "32.4.3.1.1.3.42.4 InvestorRestrictionType <InvstrRstrctnTp>", "32.4.3.1.1.3.42.4.2 Proprietary <Prtry>"]
file_pages: [1999]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.42.4.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1999 to 1999.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1999

```text
CodeName Name Definition
CITI Citizen Restriction applies to a citizen.
INDV Individual Restriction applies to an individual.
32.4.3.1.1.3.42.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor restriction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.3.42.5  InvestorType <InvstrTp>
Presence: [0..*]
Definition: Type of investor that is allowed to hold the security.
InvestorType <InvstrTp> contains one of the following InvestorType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1999
Or}   Proprietary <Prtry> [1..1] ± 1999
32.4.3.1.1.3.42.5.1  Code <Cd>
Presence: [1..1]
Definition: Investor type expressed as an ISO 20022 code.
Datatype: "InvestorType1Code" on page 3260
CodeName Name Definition
RETL Retail Investor is a retail investor.
PROF Professional Investor is a professional or institutional
investor.
STAF Staff Investor is an employee.
PPER PhysicalPerson Investor is a physical person.
32.4.3.1.1.3.42.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor type expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1999 August 2026
```

