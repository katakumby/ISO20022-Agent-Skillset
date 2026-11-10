---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.8 CountryOfIncomeSource <CtryOfIncmSrc>"]
file_pages: [490, 491]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.8 CountryOfIncomeSource <CtryOfIncmSrc>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 490 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 490

```text
ExemptionType <XmptnTp> contains the following elements (see "GenericIdentification30" on
page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
7.4.13.23.8  CountryOfIncomeSource <CtryOfIncmSrc>
Presence: [0..1]
Definition: Indicates the country from which the income originates.
Impacted by: C13 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.4.13.23.9  CashAccountIdentification <CshAcctId>
Presence: [0..1]
Definition: Identification of the account in which cash is maintained.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"CashAccountIdentification9Choice" on page 829 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 829
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 829
Or}   Proprietary <Prtry> [1..1] Text 830
7.4.13.23.10  AmountDetails <AmtDtls>
Presence: [0..1]
Definition: Provides information about the amounts related to a cash movement.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 490 February 2026
```

## File page 491

```text
AmountDetails <AmtDtls> contains the following CorporateActionAmounts78 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GrossAmount <GrssAmt> [0..1] Amount C1, C14 492
   NetAmount <NetAmt> [0..1] Amount C1, C14 493
   SolicitationFees <SlctnFees> [0..1] Amount C1, C14 493
   CashInLieuOfShare <CshInLieuOfShr> [0..1] Amount C1, C14 493
   CapitalGain <CptlGn> [0..1] Amount C1, C14 494
   InterestAmount <IntrstAmt> [0..1] Amount C1, C14 494
   MarketClaimAmount <MktClmAmt> [0..1] Amount C1, C14 495
   IndemnityAmount <IndmntyAmt> [0..1] Amount C1, C14 495
   ManufacturedDividendPaymentAmount
<ManfctrdDvddPmtAmt>
[0..1] Amount C1, C14 495
   ReinvestmentAmount <RinvstmtAmt> [0..1] Amount C1, C14 496
   FullyFrankedAmount <FullyFrnkdAmt> [0..1] Amount C1, C14 496
   UnfrankedAmount <UfrnkdAmt> [0..1] Amount C1, C14 497
   SundryOrOtherAmount <SndryOrOthrAmt> [0..1] Amount C1, C14 497
   TaxFreeAmount <TaxFreeAmt> [0..1] Amount C1, C14 497
   TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C1, C14 498
   ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C1, C14 498
   StampDutyAmount <StmpDtyAmt> [0..1] Amount C1, C14 499
   TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C1, C14 499
   TaxCreditAmount <TaxCdtAmt> [0..1] Amount C1, C14 499
   TaxArrearAmount <TaxArrearAmt> [0..1] Amount C1, C14 500
   AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C1, C14 500
   WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C14 501
   SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C14 501
   FiscalStampAmount <FsclStmpAmt> [0..1] Amount C1, C14 501
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C1, C14 502
   PayingAgentCommissionAmount
<PngAgtComssnAmt>
[0..1] Amount C1, C14 502
   LocalBrokerCommissionAmount
<LclBrkrComssnAmt>
[0..1] Amount C1, C14 503
   RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C1, C14 503
   ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C1, C14 503
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 491 February 2026
```

