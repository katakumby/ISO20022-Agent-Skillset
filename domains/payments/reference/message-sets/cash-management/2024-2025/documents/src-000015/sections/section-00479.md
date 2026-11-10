---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08", "25.4 Message Building Blocks"]
file_pages: [639, 640]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 639 to 640.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 639

```text
25.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
25.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader7" on page 814 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 814
   CreationDateTime <CreDtTm> [0..1] DateTime 814
   RequestType <ReqTp> [0..1]  814
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 814
Or     Enquiry <Enqry> [1..1] CodeSet 815
Or}     Proprietary <Prtry> [1..1] ± 815
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 815
   QueryName <QryNm> [0..1] Text 815
25.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Reports on reservations.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 639 February 2025
```

## File page 640

```text
ReportOrError <RptOrErr> contains one of the following ReservationOrError11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessReport <BizRpt> [1..1]  641
     CurrentReservation <CurRsvatn> [0..*]  643
       ReservationIdentification <RsvatnId> [1..1]  643
         ReservationIdentification <RsvatnId> [0..1] Text 644
         SystemIdentification <SysId> [0..1] ± 644
         Type <Tp> [1..1]  644
{Or           Code <Cd> [1..1] CodeSet 644
Or}           Proprietary <Prtry> [1..1] Text 645
         AccountOwner <AcctOwnr> [0..1] ± 645
         AccountIdentification <AcctId> [0..1] ± 645
       ReservationOrError <RsvatnOrErr> [1..1]  645
{Or         Reservation <Rsvatn> [1..1] ± 646
Or}         BusinessError <BizErr> [1..*]  646
           Error <Err> [1..1]  646
{Or             Code <Cd> [1..1] CodeSet 647
Or}             Proprietary <Prtry> [1..1] Text 647
           Description <Desc> [0..1] Text 647
     DefaultReservation <DfltRsvatn> [0..*]  647
       ReservationIdentification <RsvatnId> [1..1]  648
         ReservationIdentification <RsvatnId> [0..1] Text 648
         SystemIdentification <SysId> [0..1] ± 649
         Type <Tp> [1..1]  649
{Or           Code <Cd> [1..1] CodeSet 649
Or}           Proprietary <Prtry> [1..1] Text 649
         AccountOwner <AcctOwnr> [0..1] ± 649
         AccountIdentification <AcctId> [0..1] ± 650
       ReservationOrError <RsvatnOrErr> [1..1]  650
{Or         Reservation <Rsvatn> [1..1] ± 651
Or}         BusinessError <BizErr> [1..*]  651
           Error <Err> [1..1]  651
{Or             Code <Cd> [1..1] CodeSet 652
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 640 February 2025
```

