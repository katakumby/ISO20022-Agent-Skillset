---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.51 CorporateActionEventProcessingType2Choice", "16.1.15.51.2 Proprietary <Prtry>"]
file_pages: [972]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.51.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 972 to 972.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 972

```text
CodeName Name Definition
DISN Distribution Holder of the relevant security on a
certain date, for example, the record
date, will receive a benefit without giving
up the underlying security.
REOR Reorganisation Underlying security will be debited and
may be replaced by another resource (or
resources).
16.1.15.51.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the processing type of a corporate action event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.52  AdditionalBusinessProcessFormat11Choice
Definition: Choice between a standard code or proprietary code to specify the type of the additional
business process, that is, a tax refund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 972
Or}   Proprietary <Prtry> [1..1] ± 973
16.1.15.52.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the additional business process "tax refund" linked to a corporate
action event.
Datatype: "AdditionalBusinessProcess7Code" on page 1160
CodeName Name Definition
CLAI ClaimOrCompensation Relates to a claim on the associated
corporate action event.
TAXR TaxRefund Relates to a tax refund from the
authorities on the associated corporate
action event.
ACLA AutomaticMarketClaim Will automatically give rise to market
claims by the account servicer, for
example, a Central Securities Depository
(CSD).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 972 February 2026
```

