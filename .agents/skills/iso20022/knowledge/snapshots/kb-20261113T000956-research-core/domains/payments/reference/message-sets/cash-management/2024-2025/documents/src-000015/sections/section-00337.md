---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.2 Structure"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
13.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RtrMmb> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 480
   ReportOrError <RptOrErr> [1..1]  480
{Or     Report <Rpt> [1..*]  482
       MemberIdentification <MmbId> [1..1]  484
{Or         BICFI <BICFI> [1..1] IdentifierSet C2 484
Or         ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 484
Or}         Other <Othr> [1..1] ± 485
       MemberOrError <MmbOrErr> [1..1]  485
{Or         Member <Mmb> [1..1]  487
           Name <Nm> [0..1] Text 488
           ReturnAddress <RtrAdr> [0..*]  488
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 488
Or             ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 488
Or}             Other <Othr> [1..1] ± 488
           Account <Acct> [0..*] ± C6, C5 489
           Type <Tp> [0..1]  489
{Or             Code <Cd> [1..1] CodeSet 490
Or}             Proprietary <Prtry> [1..1] Text 490
           Status <Sts> [0..1]  490
{Or             Code <Cd> [1..1] CodeSet 490
Or}             Proprietary <Prtry> [1..1] Text 490
           ContactReference <CtctRef> [0..*]  491
             Name <Nm> [0..1] Text 491
             Role <Role> [1..1]  491
{Or               Code <Cd> [1..1] CodeSet 491
Or}               Proprietary <Prtry> [1..1] Text 491
             CommunicationAddress <ComAdr> [1..1]  492
               PostalAddress <PstlAdr> [1..1] ± 492
               PhoneNumber <PhneNb> [1..1] Text 492
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 478 February 2025
```

