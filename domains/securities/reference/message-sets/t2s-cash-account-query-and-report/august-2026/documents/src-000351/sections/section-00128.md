---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Financial Institution Identification", "7.1.5.3 BranchAndFinancialInstitutionIdentification8", "7.1.5.3.2 BranchIdentification <BrnchId>"]
file_pages: [143]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.3.2 BranchIdentification <BrnchId>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 143 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 143

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 139 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 139
   SchemeName <SchmeNm> [0..1]  139
{Or     Code <Cd> [1..1] CodeSet 139
Or}     Proprietary <Prtry> [1..1] Text 139
   Issuer <Issr> [0..1] Text 139
7.1.5.3.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 143
   LEI <LEI> [0..1] IdentifierSet 143
   Name <Nm> [0..1] Text 143
   PostalAddress <PstlAdr> [0..1] ± 143
7.1.5.3.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 183
7.1.5.3.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 181
7.1.5.3.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 182
7.1.5.3.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 143 August 2026
```

