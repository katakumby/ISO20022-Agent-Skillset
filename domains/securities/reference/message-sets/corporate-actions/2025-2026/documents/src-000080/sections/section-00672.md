---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.1 FinancialInstitutionIdentification18", "16.1.8.1.1 BICFI <BICFI>"]
file_pages: [863]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.1.1 BICFI <BICFI>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 863 to 863.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 863

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C2 863
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 863
   LEI <LEI> [0..1] IdentifierSet 863
   Name <Nm> [0..1] Text 863
   PostalAddress <PstlAdr> [0..1] ± 864
   Other <Othr> [0..1] ± 864
16.1.8.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 1244
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
16.1.8.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 868 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 868
   MemberIdentification <MmbId> [1..1] Text 869
16.1.8.1.3  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identifier of the financial institution.
Datatype: "LEIIdentifier" on page 1246
16.1.8.1.4  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 1249
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 863 February 2026
```

