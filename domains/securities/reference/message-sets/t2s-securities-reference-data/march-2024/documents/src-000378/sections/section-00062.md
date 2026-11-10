---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.4 Message Building Blocks", "7.4.3 SecurityReportOrError <SctyRptOrErr>", "7.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "7.4.3.1.2 BusinessError <BizErr>"]
file_pages: [111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.4.3.1.2 BusinessError <BizErr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 111 to 111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 111

```text
7.4.3.1.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Provides the business error details.
BusinessError <BizErr> contains the following BusinessError4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
111
   BusinessError <BizErr> [1..*]  112
     Error <Err> [1..1]  112
{Or       Code <Cd> [1..1] CodeSet 112
Or}       Proprietary <Prtry> [1..1] Text 113
     Description <Desc> [0..1] Text 113
7.4.3.1.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Way(s) of identifying the security.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C8 "ISINGuideline", C9
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 475
   OtherIdentification <OthrId> [0..*]  475
     Identification <Id> [1..1] Text 475
     Suffix <Sfx> [0..1] Text 475
     Type <Tp> [1..1] ± 475
   Description <Desc> [0..1] Text 476
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 111 March 2024
```

