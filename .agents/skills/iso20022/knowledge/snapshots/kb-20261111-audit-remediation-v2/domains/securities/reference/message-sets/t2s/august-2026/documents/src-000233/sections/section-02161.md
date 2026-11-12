---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.12 Financial Institution Identification", "82.1.12.3 BranchAndFinancialInstitutionIdentification8", "82.1.12.3.2 BranchIdentification <BrnchId>"]
file_pages: [2922]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.12.3.2 BranchIdentification <BrnchId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2922 to 2922.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2922

```text
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 2918 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2918
   SchemeName <SchmeNm> [0..1]  2918
{Or     Code <Cd> [1..1] CodeSet 2919
Or}     Proprietary <Prtry> [1..1] Text 2919
   Issuer <Issr> [0..1] Text 2919
82.1.12.3.2  BranchIdentification <BrnchId>
Presence: [0..1]
Definition: Identifies a specific branch of a financial institution.
Usage: This component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
BranchIdentification <BrnchId> contains the following BranchData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 2922
   LEI <LEI> [0..1] IdentifierSet 2922
   Name <Nm> [0..1] Text 2922
   PostalAddress <PstlAdr> [0..1] ± 2923
82.1.12.3.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 3328
82.1.12.3.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification for the branch of the financial institution.
Datatype: "LEIIdentifier" on page 3322
82.1.12.3.2.3  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 3326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2922 August 2026
```

