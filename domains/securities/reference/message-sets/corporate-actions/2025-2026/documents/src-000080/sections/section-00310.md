---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.1 OptionNumber <OptnNb>"]
file_pages: [430]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 430 to 430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

```text
• RevocabilityPeriodRule
If WithdrawalAllowedIndicator or ChangeAllowedIndicator is present and is 'true' or '1' (Yes), then
PeriodDetails/RevocabilityPeriod must be present to indicate the period during which the change or
withdrawal of instruction is allowed.
7.4.13.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
Datatype: "Exact3NumericText" on page 1248
7.4.13.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption37Choice"
on page 946 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 946
Or}   Proprietary <Prtry> [1..1] ± 947
7.4.13.3  FractionDisposition <FrctnDspstn>
Presence: [0..1]
Definition: Specifies how fractions resulting from derived securities will be processed or how prorated
decisions will be rounding, if provided with a pro ration rate.
FractionDisposition <FrctnDspstn> contains one of the following elements (see
"FractionDispositionType26Choice" on page 899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 899
Or}   Proprietary <Prtry> [1..1] ± 900
7.4.13.4  OfferType <OfferTp>
Presence: [0..*]
Definition: Specifies the conditions that apply to the offer.
OfferType <OfferTp> contains one of the following OfferTypeFormat17Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 431
Or}   Proprietary <Prtry> [1..1] ± 431
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 430 February 2026
```

