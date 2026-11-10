---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.3 SubAccountDetails <SubAcctDtls>"]
file_pages: [289, 290]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.3 SubAccountDetails <SubAcctDtls>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 289 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C12 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 375
   Envelope <Envlp> [1..1] (External Schema) 376
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
7.1.5.14.3  SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: Sub-account of the safekeeping or investment account.
Impacted by: C3 "ActivityAndBalanceForSubAccount1Rule", C4
"ActivityAndBalanceForSubAccount2Rule", C38 "SubSafekeepingReportingRule"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 289 March 2026
```

## File page 290

```text
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification75 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1]  291
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 291
Or     NameAndAddress <NmAndAdr> [1..1] ± 291
Or}     Country <Ctry> [1..1] CodeSet C3 292
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
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 290 March 2026
```

