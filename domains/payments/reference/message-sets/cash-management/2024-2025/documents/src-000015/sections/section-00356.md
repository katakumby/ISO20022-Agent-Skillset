---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04", "14.4 Message Building Blocks", "14.4.3 NewMemberValueSet <NewMmbValSet>", "14.4.3.1 MemberReturnAddress <MmbRtrAdr>"]
file_pages: [500]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14.4.3.1 MemberReturnAddress <MmbRtrAdr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 500 to 500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 500

```text
14.4.3.1  MemberReturnAddress <MmbRtrAdr>
Presence: [0..*]
Definition: Physical/logical address belonging to a member, segregated from its main address that is
used for normal operations. The fund return address is used to route messages that require specific
attention/exception handling, for example, returns or rejects.
MemberReturnAddress <MmbRtrAdr> contains one of the following MemberIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C1 500
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 500
Or}   Other <Othr> [1..1] ± 500
14.4.3.1.1  BICFI <BICFI>
Presence: [1..1]
Definition: Business identification code of the member financial institution.
Impacted by: C1 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 884
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
14.4.3.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 802
   MemberIdentification <MmbId> [1..1] Text 802
14.4.3.1.3  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 500 February 2025
```

