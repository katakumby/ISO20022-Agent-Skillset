---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.2 MemberOrError <MmbOrErr>", "13.4.2.1.2.1 Member <Mmb>"]
file_pages: [487]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.2.1 Member <Mmb>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 487 to 487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 487

```text
13.4.2.1.2.1  Member <Mmb>
Presence: [1..1]
Definition: Requested member data when found in the system.
Member <Mmb> contains the following Member7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 488
   ReturnAddress <RtrAdr> [0..*]  488
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 488
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 488
Or}     Other <Othr> [1..1] ± 488
   Account <Acct> [0..*] ± C6, C5 489
   Type <Tp> [0..1]  489
{Or     Code <Cd> [1..1] CodeSet 490
Or}     Proprietary <Prtry> [1..1] Text 490
   Status <Sts> [0..1]  490
{Or     Code <Cd> [1..1] CodeSet 490
Or}     Proprietary <Prtry> [1..1] Text 490
   ContactReference <CtctRef> [0..*]  491
     Name <Nm> [0..1] Text 491
     Role <Role> [1..1]  491
{Or       Code <Cd> [1..1] CodeSet 491
Or}       Proprietary <Prtry> [1..1] Text 491
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
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 487 February 2025
```

