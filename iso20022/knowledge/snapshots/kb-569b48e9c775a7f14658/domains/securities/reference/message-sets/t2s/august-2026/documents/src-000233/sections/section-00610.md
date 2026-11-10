---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.44 Restriction <Rstrctn>", "27.4.2.3.44.4 InvestorRestrictionType <InvstrRstrctnTp>", "27.4.2.3.44.4.2 Proprietary <Prtry>"]
file_pages: [795]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.44.4.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 795 to 795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 795

```text
CodeName Name Definition
CITI Citizen Restriction applies to a citizen.
INDV Individual Restriction applies to an individual.
27.4.2.3.44.4.2  Proprietary <Prtry>
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
27.4.2.3.44.5  InvestorType <InvstrTp>
Presence: [0..*]
Definition: Type of investor that is allowed to hold the security.
InvestorType <InvstrTp> contains one of the following InvestorType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 795
Or}   Proprietary <Prtry> [1..1] ± 795
27.4.2.3.44.5.1  Code <Cd>
Presence: [1..1]
Definition: Investor type expressed as an ISO 20022 code.
Datatype: "InvestorType1Code" on page 3260
CodeName Name Definition
RETL Retail Investor is a retail investor.
PROF Professional Investor is a professional or institutional
investor.
STAF Staff Investor is an employee.
PPER PhysicalPerson Investor is a physical person.
27.4.2.3.44.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor type expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 795 August 2026
```

