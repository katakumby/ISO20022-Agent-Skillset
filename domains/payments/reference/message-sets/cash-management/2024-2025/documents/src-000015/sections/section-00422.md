---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.4 Message Building Blocks", "20.4.2 ReportOrError <RptOrErr>", "20.4.2.2 BusinessReport <BizRpt>", "20.4.2.2.2 GeneralBusinessOrError <GnlBizOrErr>", "20.4.2.2.2.2 GeneralBusiness <GnlBiz>", "20.4.2.2.2.2.1 Qualifier <Qlfr>", "20.4.2.2.2.2.1.2 Priority <Prty>"]
file_pages: [576]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.4.2.2.2.2.1.2 Priority <Prty>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 576 to 576.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 576

```text
• Meaning When True: Yes
• Meaning When False: No
20.4.2.2.2.2.1.2  Priority <Prty>
Presence: [0..1]
Definition: Priority of the information.
Datatype: "Priority1Code" on page 871
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
LOWW Low Priority level is low.
20.4.2.2.2.2.2  Subject <Sbjt>
Presence: [0..1]
Definition: Subject line of an item of general business information, summarizing the topic and intended
destination of the information.
Datatype: "Max35Text" on page 889
20.4.2.2.2.2.3  SubjectDetails <SbjtDtls>
Presence: [0..1]
Definition: General business information, in unstructured form.
Datatype: "Max350Text" on page 889
20.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C1 "SupplementaryDataRule"
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
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 576 February 2025
```

