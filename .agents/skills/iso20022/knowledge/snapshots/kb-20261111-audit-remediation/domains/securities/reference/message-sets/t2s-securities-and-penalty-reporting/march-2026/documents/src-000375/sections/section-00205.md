---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [276, 277]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 276 to 277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 276

```text
Constraints
• BalanceForAccountOrSubAccountRule
BalanceForAccount must be present or SubAccountDetails must be present, both may be present.
7.1.5.14.1  SafekeepingAccount <SfkpgAcct>
Presence: [1..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
7.1.5.14.2  BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Report on the net position of a security, on a single securities account, for a certain date.
Impacted by: C7 "AggregateBalanceGuideline", C11 "BalanceAtSafekeepingPlaceRule", C22
"FinancialInstrumentAttributesRule"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 276 March 2026
```

## File page 277

```text
BalanceForAccount <BalForAcct> contains the following AggregateBalanceInformation47
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Constraints
• AggregateBalanceGuideline
If AvailableBalance and NotAvailableBalance are both present, then the AggregateBalance should
be the sum of AvailableBalance and NotAvailableBalance.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 277 March 2026
```

