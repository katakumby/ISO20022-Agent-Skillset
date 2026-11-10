---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "9.4 Message Building Blocks", "9.4.2 SearchCriteria <SchCrit>", "9.4.2.2 DatePeriod <DtPrd>", "9.4.2.2.4 EqualDate <EQDt>"]
file_pages: [67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 9.4.2.2.4 EqualDate <EQDt>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 67 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 67

```text
9.4.2.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 97
9.4.2.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 97
9.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C1 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 84 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 84
   Envelope <Envlp> [1..1] (External Schema) 84
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities - Securities Account Reference Data 67 December 2019
```

