---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.6 CollateralValueReport <CollValRpt>", "3.4.2.1.6.2 CollateralValue <CollVal>", "3.4.2.1.6.2.4 Securities <Scties>", "3.4.2.1.6.2.4.2 Position <Pos>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.6.2.4.2 Position <Pos>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
Identification <Id> contains the following elements (see "SecurityIdentification19" on page 52 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 53
   OtherIdentification <OthrId> [0..*]  54
     Identification <Id> [1..1] Text 54
     Suffix <Sfx> [0..1] Text 54
     Type <Tp> [1..1] ± 54
   Description <Desc> [0..1] Text 54
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
    /ISIN Must be present
 Or    /Description Must be present
3.4.2.1.6.2.4.2  Position <Pos>
Presence: [0..*]
Definition: Specifies the position for the security.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
33 March 2024
```

