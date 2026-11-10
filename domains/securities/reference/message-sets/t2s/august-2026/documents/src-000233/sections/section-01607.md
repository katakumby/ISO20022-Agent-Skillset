---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["54 reda.034.001.01 SecuritiesAuditTrailReportV01", "54.4 Message Building Blocks", "54.4.2 ReportOrError <RptOrErr>", "54.4.2.2 OperationalError <OprlErr>"]
file_pages: [2234]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 54.4.2.2 OperationalError <OprlErr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2234 to 2234.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2234

```text
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
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
54.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Operational error resulting from a rejection.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2234
{Or     Code <Cd> [1..1] CodeSet 2234
Or}     Proprietary <Prtry> [1..1] Text 2235
   Description <Desc> [0..1] Text 2235
54.4.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2234
Or}   Proprietary <Prtry> [1..1] Text 2235
54.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities 2234 August 2026
```

