---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01", "36.4 Message Building Blocks", "36.4.3 ValueSet <ValSet>", "36.4.3.1 MemberReturnAddress <MmbRtrAdr>"]
file_pages: [777]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36.4.3.1 MemberReturnAddress <MmbRtrAdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 777 to 777.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 777

```text
ValueSet <ValSet> contains the following Member6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MemberReturnAddress <MmbRtrAdr> [0..*]  777
{Or     BICFI <BICFI> [1..1] IdentifierSet C1 777
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 778
Or}     Other <Othr> [1..1] ± 778
   ContactReference <CtctRef> [0..*]  778
     Name <Nm> [0..1] Text 779
     Role <Role> [1..1] CodeSet 779
     CommunicationAddress <ComAdr> [1..1]  780
       PostalAddress <PstlAdr> [1..1] ± 780
       PhoneNumber <PhneNb> [1..1] Text 780
       FaxNumber <FaxNb> [0..1] Text 780
       EmailAddress <EmailAdr> [0..1] Text 780
   CommunicationAddress <ComAdr> [0..1]  781
     PostalAddress <PstlAdr> [1..1] ± 781
     PhoneNumber <PhneNb> [1..1] Text 781
     FaxNumber <FaxNb> [0..1] Text 781
     EmailAddress <EmailAdr> [0..1] Text 781
36.4.3.1  MemberReturnAddress <MmbRtrAdr>
Presence: [0..*]
Definition: Physical/logical address belonging to a member, segregated from its main address that is
used for normal operations. The fund return address is used to route messages that require specific
attention/exception handling, for example, returns or rejects.
MemberReturnAddress <MmbRtrAdr> contains one of the following MemberIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C1 777
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 778
Or}   Other <Othr> [1..1] ± 778
36.4.3.1.1  BICFI <BICFI>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 777 February 2025
```

