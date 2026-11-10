---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.14 RateAndAmountDetails <RateAndAmtDtls>"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.14 RateAndAmountDetails <RateAndAmtDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
5.4.9.14  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about rates and amounts related to a corporate action option.
RateAndAmountDetails <RateAndAmtDtls> contains the following CorporateActionRate127
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProposedRate <PropsdRate> [0..1] Rate 312
   OversubscriptionRate <OvrsbcptRate> [0..1] ± 312
   RequestedWithholdingTaxRate <ReqdWhldgTaxRate> [0..*] ± 312
   RequestedSecondLevelTaxRate
<ReqdScndLvlTaxRate>
[0..*] ± 313
5.4.9.14.1  ProposedRate <PropsdRate>
Presence: [0..1]
Definition: Rate proposed in a remarketing of variable rate notes.
Datatype: "Percentage14Rate" on page 1247
5.4.9.14.2  OversubscriptionRate <OvrsbcptRate>
Presence: [0..1]
Definition: Rate of allowed over-subscription.
OversubscriptionRate <OvrsbcptRate> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
5.4.9.14.3  RequestedWithholdingTaxRate <ReqdWhldgTaxRate>
Presence: [0..*]
Definition: Requested tax rate that will be withheld by the tax authorities of the jurisdiction of the issuer,
for which a relief at source and/or reclaim may be possible.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 312 February 2026
```

