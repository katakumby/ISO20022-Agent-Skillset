---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07", "21.4 Message Building Blocks", "21.4.6 CreditorAgent <CdtrAgt>", "21.4.6.2 MemberIdentification <MmbId>", "21.4.6.2.2 ClearingSystemMemberIdentification <ClrSysMmbId>"]
file_pages: [587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21.4.6.2.2 ClearingSystemMemberIdentification <ClrSysMmbId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 587 to 587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 587

```text
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
21.4.6.2.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 802
   MemberIdentification <MmbId> [1..1] Text 802
21.4.6.2.3  Other <Othr>
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
21.4.7 DebtorAgent <DbtrAgt>
Presence: [0..1]
Definition: Financial institution that receives the payment transaction from the account owner, or other
authorised party, and processes the instruction.
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 587 February 2025
```

