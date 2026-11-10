---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.2 ChargesFees <ChrgsFees>"]
file_pages: [653]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.2 ChargesFees <ChrgsFees>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 653 to 653.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 653

```text
AdditionalTax <AddtlTax> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
8.4.12.11.14.2  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charges/fees that cannot be categorised.
ChargesFees <ChrgsFees> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
8.4.12.11.14.3  FiscalStamp <FsclStmp>
Presence: [0..1]
Definition: Percentage of fiscal tax to apply.
Datatype: "Percentage14Rate" on page 1247
8.4.12.11.14.4  GrossDistributionRate <GrssDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate before tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 653 February 2026
```

