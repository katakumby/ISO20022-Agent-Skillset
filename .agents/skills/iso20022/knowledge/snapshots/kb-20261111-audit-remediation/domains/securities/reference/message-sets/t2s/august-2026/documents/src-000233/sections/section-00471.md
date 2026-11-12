---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks"]
file_pages: [594, 595]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 594 to 595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 594

```text
25.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
25.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Set of elements to identify the collateral value report message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader3" on page 2995 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2995
   CreationDateTime <CreDtTm> [0..1] DateTime 2995
   RequestType <ReqTp> [0..1]  2995
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 2995
Or     Enquiry <Enqry> [1..1] CodeSet 2996
Or}     Proprietary <Prtry> [1..1] ± 2996
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 2996
   QueryName <QryNm> [0..1] Text 2997
25.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Report on collateral value information or operational error.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 594 August 2026
```

## File page 595

```text
ReportOrError <RptOrErr> contains one of the following CollateralValueReportOrError7Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessReport <BizRpt> [1..*]  596
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
{Or       BusinessError <BizErr> [1..1]  603
         Error <Err> [1..1]  603
{Or           Code <Cd> [1..1] CodeSet 603
Or}           Proprietary <Prtry> [1..1] Text 603
         Description <Desc> [0..1] Text 603
Or}       CollateralValue <CollVal> [1..1]  603
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
{Or               Quantity <Qty> [1..1] ± 609
Or               Proprietary <Prtry> [1..1]  609
                 Identification <Id> [1..1] Text 609
                 Issuer <Issr> [1..1] Text 609
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 595 August 2026
```

