---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.3 SubAccountDetails <SubAcctDtls>", "7.1.5.14.3.1 AccountOwner <AcctOwnr>", "7.1.5.14.3.1.3 Country <Ctry>"]
file_pages: [292, 293]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.3.1.3 Country <Ctry>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 292 to 293.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 292

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 443 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 443
   Address <Adr> [0..1] ± 444
7.1.5.14.3.1.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.5.14.3.2  SafekeepingAccount <SfkpgAcct>
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
7.1.5.14.3.3  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.5.14.3.4  BalanceForSubAccount <BalForSubAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities subaccount.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 292 March 2026
```

## File page 293

```text
Impacted by: C7 "AggregateBalanceGuideline", C11 "BalanceAtSafekeepingPlaceRule", C22
"FinancialInstrumentAttributesRule"
BalanceForSubAccount <BalForSubAcct> contains the following AggregateBalanceInformation47
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Constraints
• AggregateBalanceGuideline
If AvailableBalance and NotAvailableBalance are both present, then the AggregateBalance should
be the sum of AvailableBalance and NotAvailableBalance.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 293 March 2026
```

