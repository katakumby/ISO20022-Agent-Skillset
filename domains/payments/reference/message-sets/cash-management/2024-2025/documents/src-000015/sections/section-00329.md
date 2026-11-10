---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.4 Message Building Blocks", "12.4.2 MemberQueryDefinition <MmbQryDef>", "12.4.2.2 MemberCriteria <MmbCrit>", "12.4.2.2.1 QueryName <QryNm>"]
file_pages: [469]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.4.2.2.1 QueryName <QryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 469 to 469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 469

```text
MemberCriteria <MmbCrit> contains one of the following MemberCriteriaDefinition2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 469
Or}   NewCriteria <NewCrit> [1..1]  C2 469
     NewQueryName <NewQryNm> [0..1] Text 470
     SearchCriteria <SchCrit> [0..*]  470
       Identification <Id> [0..*]  471
{Or         BICFI <BICFI> [1..1] IdentifierSet C1 471
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 472
Or}         Other <Othr> [1..1] ± 472
       Type <Tp> [0..*]  472
{Or         Code <Cd> [1..1] CodeSet 472
Or}         Proprietary <Prtry> [1..1] Text 473
       Status <Sts> [0..*]  473
{Or         Code <Cd> [1..1] CodeSet 473
Or}         Proprietary <Prtry> [1..1] Text 473
     ReturnCriteria <RtrCrit> [0..1]  473
       NameIndicator <NmInd> [0..1] Indicator 474
       MemberReturnAddressIndicator <MmbRtrAdrInd> [0..1] Indicator 474
       AccountIndicator <AcctInd> [0..1] Indicator 474
       TypeIndicator <TpInd> [0..1] Indicator 474
       StatusIndicator <StsInd> [0..1] Indicator 475
       ContactReferenceIndicator <CtctRefInd> [0..1] Indicator 475
       CommunicationAddressIndicator <ComAdrInd> [0..1] Indicator 475
12.4.2.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
12.4.2.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Defines the criteria based on which the information is extracted.
Impacted by: C2 "ReturnCriteriaAndOrSearchCriteriaRule"
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 469 February 2025
```

