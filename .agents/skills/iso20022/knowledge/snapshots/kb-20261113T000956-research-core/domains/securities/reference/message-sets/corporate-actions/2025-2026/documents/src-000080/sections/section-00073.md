---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.6 InterestAccruedNumberOfDays <IntrstAcrdNbOfDays>"]
file_pages: [119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.6 InterestAccruedNumberOfDays <IntrstAcrdNbOfDays>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 119 to 119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 119

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
3.4.10.6  InterestAccruedNumberOfDays <IntrstAcrdNbOfDays>
Presence: [0..1]
Definition: Number of days used for calculating the accrued interest amount.
Impacted by: C86 "NumberRule"
Datatype: "Max3Number" on page 1247
Constraints
• NumberRule
If Number is negative, then Sign must be present.
3.4.10.7  CouponNumber <CpnNb>
Presence: [0..*]
Definition: Number of the coupon attached/associated with a security.
CouponNumber <CpnNb> contains one of the following elements (see "IdentificationFormat3Choice"
on page 875 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortIdentification <ShrtId> [1..1] Text 875
Or   LongIdentification <LngId> [1..1] Text 875
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 875
3.4.10.8  AcceptancePriorityLevel <AccptncPrtyLvl>
Presence: [0..1]
Definition: Level of priority of the given offer which will be accepted by the issuer/agent within the tiered
structure of the event.
Offer events in many cases are subject to proration.
Datatype: "Exact3UpperCaseAlphaNumericText" on page 1248
3.4.10.9  CertificationBreakdownIndicator <CertfctnBrkdwnInd>
Presence: [0..1]
Definition: Indicates whether certification/breakdown is required.
Yes = certification required.
No = no certification required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 119 February 2026
```

