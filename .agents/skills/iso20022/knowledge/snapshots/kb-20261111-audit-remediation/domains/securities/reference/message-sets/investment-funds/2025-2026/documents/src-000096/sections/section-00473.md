---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.12 UnitsDetails <UnitsDtls>", "28.4.7.12.8 TransactionOverhead <TxOvrhd>", "28.4.7.12.8.5 IndividualFee <IndvFee>", "28.4.7.12.8.5.10 InformativeIndicator <InftvInd>"]
file_pages: [649]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.12.8.5.10 InformativeIndicator <InftvInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 649 to 649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 649

```text
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
28.4.7.12.8.5.10  InformativeIndicator <InftvInd>
Presence: [1..1]
Definition: Indicates the information is provided for information purposes only. When the value is 'false'
or '0' the amount provided is taken into consideration in the transaction overhead. When the value is
'true' or '1' the amount provided is not taken into consideration in the transaction overhead.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
28.4.7.12.8.6  IndividualTax <IndvTax>
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
28.4.7.12.8.7  DigitalNetworkFee <DgtlNtwkFee>
Presence: [0..2]
Definition: Digital network fee assigned to a transaction.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 649 May 2026
```

