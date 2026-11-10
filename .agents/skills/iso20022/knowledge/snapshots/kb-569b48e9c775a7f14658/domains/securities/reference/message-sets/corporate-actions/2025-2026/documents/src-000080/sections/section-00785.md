---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.57 AdditionalBusinessProcessFormat18Choice"]
file_pages: [980]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.57 AdditionalBusinessProcessFormat18Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 980 to 980.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 980

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.57  AdditionalBusinessProcessFormat18Choice
Definition: Choice between a standard code or proprietary code to specify the type of the additional
business process, that is, a tax refund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 980
Or}   Proprietary <Prtry> [1..1] ± 981
16.1.15.57.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the additional business process "tax refund" linked to a corporate
action event.
Datatype: "AdditionalBusinessProcess10Code" on page 1158
CodeName Name Definition
CLAI ClaimOrCompensation Relates to a claim on the associated
corporate action event.
REVR NotificationOfReversal Indicates a preadvice of movement
reversal.
TAXR TaxRefund Relates to a tax refund from the
authorities on the associated corporate
action event.
PPUT PartialMandatoryPutRedemption Partial mandatory exchange of a portion
of bonds where the exchanged securities
are usually remarketed. The issuer may
offer holders the right to retain instead of
exchanging their securities. A lottery will
be used to determine eligibility for the
event.
PPRE PartialPreFunding Partial pre-funding of a debt instrument
prior to maturity drawn through a lottery
process. One new security is issued with
an earlier maturity date for the refunded
(called portion) and the other new
security is issued with the original
maturity date for the non refunded
(remaining) portion. Applicable only in
the frame of a partial defeasance
corporate action event.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 980 February 2026
```

