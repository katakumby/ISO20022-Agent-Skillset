---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["12 camt.013.001.04 GetMemberV04", "12.4 Message Building Blocks", "12.4.2 MemberQueryDefinition <MmbQryDef>", "12.4.2.2 MemberCriteria <MmbCrit>", "12.4.2.2.2 NewCriteria <NewCrit>", "12.4.2.2.2.2 SearchCriteria <SchCrit>", "12.4.2.2.2.2.1 Identification <Id>", "12.4.2.2.2.2.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>"]
file_pages: [472]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.013.001.04"]
---

# 12.4.2.2.2.2.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 472 to 472.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 472

```text
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
12.4.2.2.2.2.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 802
   MemberIdentification <MmbId> [1..1] Text 802
12.4.2.2.2.2.1.3  Other <Othr>
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
12.4.2.2.2.2.2  Type <Tp>
Presence: [0..*]
Definition: Nature of the relationship a member has with a system.
Type <Tp> contains one of the following SystemMemberType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 472
Or}   Proprietary <Prtry> [1..1] Text 473
12.4.2.2.2.2.2.1  Code <Cd>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 472 February 2025
```

