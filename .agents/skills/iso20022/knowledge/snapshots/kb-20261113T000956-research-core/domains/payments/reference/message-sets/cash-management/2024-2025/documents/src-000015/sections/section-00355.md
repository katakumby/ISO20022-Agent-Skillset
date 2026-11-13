---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04", "14.4 Message Building Blocks", "14.4.3 NewMemberValueSet <NewMmbValSet>"]
file_pages: [499]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14.4.3 NewMemberValueSet <NewMmbValSet>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 499 to 499.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 499

```text
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
14.4.3 NewMemberValueSet <NewMmbValSet>
Presence: [1..1]
Definition: New member values.
NewMemberValueSet <NewMmbValSet> contains the following Member6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MemberReturnAddress <MmbRtrAdr> [0..*]  500
{Or     BICFI <BICFI> [1..1] IdentifierSet C1 500
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 500
Or}     Other <Othr> [1..1] ± 500
   ContactReference <CtctRef> [0..*]  501
     Name <Nm> [0..1] Text 501
     Role <Role> [1..1] CodeSet 501
     CommunicationAddress <ComAdr> [1..1]  502
       PostalAddress <PstlAdr> [1..1] ± 502
       PhoneNumber <PhneNb> [1..1] Text 503
       FaxNumber <FaxNb> [0..1] Text 503
       EmailAddress <EmailAdr> [0..1] Text 503
   CommunicationAddress <ComAdr> [0..1]  503
     PostalAddress <PstlAdr> [1..1] ± 503
     PhoneNumber <PhneNb> [1..1] Text 503
     FaxNumber <FaxNb> [0..1] Text 504
     EmailAddress <EmailAdr> [0..1] Text 504
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 499 February 2025
```

