---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "70.4 Message Building Blocks", "70.4.2 SearchCriteria <SchCrit>", "70.4.2.5 CountryOfIssue <CtryOfIsse>"]
file_pages: [2406]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70.4.2.5 CountryOfIssue <CtryOfIsse>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2406 to 2406.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2406

```text
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
70.4.2.5  CountryOfIssue <CtryOfIsse>
Presence: [0..1]
Definition: Country where the security is issued.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
70.4.2.6  SubBalanceType <SubBalTp>
Presence: [0..1]
Definition: Defines specific restriction characteristics for a securities position.
SubBalanceType <SubBalTp> contains one of the following elements (see
"SecuritiesBalanceType7Choice" on page 2851 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2852
Or}   Proprietary <Prtry> [1..1] ± 2853
70.4.2.7  ReturnZeroPosition <RtrZeroPos>
Presence: [1..1]
Definition: Option to provide output zero position in the results.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2406 August 2026
```

