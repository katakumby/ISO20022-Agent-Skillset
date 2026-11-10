---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>"]
file_pages: [482, 483]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1 Report <Rpt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 482 to 483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 482

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PostalAddress <PstlAdr> [1..1] ± 493
           PhoneNumber <PhneNb> [1..1] Text 493
           FaxNumber <FaxNb> [0..1] Text 493
           EmailAddress <EmailAdr> [0..1] Text 493
Or}       BusinessError <BizErr> [1..1] ± 493
Or}   OperationalError <OprlErr> [1..*] ± 494
13.4.2.1  Report <Rpt>
Presence: [1..*]
Definition: Provides the details on the requested member.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 482 February 2025
```

## File page 483

```text
Report <Rpt> contains the following MemberReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MemberIdentification <MmbId> [1..1]  484
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 484
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 484
Or}     Other <Othr> [1..1] ± 485
   MemberOrError <MmbOrErr> [1..1]  485
{Or     Member <Mmb> [1..1]  487
       Name <Nm> [0..1] Text 488
       ReturnAddress <RtrAdr> [0..*]  488
{Or         BICFI <BICFI> [1..1] IdentifierSet C2 488
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 488
Or}         Other <Othr> [1..1] ± 488
       Account <Acct> [0..*] ± C6, C5 489
       Type <Tp> [0..1]  489
{Or         Code <Cd> [1..1] CodeSet 490
Or}         Proprietary <Prtry> [1..1] Text 490
       Status <Sts> [0..1]  490
{Or         Code <Cd> [1..1] CodeSet 490
Or}         Proprietary <Prtry> [1..1] Text 490
       ContactReference <CtctRef> [0..*]  491
         Name <Nm> [0..1] Text 491
         Role <Role> [1..1]  491
{Or           Code <Cd> [1..1] CodeSet 491
Or}           Proprietary <Prtry> [1..1] Text 491
         CommunicationAddress <ComAdr> [1..1]  492
           PostalAddress <PstlAdr> [1..1] ± 492
           PhoneNumber <PhneNb> [1..1] Text 492
           FaxNumber <FaxNb> [0..1] Text 492
           EmailAddress <EmailAdr> [0..1] Text 492
       CommunicationAddress <ComAdr> [0..1]  492
         PostalAddress <PstlAdr> [1..1] ± 493
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 483 February 2025
```

