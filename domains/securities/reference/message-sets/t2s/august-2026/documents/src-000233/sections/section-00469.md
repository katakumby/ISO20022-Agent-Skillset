---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.2 Structure"]
file_pages: [591]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 591 to 591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 591

```text
25.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CollValRpt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 594
   ReportOrError <RptOrErr> [1..1]  594
{Or     BusinessReport <BizRpt> [1..*]  596
       CashAccount <CshAcct> [1..1] ± C11,
C10
598
       CashAccountOwner <CshAcctOwnr> [0..1]  599
         Name <Nm> [0..1] Text 599
         Identification <Id> [1..1] ± 599
         ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 599
       CashAccountServicer <CshAcctSvcr> [0..1] ± 599
       SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 600
       SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 600
       CollateralValueReport <CollValRpt> [0..*]  601
{Or         BusinessError <BizErr> [1..1]  603
           Error <Err> [1..1]  603
{Or             Code <Cd> [1..1] CodeSet 603
Or}             Proprietary <Prtry> [1..1] Text 603
           Description <Desc> [0..1] Text 603
Or}         CollateralValue <CollVal> [1..1]  603
           DataAccessTime <DataAccsTm> [1..1] DateTime 604
           TotalCollateralValuation <TtlCollValtn> [0..1] Amount C1, C6 604
           SecuritiesAccount <SctiesAcct> [0..1] ± 605
           Securities <Scties> [0..*]  605
             Identification <Id> [0..*] ± C7, C8,
C12,
C13,
C14
606
             Position <Pos> [0..*]  607
               Type <Tp> [1..1] Text 608
               Quantity <Qty> [1..1]  608
{Or                 Quantity <Qty> [1..1] ± 609
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 591 August 2026
```

