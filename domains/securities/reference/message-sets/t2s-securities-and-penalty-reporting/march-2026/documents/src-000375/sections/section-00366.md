---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.24 Safekeeping Place"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.24 Safekeeping Place

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

```text
7.1.24 Safekeeping Place
7.1.24.1  SafeKeepingPlace3
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 453
   LEI <LEI> [0..1] IdentifierSet 453
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
7.1.24.1.1  SafekeepingPlaceFormat <SfkpgPlcFrmt>
Presence: [0..1]
Definition: Unique identification of the party.
SafekeepingPlaceFormat <SfkpgPlcFrmt> contains one of the following elements (see
"SafekeepingPlaceFormat29Choice" on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  398
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 398
     Identification <Id> [0..1] Text 399
Or   Country <Ctry> [1..1] CodeSet C3 399
Or   TypeAndIdentification <TpAndId> [1..1]  399
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 399
     Identification <Id> [1..1] IdentifierSet C2 400
Or}   Proprietary <Prtry> [1..1] ± 400
7.1.24.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 552
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 453 March 2026
```

