---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.8 TransactionOverhead <TxOvrhd>", "38.4.15.8.4.8.5 IndividualFee <IndvFee>", "38.4.15.8.4.8.5.10 InformativeIndicator <InftvInd>"]
file_pages: [1411]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.8.5.10 InformativeIndicator <InftvInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1411 to 1411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1411

```text
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
38.4.15.8.4.8.5.10  InformativeIndicator <InftvInd>
Presence: [1..1]
Definition: Indicates the information is provided for information purposes only. When the value is 'false'
or '0' the amount provided is taken into consideration in the transaction overhead. When the value is
'true' or '1' the amount provided is not taken into consideration in the transaction overhead.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.8.4.8.6  IndividualTax <IndvTax>
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
38.4.15.8.4.8.7  DigitalNetworkFee <DgtlNtwkFee>
Presence: [0..2]
Definition: Digital network fee assigned to a transaction.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1411 May 2026
```

