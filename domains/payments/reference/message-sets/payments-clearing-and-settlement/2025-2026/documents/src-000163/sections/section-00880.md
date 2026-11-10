---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.7 Financial Institution Identification", "10.1.7.3 BranchAndFinancialInstitutionIdentification8", "10.1.7.3.1 FinancialInstitutionIdentification <FinInstnId>", "10.1.7.3.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>"]
file_pages: [1175]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.7.3.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1175 to 1175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1175

```text
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
10.1.7.3.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 1172 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 1172
   MemberIdentification <MmbId> [1..1] Text 1172
10.1.7.3.1.3  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identifier of the financial institution.
Datatype: "LEIIdentifier" on page 1241
10.1.7.3.1.4  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 1244
10.1.7.3.1.5  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1175 March 2026
```

