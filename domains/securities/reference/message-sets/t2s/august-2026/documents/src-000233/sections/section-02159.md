---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.12 Financial Institution Identification", "82.1.12.3 BranchAndFinancialInstitutionIdentification8", "82.1.12.3.1 FinancialInstitutionIdentification <FinInstnId>"]
file_pages: [2920]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.12.3.1 FinancialInstitutionIdentification <FinInstnId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2920 to 2920.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2920

```text
82.1.12.3.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C3 2920
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
   LEI <LEI> [0..1] IdentifierSet 2920
   Name <Nm> [0..1] Text 2921
   PostalAddress <PstlAdr> [0..1] ± 2921
   Other <Othr> [0..1] ± 2921
82.1.12.3.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C3 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 3320
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
82.1.12.3.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 2917 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 2918
   MemberIdentification <MmbId> [1..1] Text 2918
82.1.12.3.1.3  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identifier of the financial institution.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2920 August 2026
```

