---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.3 SubAccountDetails <SubAcctDtls>", "82.1.5.16.3.1 AccountOwner <AcctOwnr>", "82.1.5.16.3.1.3 Country <Ctry>"]
file_pages: [2884, 2885]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.3.1.3 Country <Ctry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2884 to 2885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2884

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 3098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 3098
   Address <Adr> [0..1] ± 3098
82.1.5.16.3.1.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.5.16.3.2  SafekeepingAccount <SfkpgAcct>
Presence: [1..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
82.1.5.16.3.3  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.5.16.3.4  BalanceForSubAccount <BalForSubAcct>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities subaccount.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2884 August 2026
```

## File page 2885

```text
Impacted by: C7 "AggregateBalanceGuideline", C11 "BalanceAtSafekeepingPlaceRule", C22
"FinancialInstrumentAttributesRule"
BalanceForSubAccount <BalForSubAcct> contains the following AggregateBalanceInformation47
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceDate <BalDt> [1..1] ± 2886
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
2886
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C28 2887
   InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 2889
   ValuationHaircutDetails <ValtnHrcutDtls> [0..1] ± 2890
   AggregateBalance <AggtBal> [0..1] ± 2890
   AvailableBalance <AvlblBal> [0..1] ± 2890
   NotAvailableBalance <NotAvlblBal> [0..1] ± 2891
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 2891
   CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 2891
   PriceDetails <PricDtls> [0..*] ± C41 2892
   ForeignExchangeDetails <FXDtls> [0..*] ± 2892
   DaysAccrued <DaysAcrd> [0..1] Quantity 2892
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C19 2893
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C19 2893
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2893
   BalanceBreakdown <BalBrkdwn> [0..*] ± C10,
C35
2894
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C21,
C37
2894
   BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*] ± C23, C8 2895
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 2896
   SupplementaryData <SplmtryData> [0..*] ± C6 2896
Constraints
• AggregateBalanceGuideline
If AvailableBalance and NotAvailableBalance are both present, then the AggregateBalance should
be the sum of AvailableBalance and NotAvailableBalance.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2885 August 2026
```

