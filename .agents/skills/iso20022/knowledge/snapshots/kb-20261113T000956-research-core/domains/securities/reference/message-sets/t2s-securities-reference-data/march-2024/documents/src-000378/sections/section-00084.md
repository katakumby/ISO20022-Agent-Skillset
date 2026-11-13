---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["11 reda.033.001.01 SecuritiesAuditTrailQueryV01", "11.4 Message Building Blocks", "11.4.2 SearchCriteria <SchCrit>", "11.4.2.2 DatePeriod <DtPrd>", "11.4.2.2.4 EqualDate <EQDt>"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 11.4.2.2.4 EqualDate <EQDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 235 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 235
   ToDate <ToDt> [1..1] Date 236
11.4.2.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 529
11.4.2.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 529
11.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 486 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 486
   Envelope <Envlp> [1..1] (External Schema) 486
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities - Securities Reference Data 133 March 2024
```

