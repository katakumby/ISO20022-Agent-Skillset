---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.55 GlobalType <GblTp>", "13.1.2.3.55.2 Proprietary <Prtry>"]
file_pages: [222]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.55.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 222 to 222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

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
13.1.2.3.55.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Global note expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.3.56  PotentialEuroSystemEligibility <PotntlEuroSysElgblty>
Presence: [0..1]
Definition: Flag to indicate the security is intended to be held in a manner that could allow the
Eurosystem eligibility.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.57  Geographics <Geogcs>
Presence: [0..1]
Definition: Type of stipulation expressing geographical constraints on a fixed income instrument. It is
expressed with a state or country abbreviation and a minimum or maximum percentage. Example: CA
0-80 (minimum of 80 percent in Californian assets).
Datatype: "Max35Text" on page 534
13.1.2.3.58  YieldRange <YldRg>
Presence: [0..1]
Definition: Range of allowed yield.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 222 March 2024
```

