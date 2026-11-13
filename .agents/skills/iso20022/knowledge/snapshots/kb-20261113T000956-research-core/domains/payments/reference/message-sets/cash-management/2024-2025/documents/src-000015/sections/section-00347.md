---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.2 MemberOrError <MmbOrErr>", "13.4.2.1.2.1 Member <Mmb>", "13.4.2.1.2.1.6 ContactReference <CtctRef>"]
file_pages: [491]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.2.1.6 ContactReference <CtctRef>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 491 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 491

```text
13.4.2.1.2.1.6  ContactReference <CtctRef>
Presence: [0..*]
Definition: Person to be contacted in a given organisation.
ContactReference <CtctRef> contains the following ContactIdentificationAndAddress2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 491
   Role <Role> [1..1]  491
{Or     Code <Cd> [1..1] CodeSet 491
Or}     Proprietary <Prtry> [1..1] Text 491
   CommunicationAddress <ComAdr> [1..1]  492
     PostalAddress <PstlAdr> [1..1] ± 492
     PhoneNumber <PhneNb> [1..1] Text 492
     FaxNumber <FaxNb> [0..1] Text 492
     EmailAddress <EmailAdr> [0..1] Text 492
13.4.2.1.2.1.6.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 889
13.4.2.1.2.1.6.2  Role <Role>
Presence: [1..1]
Definition: Role of the party in the payment.
Role <Role> contains one of the following PaymentRole1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 491
Or}   Proprietary <Prtry> [1..1] Text 491
13.4.2.1.2.1.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Payment party role, in a coded form.
Datatype: "ExternalPaymentRole1Code" on page 855
13.4.2.1.2.1.6.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Payment party role, in a proprietary form.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 491 February 2025
```

