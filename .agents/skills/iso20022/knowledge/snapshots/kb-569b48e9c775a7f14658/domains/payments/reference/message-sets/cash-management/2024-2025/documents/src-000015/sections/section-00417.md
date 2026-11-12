---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.4 Message Building Blocks", "20.4.2 ReportOrError <RptOrErr>", "20.4.2.1 OperationalError <OprlErr>"]
file_pages: [571]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.4.2.1 OperationalError <OprlErr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 571 to 571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 571

```text
ReportOrError <RptOrErr> contains one of the following GeneralBusinessOrError7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OperationalError <OprlErr> [1..*]  571
     Error <Err> [1..1]  572
{Or       Code <Cd> [1..1] CodeSet 572
Or}       Proprietary <Prtry> [1..1] Text 572
     Description <Desc> [0..1] Text 572
Or}   BusinessReport <BizRpt> [1..*]  572
     BusinessInformationReference <BizInfRef> [1..1] Text 573
     GeneralBusinessOrError <GnlBizOrErr> [1..1]  573
{Or       BusinessError <BizErr> [1..*]  574
         Error <Err> [1..1]  574
{Or           Code <Cd> [1..1] CodeSet 574
Or}           Proprietary <Prtry> [1..1] Text 575
         Description <Desc> [0..1] Text 575
Or}       GeneralBusiness <GnlBiz> [1..1]  575
         Qualifier <Qlfr> [0..1]  575
           IsFormatted <IsFrmtd> [0..1] Indicator 575
           Priority <Prty> [0..1] CodeSet 576
         Subject <Sbjt> [0..1] Text 576
         SubjectDetails <SbjtDtls> [0..1] Text 576
20.4.2.1  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates that an operational error has been issued during the processing of the related
request.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  572
{Or     Code <Cd> [1..1] CodeSet 572
Or}     Proprietary <Prtry> [1..1] Text 572
   Description <Desc> [0..1] Text 572
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 571 February 2025
```

