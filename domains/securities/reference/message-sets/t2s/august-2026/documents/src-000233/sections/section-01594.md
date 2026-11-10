---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["53 reda.033.001.01 SecuritiesAuditTrailQueryV01", "53.4 Message Building Blocks", "53.4.2 SearchCriteria <SchCrit>", "53.4.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [2221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 53.4.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2221 to 2221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2221

```text
SearchCriteria <SchCrit> contains the following SecuritiesAuditTrailSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C1, C2,
C3, C4,
C5
2221
   DatePeriod <DtPrd> [0..1]  2222
{Or     FromDate <FrDt> [1..1] Date 2222
Or     ToDate <ToDt> [1..1] Date 2222
Or     FromToDate <FrToDt> [1..1] ± 2222
Or     EqualDate <EQDt> [1..1] Date 2223
Or}     NotEqualDate <NEQDt> [1..1] Date 2223
53.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Describes security to be queried.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities 2221 August 2026
```

