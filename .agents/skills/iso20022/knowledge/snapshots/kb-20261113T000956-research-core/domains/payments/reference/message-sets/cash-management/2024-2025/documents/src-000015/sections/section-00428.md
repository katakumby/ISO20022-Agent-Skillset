---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07", "21.4 Message Building Blocks", "21.4.5 Creditor <Cdtr>"]
file_pages: [584]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21.4.5 Creditor <Cdtr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 584 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 584

```text
21.4.5 Creditor <Cdtr>
Presence: [1..1]
Definition: Party that receives an amount of money from the debtor.
Creditor <Cdtr> contains the following SystemMember3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 584
   MemberIdentification <MmbId> [1..1]  584
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 584
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 585
Or}     Other <Othr> [1..1] ± 585
21.4.5.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
21.4.5.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
MemberIdentification <MmbId> contains one of the following MemberIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 584
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 585
Or}   Other <Othr> [1..1] ± 585
21.4.5.2.1  BICFI <BICFI>
Presence: [1..1]
Definition: Business identification code of the member financial institution.
Impacted by: C2 "BICFI"
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 584 February 2025
```

