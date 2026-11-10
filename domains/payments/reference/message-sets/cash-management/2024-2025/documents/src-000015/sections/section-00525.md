---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.2 Structure"]
file_pages: [687]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 687 to 687.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 687

```text
30.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <GetStgOrdr> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 689
   StandingOrderQueryDefinition <StgOrdrQryDef> [0..1]  689
     QueryType <QryTp> [0..1] CodeSet 691
     StandingOrderCriteria <StgOrdrCrit> [0..1]  691
{Or       QueryName <QryNm> [1..1] Text 693
Or}       NewCriteria <NewCrit> [1..1]  C8 693
         NewQueryName <NewQryNm> [0..1] Text 695
         SearchCriteria <SchCrit> [0..*]  695
           KeyAttributesIndicator <KeyAttrbtsInd> [0..1] Indicator 696
           StandingOrderIdentification <StgOrdrId> [0..1] Text 696
           Type <Tp> [0..1]  697
{Or             Code <Cd> [1..1] CodeSet 697
Or}             Proprietary <Prtry> [1..1] ± 697
           Account <Acct> [0..1] ± C7, C6 697
           Currency <Ccy> [0..1] CodeSet C1 698
           ValidityPeriod <VldtyPrd> [0..1]  698
{Or             FromDate <FrDt> [1..1] Date 699
Or             ToDate <ToDt> [1..1] Date 699
Or}             FromToDate <FrToDt> [1..1] ± 699
           SystemMember <SysMmb> [0..1] ± 699
           ResponsibleParty <RspnsblPty> [0..1] ± 700
           AssociatedPoolAccount <AssoctdPoolAcct> [0..1] ± 701
           LinkSetIdentification <LkSetId> [0..1] Text 701
           LinkSetOrderIdentification <LkSetOrdrId> [0..1] Text 701
           LinkSetOrderSequence <LkSetOrdrSeq> [0..1] Quantity 701
           ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 701
         ReturnCriteria <RtrCrit> [0..1]  701
           StandingOrderIdentificationIndicator <StgOrdrIdInd> [0..1] Indicator 702
           TypeIndicator <TpInd> [0..1] Indicator 702
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 687 February 2025
```

