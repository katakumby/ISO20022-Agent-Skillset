---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks"]
file_pages: [480, 481]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C8"], "until_heading": "13.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 480, "topic": "13.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00338.md"}]
---

# 13.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 480 to 481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 480, C8 before **13.4 Message Building Blocks** continue [13.3 Constraints](section-00338.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 480

```text
C8 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
13.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
13.4.1 MessageHeader <MsgHdr>
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
13.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Reports on members.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 480 February 2025
```

## File page 481

```text
ReportOrError <RptOrErr> contains one of the following MemberReportOrError7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Report <Rpt> [1..*]  482
     MemberIdentification <MmbId> [1..1]  484
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 484
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 484
Or}       Other <Othr> [1..1] ± 485
     MemberOrError <MmbOrErr> [1..1]  485
{Or       Member <Mmb> [1..1]  487
         Name <Nm> [0..1] Text 488
         ReturnAddress <RtrAdr> [0..*]  488
{Or           BICFI <BICFI> [1..1] IdentifierSet C2 488
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 488
Or}           Other <Othr> [1..1] ± 488
         Account <Acct> [0..*] ± C6, C5 489
         Type <Tp> [0..1]  489
{Or           Code <Cd> [1..1] CodeSet 490
Or}           Proprietary <Prtry> [1..1] Text 490
         Status <Sts> [0..1]  490
{Or           Code <Cd> [1..1] CodeSet 490
Or}           Proprietary <Prtry> [1..1] Text 490
         ContactReference <CtctRef> [0..*]  491
           Name <Nm> [0..1] Text 491
           Role <Role> [1..1]  491
{Or             Code <Cd> [1..1] CodeSet 491
Or}             Proprietary <Prtry> [1..1] Text 491
           CommunicationAddress <ComAdr> [1..1]  492
             PostalAddress <PstlAdr> [1..1] ± 492
             PhoneNumber <PhneNb> [1..1] Text 492
             FaxNumber <FaxNb> [0..1] Text 492
             EmailAddress <EmailAdr> [0..1] Text 492
         CommunicationAddress <ComAdr> [0..1]  492
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 481 February 2025
```

