---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.34 AdditionalBusinessProcessFormat15Choice", "16.1.15.34.2 Proprietary <Prtry>"]
file_pages: [942]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.34.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 942 to 942.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 942

```text
CodeName Name Definition
CONS Consent Relates to a consent within a corporate
action event other than a Consent event
(: 22F:: CAEV//CONS).
FPRE FullPrefunding Full pre-funding of a debt instrument by
the issuer prior to original maturity when
the issuer deposits assets in trust.
Applicable only in the frame of a partial
defeasance corporate action event.
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
16.1.15.34.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the additional business process linked to a corporate action
event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.35  OptionFeaturesFormat25Choice
Definition: Choice between a standard code and a proprietary code to specify the features that may
apply to a corporate action option.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 943
Or}   Proprietary <Prtry> [1..1] ± 943
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 942 February 2026
```

