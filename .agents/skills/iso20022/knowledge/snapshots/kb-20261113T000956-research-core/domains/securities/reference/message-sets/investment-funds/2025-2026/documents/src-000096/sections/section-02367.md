---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.26 TransactionOverhead <TxOvrhd>", "52.4.5.10.26.5 IndividualFee <IndvFee>", "52.4.5.10.26.5.10 InformativeIndicator <InftvInd>"]
file_pages: [3330]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.26.5.10 InformativeIndicator <InftvInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3330 to 3330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3330

```text
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
52.4.5.10.26.5.10  InformativeIndicator <InftvInd>
Presence: [1..1]
Definition: Indicates the information is provided for information purposes only. When the value is 'false'
or '0' the amount provided is taken into consideration in the transaction overhead. When the value is
'true' or '1' the amount provided is not taken into consideration in the transaction overhead.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
52.4.5.10.26.6  IndividualTax <IndvTax>
Presence: [0..*]
Definition: Individual tax.
IndividualTax <IndvTax> contains the following elements (see "Tax35" on page 5245 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  5246
{Or     Code <Cd> [1..1] CodeSet 5246
Or}     Proprietary <Prtry> [1..1] ± 5248
   AppliedAmount <ApldAmt> [1..1] Amount C1, C13 5248
   AppliedRate <ApldRate> [0..1] Rate 5248
   Country <Ctry> [0..1] CodeSet C12 5248
   RecipientIdentification <RcptId> [0..1] ± 5249
   TaxCalculationDetails <TaxClctnDtls> [0..1]  5249
     Basis <Bsis> [0..1]  5249
{Or       Code <Cd> [1..1] CodeSet 5249
Or}       Proprietary <Prtry> [1..1] ± 5250
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5250
52.4.5.10.26.7  DigitalNetworkFee <DgtlNtwkFee>
Presence: [0..*]
Definition: Digital network fee assigned to a transaction.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3330 May 2026
```

