---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.44 Restriction <Rstrctn>", "28.4.2.1.3.2.44.4 InvestorRestrictionType <InvstrRstrctnTp>", "28.4.2.1.3.2.44.4.2 Proprietary <Prtry>"]
file_pages: [1532]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.44.4.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1532 to 1532.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1532

```text
CodeName Name Definition
CITI Citizen Restriction applies to a citizen.
INDV Individual Restriction applies to an individual.
28.4.2.1.3.2.44.4.2  Proprietary <Prtry>
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
28.4.2.1.3.2.44.5  InvestorType <InvstrTp>
Presence: [0..*]
Definition: Type of investor that is allowed to hold the security.
InvestorType <InvstrTp> contains one of the following InvestorType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1532
Or}   Proprietary <Prtry> [1..1] ± 1532
28.4.2.1.3.2.44.5.1  Code <Cd>
Presence: [1..1]
Definition: Investor type expressed as an ISO 20022 code.
Datatype: "InvestorType1Code" on page 3260
CodeName Name Definition
RETL Retail Investor is a retail investor.
PROF Professional Investor is a professional or institutional
investor.
STAF Staff Investor is an employee.
PPER PhysicalPerson Investor is a physical person.
28.4.2.1.3.2.44.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor type expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1532 August 2026
```

