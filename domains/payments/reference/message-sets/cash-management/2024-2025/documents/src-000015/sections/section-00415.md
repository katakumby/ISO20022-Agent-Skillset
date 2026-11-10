---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.2 Structure"]
file_pages: [569]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 569 to 569.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 569

```text
Report on the Business Information.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
20.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RtrGnlBizInf> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 570
   ReportOrError <RptOrErr> [1..1]  570
{Or     OperationalError <OprlErr> [1..*]  571
       Error <Err> [1..1]  572
{Or         Code <Cd> [1..1] CodeSet 572
Or}         Proprietary <Prtry> [1..1] Text 572
       Description <Desc> [0..1] Text 572
Or}     BusinessReport <BizRpt> [1..*]  572
       BusinessInformationReference <BizInfRef> [1..1] Text 573
       GeneralBusinessOrError <GnlBizOrErr> [1..1]  573
{Or         BusinessError <BizErr> [1..*]  574
           Error <Err> [1..1]  574
{Or             Code <Cd> [1..1] CodeSet 574
Or}             Proprietary <Prtry> [1..1] Text 575
           Description <Desc> [0..1] Text 575
Or}         GeneralBusiness <GnlBiz> [1..1]  575
           Qualifier <Qlfr> [0..1]  575
             IsFormatted <IsFrmtd> [0..1] Indicator 575
             Priority <Prty> [0..1] CodeSet 576
           Subject <Sbjt> [0..1] Text 576
           SubjectDetails <SbjtDtls> [0..1] Text 576
   SupplementaryData <SplmtryData> [0..*] ± C1 576
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 569 February 2025
```

