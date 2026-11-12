---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.8 BeneficialOwnerDetails <BnfclOwnrDtls>", "5.4.8.6 CertificationType <CertfctnTp>"]
file_pages: [303, 304]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.8.6 CertificationType <CertfctnTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 303 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 303

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
5.4.8.6  CertificationType <CertfctnTp>
Presence: [0..*]
Definition: Type of certification which is required.
CertificationType <CertfctnTp> contains one of the following elements (see
"BeneficiaryCertificationType10Choice" on page 982 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 982
Or}   Proprietary <Prtry> [1..1] ± 982
5.4.8.7  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..1]
Definition: Requested percentage of a cash distribution that will be withheld by the tax authorities of the
jurisdiction of the issuer, for which a relief at source and/or reclaim may be possible.
WithholdingTaxRate <WhldgTaxRate> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
5.4.8.8  CertificationBreakdown <CertfctnBrkdwn>
Presence: [0..*]
Definition: Provides additional information about the type of certification/breakdown required.
Datatype: "Max350Text" on page 1250
5.4.9 CorporateActionInstruction <CorpActnInstr>
Presence: [1..1]
Definition: Information about the corporate action instruction.
Impacted by: C20 "OptionNumber1Rule", C21 "OptionNumber2Rule"
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 303 February 2026
```

## File page 304

```text
CorporateActionInstruction <CorpActnInstr> contains the following CorporateActionOption237
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] ± 305
   OptionType <OptnTp> [1..1] ± 305
   OptionFeatures <OptnFeatrs> [0..1] ± 306
   FractionDisposition <FrctnDspstn> [0..1] ± 306
   ChangeType <ChngTp> [0..*] ± 306
   EligibleForCollateralIndicator <ElgblForCollInd> [0..1] Indicator 306
   SolicitationDealerFeeIndicator <SlctnDealrFeeInd> [0..1] Indicator 307
   CurrencyToBuy <CcyToBuy> [0..1] CodeSet C1 307
   CurrencyToSell <CcyToSell> [0..1] CodeSet C1 307
   CurrencyOption <CcyOptn> [0..1] CodeSet C1 308
   SecurityIdentification <SctyId> [0..1] ± C10,
C11,
C17,
C18,
C23
308
   SecuritiesQuantityOrInstructedAmount
<SctiesQtyOrInstdAmt>
[1..1]  309
{Or     SecuritiesQuantity <SctiesQty> [1..1]  309
       ConditionalQuantity <CondlQty> [0..1] ± C12 310
       InstructedQuantity <InstdQty> [1..1] ± 310
       AdditionalRoundUpQuantity <AddtlRndUpQty> [0..1] ± C12 310
Or}     InstructedAmount <InstdAmt> [1..1] Amount C1, C9 311
   ExecutionRequestedDateTime <ExctnReqdDtTm> [0..1] ± 311
   RateAndAmountDetails <RateAndAmtDtls> [0..1]  312
     ProposedRate <PropsdRate> [0..1] Rate 312
     OversubscriptionRate <OvrsbcptRate> [0..1] ± 312
     RequestedWithholdingTaxRate
<ReqdWhldgTaxRate>
[0..*] ± 312
     RequestedSecondLevelTaxRate
<ReqdScndLvlTaxRate>
[0..*] ± 313
   PriceDetails <PricDtls> [0..1]  C15 313
     IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  314
{Or       IndicativePrice <IndctvPric> [1..1] ± 314
Or}       MarketPrice <MktPric> [1..1] ± 315
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 304 February 2026
```

