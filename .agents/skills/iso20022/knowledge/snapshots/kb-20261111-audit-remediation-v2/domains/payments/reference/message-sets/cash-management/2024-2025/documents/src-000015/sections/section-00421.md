---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.4 Message Building Blocks", "20.4.2 ReportOrError <RptOrErr>", "20.4.2.2 BusinessReport <BizRpt>", "20.4.2.2.2 GeneralBusinessOrError <GnlBizOrErr>", "20.4.2.2.2.1 BusinessError <BizErr>", "20.4.2.2.2.1.1 Error <Err>", "20.4.2.2.2.1.1.2 Proprietary <Prtry>"]
file_pages: [575]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.4.2.2.2.1.1.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 575 to 575.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 575

```text
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 857
20.4.2.2.2.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 889
20.4.2.2.2.1.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
20.4.2.2.2.2  GeneralBusiness <GnlBiz>
Presence: [1..1]
Definition: Requested business information.
GeneralBusiness <GnlBiz> contains the following GeneralBusinessInformation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Qualifier <Qlfr> [0..1]  575
     IsFormatted <IsFrmtd> [0..1] Indicator 575
     Priority <Prty> [0..1] CodeSet 576
   Subject <Sbjt> [0..1] Text 576
   SubjectDetails <SbjtDtls> [0..1] Text 576
20.4.2.2.2.2.1  Qualifier <Qlfr>
Presence: [0..1]
Definition: Further information about the criticality or importance of a general business information
system.
Qualifier <Qlfr> contains the following InformationQualifierType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IsFormatted <IsFrmtd> [0..1] Indicator 575
   Priority <Prty> [0..1] CodeSet 576
20.4.2.2.2.2.1.1  IsFormatted <IsFrmtd>
Presence: [0..1]
Definition: Indicates whether the information is formatted.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 886):
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 575 February 2025
```

