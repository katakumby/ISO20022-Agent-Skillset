---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.3 SubAccountDetails <SubAcctDtls>"]
file_pages: [2881, 2882]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.3 SubAccountDetails <SubAcctDtls>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2881 to 2882.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2881

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
82.1.5.16.3  SubAccountDetails <SubAcctDtls>
Presence: [0..*]
Definition: Sub-account of the safekeeping or investment account.
Impacted by: C3 "ActivityAndBalanceForSubAccount1Rule", C4
"ActivityAndBalanceForSubAccount2Rule", C38 "SubSafekeepingReportingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2881 August 2026
```

## File page 2882

```text
SubAccountDetails <SubAcctDtls> contains the following SubAccountIdentification75 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1]  2883
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 2883
Or     NameAndAddress <NmAndAdr> [1..1] ± 2883
Or}     Country <Ctry> [1..1] CodeSet C3 2884
   SafekeepingAccount <SfkpgAcct> [1..1] ± 2884
   ActivityIndicator <ActvtyInd> [1..1] Indicator 2884
   BalanceForSubAccount <BalForSubAcct> [0..*]  C7, C11,
C22
2884
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2882 August 2026
```

