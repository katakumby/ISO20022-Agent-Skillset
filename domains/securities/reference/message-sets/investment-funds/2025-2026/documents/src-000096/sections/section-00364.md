---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.8.13 Fees <Fees>"]
file_pages: [502]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.8.13 Fees <Fees>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 502 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 502

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
24.4.8.13  Fees <Fees>
Presence: [0..*]
Definition: Fee related to the transfer of the financial instrument.
Impacted by: C18 "FeeTaxElementRule"
Fees <Fees> contains the following elements (see "Fees2" on page 4434 for details)
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
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 502 May 2026
```

