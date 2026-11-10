---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1855]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1855 to 1855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1855

```text
32.4.3.1.1.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..*]
Definition: Way(s) of identifying the security.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C8 "ISINGuideline", C9
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 2945 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2946
   OtherIdentification <OthrId> [0..*]  2947
     Identification <Id> [1..1] Text 2947
     Suffix <Sfx> [0..1] Text 2947
     Type <Tp> [1..1] ± 2947
   Description <Desc> [0..1] Text 2947
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1855 August 2026
```

