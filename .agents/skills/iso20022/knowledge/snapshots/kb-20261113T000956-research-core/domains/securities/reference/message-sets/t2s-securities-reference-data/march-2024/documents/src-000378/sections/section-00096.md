---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["12 reda.034.001.01 SecuritiesAuditTrailReportV01", "12.4 Message Building Blocks", "12.4.2 ReportOrError <RptOrErr>", "12.4.2.2 OperationalError <OprlErr>", "12.4.2.2.1 Error <Err>", "12.4.2.2.1.2 Proprietary <Prtry>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 12.4.2.2.1.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 514
12.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 534
12.4.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 533
12.4.3 SupplementaryData <SplmtryData>
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
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities - Securities Reference Data 145 March 2024
```

