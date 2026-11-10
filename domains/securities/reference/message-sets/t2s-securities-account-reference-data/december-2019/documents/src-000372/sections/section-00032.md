---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["5 reda.021.001.01 SecuritiesAccountReportV01", "5.4 Message Building Blocks", "5.4.2 Pagination <Pgntn>"]
file_pages: [35, 36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 5.4.2 Pagination <Pgntn>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 35 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader3" on page 85 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 85
   CreationDateTime <CreDtTm> [0..1] DateTime 85
   RequestType <ReqTp> [0..1]  85
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 86
Or     Enquiry <Enqry> [1..1] CodeSet 86
Or}     Proprietary <Prtry> [1..1] ± 86
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 87
   QueryName <QryNm> [0..1] Text 87
5.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Provides details on the page number of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 83 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 84
   LastPageIndicator <LastPgInd> [1..1] Indicator 84
5.4.3 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities - Securities Account Reference Data 35 December 2019
```

## File page 36

```text
ReportOrError <RptOrErr> contains one of the following
SecuritiesAccountOrOperationalError3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccountReport <SctiesAcctRpt> [1..*]  37
     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 38
     SecuritiesAccountOrError <SctiesAcctOrErr> [1..1]  39
{Or       SecuritiesAccount <SctiesAcct> [1..1]  40
         OpeningDate <OpngDt> [0..1] Date 41
         ClosingDate <ClsgDt> [0..1] Date 41
         HoldIndicator <HldInd> [0..1] Indicator 41
         NegativePosition <NegPos> [0..1] Indicator 42
         Type <Tp> [0..1]  42
{Or           Code <Cd> [1..1] CodeSet 42
Or}           Proprietary <Prtry> [1..1] ± 43
         AccountOwner <AcctOwnr> [1..1] ± 43
         PartyType <PtyTp> [0..1]  43
{Or           Code <Cd> [1..1] CodeSet 43
Or}           Proprietary <Prtry> [1..1] Text 44
         MarketSpecificAttribute <MktSpcfcAttr> [0..*]  44
           Name <Nm> [1..1] Text 44
           Value <Val> [1..1] Text 44
         Restriction <Rstrctn> [0..*]  44
           ValidFrom <VldFr> [1..1] DateTime 44
           ValidTo <VldTo> [0..1] DateTime 45
           Type <Tp> [1..1] Text 45
         EndInvestorFlag <EndInvstrFlg> [0..1] Text 45
         PricingScheme <PricgSchme> [0..1] Text 45
Or}       BusinessError <BizErr> [1..*]  45
         Error <Err> [1..1]  45
{Or           Code <Cd> [1..1] CodeSet 46
Or}           Proprietary <Prtry> [1..1] Text 46
         Description <Desc> [0..1] Text 46
Or}   OperationalError <OprlErr> [1..*]  46
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities - Securities Account Reference Data 36 December 2019
```

