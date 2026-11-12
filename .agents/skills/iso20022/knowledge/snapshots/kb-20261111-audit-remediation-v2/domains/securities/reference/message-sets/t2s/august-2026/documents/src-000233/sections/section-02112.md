---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [2868, 2869]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2868 to 2869.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2868

```text
Constraints
• BalanceForAccountOrSubAccountRule
BalanceForAccount must be present or SubAccountDetails must be present, both may be present.
82.1.5.16.1  SafekeepingAccount <SfkpgAcct>
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
82.1.5.16.2  BalanceForAccount <BalForAcct>
Presence: [0..*]
Definition: Report on the net position of a security, on a single securities account, for a certain date.
Impacted by: C7 "AggregateBalanceGuideline", C11 "BalanceAtSafekeepingPlaceRule", C22
"FinancialInstrumentAttributesRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2868 August 2026
```

## File page 2869

```text
BalanceForAccount <BalForAcct> contains the following AggregateBalanceInformation47
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceDate <BalDt> [1..1] ± 2870
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
2870
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C28 2871
   InvestmentFundsFinancialInstrumentAttributes
<InvstmtFndsFinInstrmAttrbts>
[0..1] ± 2873
   ValuationHaircutDetails <ValtnHrcutDtls> [0..1] ± 2874
   AggregateBalance <AggtBal> [0..1] ± 2874
   AvailableBalance <AvlblBal> [0..1] ± 2874
   NotAvailableBalance <NotAvlblBal> [0..1] ± 2875
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 2875
   CorporateActionOptionType <CorpActnOptnTp> [0..1] CodeSet 2875
   PriceDetails <PricDtls> [0..*] ± C41 2876
   ForeignExchangeDetails <FXDtls> [0..*] ± 2876
   DaysAccrued <DaysAcrd> [0..1] Quantity 2876
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C19 2877
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C19 2877
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2877
   BalanceBreakdown <BalBrkdwn> [0..*] ± C10,
C35
2878
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C21,
C37
2878
   BalanceAtSafekeepingPlace <BalAtSfkpgPlc> [0..*] ± C23, C8 2879
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 2880
   SupplementaryData <SplmtryData> [0..*] ± C6 2880
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
Target2-Securities 2869 August 2026
```

