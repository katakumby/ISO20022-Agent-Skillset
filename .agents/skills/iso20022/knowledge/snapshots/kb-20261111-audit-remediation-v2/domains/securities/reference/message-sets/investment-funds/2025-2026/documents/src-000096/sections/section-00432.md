---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.8.15 IndividualTax <IndvTax>"]
file_pages: [591]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.8.15 IndividualTax <IndvTax>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 591 to 591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 591

```text
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
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax) must be
present.
26.4.8.15  IndividualTax <IndvTax>
Presence: [0..*]
Definition: Tax related to the transfer of the financial instrument.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 591 May 2026
```

