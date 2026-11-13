---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.9 Financial Institution Identification", "37.1.9.3 BranchAndFinancialInstitutionIdentification8", "37.1.9.3.1 FinancialInstitutionIdentification <FinInstnId>", "37.1.9.3.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>"]
file_pages: [805]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.9.3.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 805 to 805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 805

```text
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
37.1.9.3.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 802
   MemberIdentification <MmbId> [1..1] Text 802
37.1.9.3.1.3  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identifier of the financial institution.
Datatype: "LEIIdentifier" on page 885
37.1.9.3.1.4  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 888
37.1.9.3.1.5  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 805 February 2025
```

