---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.2 Structure"]
file_pages: [559]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 559 to 559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 559

```text
Common business identification for the message.
B. GeneralBusinessInformationQueryDefinition
Definition of the general business information query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
19.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <GetGnlBizInf> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 560
   GeneralBusinessInformationQueryDefinition
<GnlBizInfQryDef>
[0..1]  560
     QueryType <QryTp> [0..1] CodeSet 561
     GeneralBusinessInformationCriteria <GnlBizInfCrit> [0..1]  562
{Or       QueryName <QryNm> [1..1] Text 562
Or}       NewCriteria <NewCrit> [1..1]  C1 562
         NewQueryName <NewQryNm> [0..1] Text 563
         SearchCriteria <SchCrit> [0..*]  563
           Reference <Ref> [0..*] Text 564
           Subject <Sbjt> [0..*]  564
{Or             Equal <EQ> [1..1] Text 564
Or             NotEqual <NEQ> [1..1] Text 564
Or             Contain <CT> [1..1] Text 565
Or}             NotContain <NCT> [1..1] Text 565
           Qualifier <Qlfr> [0..*]  565
             IsFormatted <IsFrmtd> [0..1] Indicator 565
             Priority <Prty> [0..1] CodeSet 565
         ReturnCriteria <RtrCrit> [0..1]  565
           QualifierIndicator <QlfrInd> [0..1] Indicator 566
           SubjectIndicator <SbjtInd> [0..1] Indicator 566
           SubjectDetailsIndicator <SbjtDtlsInd> [0..1] Indicator 566
   SupplementaryData <SplmtryData> [0..*] ± C2 566
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 559 February 2025
```

