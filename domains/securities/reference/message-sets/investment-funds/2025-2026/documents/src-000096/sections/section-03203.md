---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.1 Fees2", "66.1.8.1.1 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [4435]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.1.1 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4435 to 4435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4435

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 4435
   IndividualFee <IndvFee> [0..*]  4435
     Type <Tp> [1..1]  4436
{Or       Code <Cd> [1..1] CodeSet 4436
Or}       Proprietary <Prtry> [1..1] ± 4437
     Basis <Bsis> [0..1]  4437
{Or       Code <Cd> [1..1] CodeSet 4437
Or}       Proprietary <Prtry> [1..1] ± 4438
     Amount <Amt> [1..1] Amount C1, C13 4438
     DiscountDetails <DscntDtls> [0..1]  C16 4438
       Amount <Amt> [0..1] Amount C1, C13 4439
       Rate <Rate> [0..1] Rate 4439
       Basis <Bsis> [0..1]  4439
{Or         Code <Cd> [1..1] CodeSet 4440
Or}         Proprietary <Prtry> [1..1] ± 4440
     ChargeBearer <ChrgBr> [0..1] CodeSet 4440
     RecipientIdentification <RcptId> [0..1] ± 4441
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax) must be
present.
66.1.8.1.1  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
66.1.8.1.2  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4435 May 2026
```

