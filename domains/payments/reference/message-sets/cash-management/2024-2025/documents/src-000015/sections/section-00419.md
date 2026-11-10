---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.4 Message Building Blocks", "20.4.2 ReportOrError <RptOrErr>", "20.4.2.2 BusinessReport <BizRpt>", "20.4.2.2.1 BusinessInformationReference <BizInfRef>"]
file_pages: [573]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.4.2.2.1 BusinessInformationReference <BizInfRef>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 573 to 573.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 573

```text
BusinessReport <BizRpt> contains the following GeneralBusinessReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BusinessInformationReference <BizInfRef> [1..1] Text 573
   GeneralBusinessOrError <GnlBizOrErr> [1..1]  573
{Or     BusinessError <BizErr> [1..*]  574
       Error <Err> [1..1]  574
{Or         Code <Cd> [1..1] CodeSet 574
Or}         Proprietary <Prtry> [1..1] Text 575
       Description <Desc> [0..1] Text 575
Or}     GeneralBusiness <GnlBiz> [1..1]  575
       Qualifier <Qlfr> [0..1]  575
         IsFormatted <IsFrmtd> [0..1] Indicator 575
         Priority <Prty> [0..1] CodeSet 576
       Subject <Sbjt> [0..1] Text 576
       SubjectDetails <SbjtDtls> [0..1] Text 576
20.4.2.2.1  BusinessInformationReference <BizInfRef>
Presence: [1..1]
Definition: Unique and unambiguous identification of a general business information system, as
assigned by the system transaction administrator.
Datatype: "Max35Text" on page 889
20.4.2.2.2  GeneralBusinessOrError <GnlBizOrErr>
Presence: [1..1]
Definition: Requested business information.
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 573 February 2025
```

