---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.16 TransactionOverhead <TxOvrhd>", "55.4.5.20.16.5 IndividualFee <IndvFee>", "55.4.5.20.16.5.10 InformativeIndicator <InftvInd>"]
file_pages: [3961]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.16.5.10 InformativeIndicator <InftvInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3961 to 3961.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3961

```text
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
55.4.5.20.16.5.10  InformativeIndicator <InftvInd>
Presence: [1..1]
Definition: Indicates the information is provided for information purposes only. When the value is 'false'
or '0' the amount provided is taken into consideration in the transaction overhead. When the value is
'true' or '1' the amount provided is not taken into consideration in the transaction overhead.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
55.4.5.20.16.6  IndividualTax <IndvTax>
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
55.4.5.20.16.7  DigitalNetworkFee <DgtlNtwkFee>
Presence: [0..2]
Definition: Digital network fee assigned to a transaction.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3961 May 2026
```

