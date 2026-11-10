---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.15 SubBalanceInformation18", "82.1.5.15.5 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>"]
file_pages: [2865, 2866, 2867]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.15.5 AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2865 to 2867.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2865

```text
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown54" on
page 3111 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 3111
   LotQuantity <LotQty> [0..1] ± 3111
   LotDateTime <LotDtTm> [0..1] ± 3111
   LotPrice <LotPric> [0..1] ± 3112
   TypeOfPrice <TpOfPric> [0..1] ± 3112
82.1.5.15.5  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
Presence: [0..*]
Definition: Provides additional instrument sub-balance information on all or parts of the reported
financial instrument (unregistered, tax exempt, etc.).
Impacted by: C20 "EligibleForCollateralPurposesRule", C36 "SubBalanceAdditionalDetailsRule"
AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls> contains the following elements (see
"AdditionalBalanceInformation18" on page 2850 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 2850
   Quantity <Qty> [1..1] ± 2851
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 2851
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2851
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
82.1.5.16  Balance30
Definition: Report on the net position of a security, on a single securities account, for a certain date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2865 August 2026
```

## File page 2866

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [1..1] ± 2868
   BalanceForAccount <BalForAcct> [0..*]  C7, C11,
C22
2868
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
   SubAccountDetails <SubAcctDtls> [0..*]  C3, C4,
C38
2881
     AccountOwner <AcctOwnr> [0..1]  2883
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C2 2883
Or       NameAndAddress <NmAndAdr> [1..1] ± 2883
Or}       Country <Ctry> [1..1] CodeSet C3 2884
     SafekeepingAccount <SfkpgAcct> [1..1] ± 2884
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2866 August 2026
```

## File page 2867

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   AccountBaseCurrencyTotalAmounts
<AcctBaseCcyTtlAmts>
[0..1]  C40 2897
     TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 2897
     TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 2898
     TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 2898
     TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 2898
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2867 August 2026
```

