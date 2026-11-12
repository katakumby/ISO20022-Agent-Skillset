---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["6 reda.040.001.01 CashAccountAuditTrailReportV01", "6.4 Message Building Blocks", "6.4.2 ReportOrError <RptOrErr>", "6.4.2.2 OperationalError <OprlErr>"]
file_pages: [128, 129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.040.001.01"]
---

# 6.4.2.2 OperationalError <OprlErr>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 128 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
6.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Operational error resulting from a rejection.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  128
{Or     Code <Cd> [1..1] CodeSet 128
Or}     Proprietary <Prtry> [1..1] Text 128
   Description <Desc> [0..1] Text 128
6.4.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 128
Or}   Proprietary <Prtry> [1..1] Text 128
6.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 178
6.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 183
6.4.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 182
6.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.040.001.01 CashAccountAuditTrailReportV01
Target2-Securities - Cash Account Query and Report 128 August 2026
```

## File page 129

```text
Impacted by: C5 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 147 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 147
   Envelope <Envlp> [1..1] (External Schema) 147
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.040.001.01 CashAccountAuditTrailReportV01
Target2-Securities - Cash Account Query and Report 129 August 2026
```

