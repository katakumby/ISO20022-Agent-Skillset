---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>"]
file_pages: [2162, 2163, 2164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15 TransactionOverhead <TxOvrhd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2162 to 2164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2162

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
44.4.4.9.15  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and tax to be applied to the gross amount.
Impacted by: C19 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2162 May 2026
```

## File page 2163

```text
TransactionOverhead <TxOvrhd> contains the following FeeAndTax2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2165
   IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
2165
     Type <Tp> [1..1]  2166
{Or       Code <Cd> [1..1] CodeSet 2166
Or}       Proprietary <Prtry> [1..1] ± 2167
     Basis <Bsis> [0..1]  2167
{Or       Code <Cd> [1..1] CodeSet 2168
Or}       Proprietary <Prtry> [1..1] ± 2168
     StandardAmount <StdAmt> [0..1] Amount C3, C10 2168
     StandardRate <StdRate> [0..1] Rate 2169
     DiscountDetails <DscntDtls> [0..1]  C16 2169
       Amount <Amt> [0..1] Amount C3, C10 2169
       Rate <Rate> [0..1] Rate 2170
       Basis <Bsis> [0..1]  2170
{Or         Code <Cd> [1..1] CodeSet 2170
Or}         Proprietary <Prtry> [1..1] ± 2171
     RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 2171
     RequestedRate <ReqdRate> [0..1] Rate 2171
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 2172
     RecipientIdentification <RcptId> [0..1] ± 2172
   IndividualTax <IndvTax> [0..*]  2172
     Type <Tp> [1..1]  2173
{Or       Code <Cd> [1..1] CodeSet 2173
Or}       Proprietary <Prtry> [1..1] ± 2175
     Tax <Tax> [0..1]  2175
{Or       Amount <Amt> [1..1] Amount C3, C10 2175
Or}       Rate <Rate> [1..1] Rate 2176
     Country <Ctry> [0..1] CodeSet C8 2176
     ExemptionIndicator <XmptnInd> [1..1] Indicator 2176
     ExemptionReason <XmptnRsn> [0..1]  2176
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2163 May 2026
```

## File page 2164

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 2176
Or}       Proprietary <Prtry> [1..1] ± 2179
     RecipientIdentification <RcptId> [0..1] ± 2179
     TaxCalculationDetails <TaxClctnDtls> [0..1]  2180
       Basis <Bsis> [1..1]  2180
{Or         Code <Cd> [1..1] CodeSet 2180
Or}         Proprietary <Prtry> [1..1] ± 2180
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  2181
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2181
       ISIN <ISIN> [0..1] IdentifierSet 2183
       OtherIdentification <OthrId> [0..*]  2183
         Identification <Id> [1..1] Text 2183
         Suffix <Sfx> [0..1] Text 2183
         Type <Tp> [1..1]  2183
{Or           Code <Cd> [1..1] CodeSet 2184
Or}           Proprietary <Prtry> [1..1] Text 2185
       Description <Desc> [0..1] Text 2185
     Quantity <Qty> [1..1]  2186
{Or       Quantity <Qty> [1..1] ± C15 2186
Or}       ProprietaryQuantity <PrtryQty> [1..1]  2186
         Quantity <Qty> [1..1] Quantity 2187
         QuantityType <QtyTp> [1..1] Text 2187
         Issuer <Issr> [1..1] Text 2187
         SchemeName <SchmeNm> [0..1] Text 2187
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2187
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2164 May 2026
```

