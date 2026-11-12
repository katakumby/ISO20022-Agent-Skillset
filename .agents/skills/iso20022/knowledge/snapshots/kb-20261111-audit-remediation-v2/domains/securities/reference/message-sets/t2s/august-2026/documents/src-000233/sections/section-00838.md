---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.55 GlobalType <GblTp>", "28.4.2.1.2.1.3.55.2 Proprietary <Prtry>"]
file_pages: [1245]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.55.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1245 to 1245.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1245

```text
CodeName Name Definition
NGNO NewGlobalNote Form of global certificate which refers to
the books and records of the ICSDs to
determine the Issue Outstanding Amount
(IOA).
CGNO ClassicalGlobalNote Form of global certificate which requires
physical annotation on the attached
schedule to reflect changes in the Issue
Outstanding Amount (IOA).
28.4.2.1.2.1.3.55.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Global note expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.2.1.3.56  PotentialEuroSystemEligibility <PotntlEuroSysElgblty>
Presence: [0..1]
Definition: Flag to indicate the security is intended to be held in a manner that could allow the
Eurosystem eligibility.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.2.1.3.57  Geographics <Geogcs>
Presence: [0..1]
Definition: Type of stipulation expressing geographical constraints on a fixed income instrument. It is
expressed with a state or country abbreviation and a minimum or maximum percentage. Example: CA
0-80 (minimum of 80 percent in Californian assets).
Datatype: "Max35Text" on page 3328
28.4.2.1.2.1.3.58  YieldRange <YldRg>
Presence: [0..1]
Definition: Range of allowed yield.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1245 August 2026
```

