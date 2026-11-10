---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["11 reda.033.001.01 SecuritiesAuditTrailQueryV01", "11.4 Message Building Blocks", "11.4.2 SearchCriteria <SchCrit>", "11.4.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [131]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 11.4.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 131 to 131.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 131

```text
SearchCriteria <SchCrit> contains the following SecuritiesAuditTrailSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C1, C2,
C3, C4,
C5
131
   DatePeriod <DtPrd> [0..1]  132
{Or     FromDate <FrDt> [1..1] Date 132
Or     ToDate <ToDt> [1..1] Date 132
Or     FromToDate <FrToDt> [1..1] ± 132
Or     EqualDate <EQDt> [1..1] Date 133
Or}     NotEqualDate <NEQDt> [1..1] Date 133
11.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Describes security to be queried.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
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
• DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities - Securities Reference Data 131 March 2024
```

