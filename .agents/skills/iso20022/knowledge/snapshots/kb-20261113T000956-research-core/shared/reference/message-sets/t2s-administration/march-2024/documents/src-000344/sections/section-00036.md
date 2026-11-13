---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.5 Financial Institution Identification", "5.1.5.2 BranchAndFinancialInstitutionIdentification8", "5.1.5.2.1 FinancialInstitutionIdentification <FinInstnId>", "5.1.5.2.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.5.2.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
5.1.5.2.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 41 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 41
   MemberIdentification <MmbId> [1..1] Text 41
5.1.5.2.1.3  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identifier of the financial institution.
Datatype: "LEIIdentifier" on page 67
5.1.5.2.1.4  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 68
5.1.5.2.1.5  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
43 March 2024
```

