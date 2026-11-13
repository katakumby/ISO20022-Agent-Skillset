---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.2 Structure"]
file_pages: [465]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 465 to 465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 465

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <GetMmb> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 466
   MemberQueryDefinition <MmbQryDef> [0..1]  466
     QueryType <QryTp> [0..1] CodeSet 467
     MemberCriteria <MmbCrit> [0..1]  468
{Or       QueryName <QryNm> [1..1] Text 469
Or}       NewCriteria <NewCrit> [1..1]  C2 469
         NewQueryName <NewQryNm> [0..1] Text 470
         SearchCriteria <SchCrit> [0..*]  470
           Identification <Id> [0..*]  471
{Or             BICFI <BICFI> [1..1] IdentifierSet C1 471
Or             ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 472
Or}             Other <Othr> [1..1] ± 472
           Type <Tp> [0..*]  472
{Or             Code <Cd> [1..1] CodeSet 472
Or}             Proprietary <Prtry> [1..1] Text 473
           Status <Sts> [0..*]  473
{Or             Code <Cd> [1..1] CodeSet 473
Or}             Proprietary <Prtry> [1..1] Text 473
         ReturnCriteria <RtrCrit> [0..1]  473
           NameIndicator <NmInd> [0..1] Indicator 474
           MemberReturnAddressIndicator <MmbRtrAdrInd> [0..1] Indicator 474
           AccountIndicator <AcctInd> [0..1] Indicator 474
           TypeIndicator <TpInd> [0..1] Indicator 474
           StatusIndicator <StsInd> [0..1] Indicator 475
           ContactReferenceIndicator <CtctRefInd> [0..1] Indicator 475
           CommunicationAddressIndicator <ComAdrInd> [0..1] Indicator 475
   SupplementaryData <SplmtryData> [0..*] ± C3 475
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 465 February 2025
```

