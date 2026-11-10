---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.1 OptionNumber <OptnNb>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
On Condition
    /OptionFeatures[*]/Code is different from value 'InstructCashAmount'
Following Must be True
    /PriceDetails/MaximumCashToInstruct Must be absent
 And    /PriceDetails/MinimumCashToInstruct Must be absent
 And    /PriceDetails/MinimumMultipleCashToInstruct Must be absent
• OptionNumberGuideline
For differentiation between options, it is recommended to use the OptionNumber rather than the
OptionType, for example, in the case where two or more offers can be described by the same
corporate action option code.
• OptionTypeUnknownProceedsUsageRule
When used, the corporate action option code PRUN (Unknown Proceeds) should be maintained
throughout the full lifecycle of the event.
• RevocabilityPeriodRule
If WithdrawalAllowedIndicator or ChangeAllowedIndicator is present and is 'true' or '1' (Yes), then
PeriodDetails/RevocabilityPeriod must be present to indicate the period during which the change or
withdrawal of instruction is allowed.
3.4.11.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
Datatype: "Exact3NumericText" on page 1248
3.4.11.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption37Choice"
on page 946 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 946
Or}   Proprietary <Prtry> [1..1] ± 947
3.4.11.3  FractionDisposition <FrctnDspstn>
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 140 February 2026
```

