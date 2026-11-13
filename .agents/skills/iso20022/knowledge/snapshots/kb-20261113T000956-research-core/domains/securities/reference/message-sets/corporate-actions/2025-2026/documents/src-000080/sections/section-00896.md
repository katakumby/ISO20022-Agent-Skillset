---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.10 RateAndAmountFormat62Choice", "16.1.22.10.4 RateTypeAndRate <RateTpAndRate>", "16.1.22.10.4.1 RateType <RateTp>"]
file_pages: [1114]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.10.4.1 RateType <RateTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1114 to 1114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1114

```text
RateTypeAndRate <RateTpAndRate> contains the following RateTypeAndPercentageRate14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  1114
{Or     Code <Cd> [1..1] CodeSet 1114
Or}     Proprietary <Prtry> [1..1] ± 1114
   Rate <Rate> [1..1] Rate 1115
16.1.22.10.4.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
RateType <RateTp> contains one of the following DeemedRateType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1114
Or}   Proprietary <Prtry> [1..1] ± 1114
16.1.22.10.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of deemed rate.
Datatype: "DeemedRateType1Code" on page 1206
CodeName Name Definition
DEDI DeemedDividendProceeds Deemed rate of dividend proceeds
attributed to the security holder.
DEFP DeemedFundProceeds Deemed rate of fund proceeds attributed
to the security holder.
DEIT DeemedInterestProceeds Deemed rate of interest proceeds
attributed to the security holder.
DERY DeemedRoyaltiesProceeds Deemed rate of royalties proceeds
attributed to the security holder.
16.1.22.10.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of deemed rate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1114 February 2026
```

