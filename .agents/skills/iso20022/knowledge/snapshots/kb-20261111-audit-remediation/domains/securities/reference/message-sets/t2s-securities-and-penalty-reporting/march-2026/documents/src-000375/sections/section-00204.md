---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.13 SubBalanceInformation18", "7.1.5.13.5 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>"]
file_pages: [273, 274, 275]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.13.5 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 273 to 275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 273

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown54" on
page 451 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 451
   LotQuantity <LotQty> [0..1] ± 451
   LotDateTime <LotDtTm> [0..1] ± 452
   LotPrice <LotPric> [0..1] ± 452
   TypeOfPrice <TpOfPric> [0..1] ± 452
7.1.5.13.5  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
Presence: [0..*]
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C20 "EligibleForCollateralPurposesRule", C36 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls> contains the following elements (see
"AdditionalBalanceInformation18" on page 261 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 261
   Quantity <Qty> [1..1] ± 262
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 262
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 262
Constraints
• EligibleForCollateralPurposesRule
If Subbalance type is EligibleForCollateralPurposes, then QuantityAndAvailability cannot be used.
On Condition
    /SubBalanceType/Code is equal to value 'EligibleForCollateralPurposes'
Following Must be True
    /Quantity/Quantity/QuantityAndAvailability Must be absent
• SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
7.1.5.14  Balance30
Definition: Report on the net position of a security, on a single securities account, for a certain date.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 273 March 2026
```

## File page 274

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [1..1] ± 276
   BalanceForAccount <BalForAcct> [0..*]  C7, C11,
C22
276
     BalanceDate <BalDt> [1..1] ± 278
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C4, C5,
C7, C8,
C9
278
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C28 279
     InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 281
     ValuationHaircutDetails <ValtnHrcutDtls> [0..1] ± 282
     AggregateBalance <AggtBal> [0..1] ± 282
     AvailableBalance <AvlblBal> [0..1] ± 282
     NotAvailableBalance <NotAvlblBal> [0..1] ± 283
     SafekeepingPlace <SfkpgPlc> [0..1] ± C33 283
     CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 283
     PriceDetails <PricDtls> [0..*] ± C41 284
     ForeignExchangeDetails <FXDtls> [0..*] ± 284
     DaysAccrued <DaysAcrd> [0..1] Quantity 284
     AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C19 285
     InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C19 285
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 285
     BalanceBreakdown <BalBrkdwn> [0..*] ± C10,
C35
286
     AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C21,
C37
286
     BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*] ± C23, C8 287
     HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 288
     SupplementaryData <SplmtryData> [0..*] ± C12 288
   SubAccountDetails <SubAcctDtls> [0..*]  C3, C4,
C38
289
     AccountOwner <AcctOwnr> [0..1]  291
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C2 291
Or       NameAndAddress <NmAndAdr> [1..1] ± 291
Or}       Country <Ctry> [1..1] CodeSet C3 292
     SafekeepingAccount <SfkpgAcct> [1..1] ± 292
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 274 March 2026
```

## File page 275

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ActivityIndicator <ActvtyInd> [1..1] Indicator 292
     BalanceForSubAccount <BalForSubAcct> [0..*]  C7, C11,
C22
292
       BalanceDate <BalDt> [1..1] ± 294
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C4, C5,
C7, C8,
C9
294
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C28 295
       InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 297
       ValuationHaircutDetails <ValtnHrcutDtls> [0..1] ± 298
       AggregateBalance <AggtBal> [0..1] ± 298
       AvailableBalance <AvlblBal> [0..1] ± 298
       NotAvailableBalance <NotAvlblBal> [0..1] ± 299
       SafekeepingPlace <SfkpgPlc> [0..1] ± C33 299
       CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 299
       PriceDetails <PricDtls> [0..*] ± C41 300
       ForeignExchangeDetails <FXDtls> [0..*] ± 300
       DaysAccrued <DaysAcrd> [0..1] Quantity 300
       AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C19 301
       InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C19 301
       QuantityBreakdown <QtyBrkdwn> [0..*] ± 301
       BalanceBreakdown <BalBrkdwn> [0..*] ± C10,
C35
302
       AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C21,
C37
302
       BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*] ± C23, C8 303
       HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 304
       SupplementaryData <SplmtryData> [0..*] ± C12 304
   AccountBaseCurrencyTotalAmounts
<AcctBaseCcyTtlAmts>
[0..1]  C40 305
     TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 305
     TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 306
     TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 306
     TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 306
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 275 March 2026
```

