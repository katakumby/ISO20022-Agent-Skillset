---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Financial Institution Identification", "6.1.12.3 BranchAndFinancialInstitutionIdentification8", "6.1.12.3.2 BranchIdentification <BrnchId>"]
file_pages: [833]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.3.2 BranchIdentification <BrnchId>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 833 to 833.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 833

```text
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 829 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 829
   SchemeName <SchmeNm> [0..1]  829
{Or     Code <Cd> [1..1] CodeSet 829
Or}     Proprietary <Prtry> [1..1] Text 830
   Issuer <Issr> [0..1] Text 830
6.1.12.3.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 833
   LEI <LEI> [0..1] IdentifierSet 833
   Name <Nm> [0..1] Text 833
   PostalAddress <PstlAdr> [0..1] ± 833
6.1.12.3.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 916
6.1.12.3.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 910
6.1.12.3.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 914
6.1.12.3.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
833 March 2026
```

