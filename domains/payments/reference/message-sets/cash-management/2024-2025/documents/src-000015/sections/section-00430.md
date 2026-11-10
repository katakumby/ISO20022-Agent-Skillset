---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07", "21.4 Message Building Blocks", "21.4.6 CreditorAgent <CdtrAgt>", "21.4.6.1 SystemIdentification <SysId>"]
file_pages: [586]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21.4.6.1 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 586 to 586.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 586

```text
CreditorAgent <CdtrAgt> contains the following SystemMember3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 586
   MemberIdentification <MmbId> [1..1]  586
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 586
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 587
Or}     Other <Othr> [1..1] ± 587
21.4.6.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
21.4.6.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
MemberIdentification <MmbId> contains one of the following MemberIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 586
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 587
Or}   Other <Othr> [1..1] ± 587
21.4.6.2.1  BICFI <BICFI>
Presence: [1..1]
Definition: Business identification code of the member financial institution.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 884
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 586 February 2025
```

