---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "5.4 Message Building Blocks", "5.4.4 AccountServicer <AcctSvcr>"]
file_pages: [173, 174, 175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 5.4.4 AccountServicer <AcctSvcr>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 173 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
5.4.4 AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Central securities depository where the securities accounts are held.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
5.4.5 Balances <Bals>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
Impacted by: C12 "BalanceForAccountOrSubAccountRule"
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 173 March 2026
```

## File page 174

```text
Balances <Bals> contains the following elements (see "Balance30" on page 273 for details)
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
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 174 March 2026
```

## File page 175

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SafekeepingAccount <SfkpgAcct> [1..1] ± 292
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
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 175 March 2026
```

