---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01", "36.2 Structure"]
file_pages: [774]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 774 to 774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 774

```text
36.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CretMmb> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 775
   MemberIdentification <MmbId> [1..1]  775
{Or     BICFI <BICFI> [1..1] IdentifierSet C1 775
Or     ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 776
Or}     Other <Othr> [1..1] ± 776
   ValueSet <ValSet> [1..1]  776
     MemberReturnAddress <MmbRtrAdr> [0..*]  777
{Or       BICFI <BICFI> [1..1] IdentifierSet C1 777
Or       ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 778
Or}       Other <Othr> [1..1] ± 778
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
   SupplementaryData <SplmtryData> [0..*] ± C4 781
36.3 Constraints
C1 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 774 February 2025
```

