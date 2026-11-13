---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.4 Message Building Blocks", "19.4.2 GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef>", "19.4.2.2 GeneralBusinessInformationCriteria <GnlBizInfCrit>", "19.4.2.2.2 NewCriteria <NewCrit>", "19.4.2.2.2.3 ReturnCriteria <RtrCrit>", "19.4.2.2.2.3.1 QualifierIndicator <QlfrInd>"]
file_pages: [566, 567]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.4.2.2.2.3.1 QualifierIndicator <QlfrInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 566 to 567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 566

```text
ReturnCriteria <RtrCrit> contains the following GeneralBusinessInformationReturnCriteria1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QualifierIndicator <QlfrInd> [0..1] Indicator 566
   SubjectIndicator <SbjtInd> [0..1] Indicator 566
   SubjectDetailsIndicator <SbjtDtlsInd> [0..1] Indicator 566
19.4.2.2.2.3.1  QualifierIndicator <QlfrInd>
Presence: [0..1]
Definition: Indicates whether the qualifier is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
19.4.2.2.2.3.2  SubjectIndicator <SbjtInd>
Presence: [0..1]
Definition: Indicates whether the subject is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
19.4.2.2.2.3.3  SubjectDetailsIndicator <SbjtDtlsInd>
Presence: [0..1]
Definition: Indicates whether the subject details are requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
19.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C2 "SupplementaryDataRule"
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 566 February 2025
```

## File page 567

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 567 February 2025
```

