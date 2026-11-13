---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.4 Message Building Blocks", "12.4.2 MemberQueryDefinition <MmbQryDef>", "12.4.2.2 MemberCriteria <MmbCrit>", "12.4.2.2.2 NewCriteria <NewCrit>", "12.4.2.2.2.2 SearchCriteria <SchCrit>", "12.4.2.2.2.2.1 Identification <Id>"]
file_pages: [471]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.4.2.2.2.2.1 Identification <Id>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 471 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 471

```text
Definition: Defines the criteria based on which the information is extracted.
SearchCriteria <SchCrit> contains the following MemberSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..*]  471
{Or     BICFI <BICFI> [1..1] IdentifierSet C1 471
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 472
Or}     Other <Othr> [1..1] ± 472
   Type <Tp> [0..*]  472
{Or     Code <Cd> [1..1] CodeSet 472
Or}     Proprietary <Prtry> [1..1] Text 473
   Status <Sts> [0..*]  473
{Or     Code <Cd> [1..1] CodeSet 473
Or}     Proprietary <Prtry> [1..1] Text 473
12.4.2.2.2.2.1  Identification <Id>
Presence: [0..*]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
Identification <Id> contains one of the following MemberIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C1 471
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 472
Or}   Other <Othr> [1..1] ± 472
12.4.2.2.2.2.1.1  BICFI <BICFI>
Presence: [1..1]
Definition: Business identification code of the member financial institution.
Impacted by: C1 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 884
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 471 February 2025
```

