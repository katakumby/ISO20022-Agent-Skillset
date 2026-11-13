---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.1 MemberIdentification <MmbId>", "13.4.2.1.1.3 Other <Othr>"]
file_pages: [485, 486]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.1.3 Other <Othr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 485 to 486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 485

```text
13.4.2.1.1.3  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 802 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 803
   SchemeName <SchmeNm> [0..1]  803
{Or     Code <Cd> [1..1] CodeSet 803
Or}     Proprietary <Prtry> [1..1] Text 803
   Issuer <Issr> [0..1] Text 803
13.4.2.1.2  MemberOrError <MmbOrErr>
Presence: [1..1]
Definition: Reports either on a member or a business error.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 485 February 2025
```

## File page 486

```text
MemberOrError <MmbOrErr> contains one of the following MemberReportOrError8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Member <Mmb> [1..1]  487
     Name <Nm> [0..1] Text 488
     ReturnAddress <RtrAdr> [0..*]  488
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 488
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 488
Or}       Other <Othr> [1..1] ± 488
     Account <Acct> [0..*] ± C6, C5 489
     Type <Tp> [0..1]  489
{Or       Code <Cd> [1..1] CodeSet 490
Or}       Proprietary <Prtry> [1..1] Text 490
     Status <Sts> [0..1]  490
{Or       Code <Cd> [1..1] CodeSet 490
Or}       Proprietary <Prtry> [1..1] Text 490
     ContactReference <CtctRef> [0..*]  491
       Name <Nm> [0..1] Text 491
       Role <Role> [1..1]  491
{Or         Code <Cd> [1..1] CodeSet 491
Or}         Proprietary <Prtry> [1..1] Text 491
       CommunicationAddress <ComAdr> [1..1]  492
         PostalAddress <PstlAdr> [1..1] ± 492
         PhoneNumber <PhneNb> [1..1] Text 492
         FaxNumber <FaxNb> [0..1] Text 492
         EmailAddress <EmailAdr> [0..1] Text 492
     CommunicationAddress <ComAdr> [0..1]  492
       PostalAddress <PstlAdr> [1..1] ± 493
       PhoneNumber <PhneNb> [1..1] Text 493
       FaxNumber <FaxNb> [0..1] Text 493
       EmailAddress <EmailAdr> [0..1] Text 493
Or}   BusinessError <BizErr> [1..1] ± 493
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 486 February 2025
```

