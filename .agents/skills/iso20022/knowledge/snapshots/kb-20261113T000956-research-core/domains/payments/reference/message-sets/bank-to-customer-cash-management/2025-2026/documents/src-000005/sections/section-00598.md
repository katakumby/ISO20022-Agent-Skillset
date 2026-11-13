---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Financial Institution Identification", "6.1.12.3 BranchAndFinancialInstitutionIdentification8", "6.1.12.3.1 FinancialInstitutionIdentification <FinInstnId>", "6.1.12.3.1.1 BICFI <BICFI>"]
file_pages: [831]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.3.1.1 BICFI <BICFI>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 831 to 831.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 831

```text
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C3 831
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 831
   LEI <LEI> [0..1] IdentifierSet 831
   Name <Nm> [0..1] Text 831
   PostalAddress <PstlAdr> [0..1] ± 832
   Other <Othr> [0..1] ± 832
6.1.12.3.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C3 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 909
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
6.1.12.3.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 828 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 828
   MemberIdentification <MmbId> [1..1] Text 829
6.1.12.3.1.3  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identifier of the financial institution.
Datatype: "LEIIdentifier" on page 910
6.1.12.3.1.4  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
831 March 2026
```

