---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.4 BranchAndFinancialInstitutionIdentification6", "16.1.8.4.2 BranchIdentification <BrnchId>"]
file_pages: [868]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.4.2 BranchIdentification <BrnchId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 868 to 868.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 868

```text
FinancialInstitutionIdentification <FinInstnId> contains the following elements (see
"FinancialInstitutionIdentification18" on page 862 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C2 863
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 863
   LEI <LEI> [0..1] IdentifierSet 863
   Name <Nm> [0..1] Text 863
   PostalAddress <PstlAdr> [0..1] ± 864
   Other <Othr> [0..1] ± 864
16.1.8.4.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following elements (see "BranchData3" on page 865 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 865
   LEI <LEI> [0..1] IdentifierSet 865
   Name <Nm> [0..1] Text 865
   PostalAddress <PstlAdr> [0..1] ± 865
16.1.8.5  ClearingSystemMemberIdentification2
Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member
of the clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 868
   MemberIdentification <MmbId> [1..1] Text 869
16.1.8.5.1  ClearingSystemIdentification <ClrSysId>
Presence: [0..1]
Definition: Specification of a pre-agreed offering between clearing agents or the channel through which
the payment instruction is processed.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 868 February 2026
```

