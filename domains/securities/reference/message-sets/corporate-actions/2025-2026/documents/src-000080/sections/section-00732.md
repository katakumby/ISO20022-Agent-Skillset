---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.27 DistributionTypeFormat7Choice", "16.1.15.27.1 Code <Cd>"]
file_pages: [925]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.27.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 925 to 925.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 925

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 925
Or}   Proprietary <Prtry> [1..1] ± 925
16.1.15.27.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify whether the proceeds of the event will be distributed on a rolling
basis rather than on a specific date.
Datatype: "DistributionType3Code" on page 1207
CodeName Name Definition
FINL Final Final payment.
INTE Interim Interim payment.
ONGO Ongoing Event is ongoing for acceptance on an
unsolicited basis.
ROLL RollingBasis Event will have a number of acceptance
and payment dates until further
announcement by the Issuer or its agent.
16.1.15.27.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of distribution.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.28  BlockChainAddressWallet3
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 925
   Type <Tp> [0..1] ± 926
   Name <Nm> [0..1] Text 926
16.1.15.28.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 925 February 2026
```

