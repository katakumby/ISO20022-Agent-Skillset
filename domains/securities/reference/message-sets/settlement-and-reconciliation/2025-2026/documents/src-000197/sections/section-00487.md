---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>"]
file_pages: [744, 745, 746, 747, 748]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 744 to 748.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 744

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 744 March 2026
```

## File page 745

```text
Impacted by: C3 "AdditionalDetailsRule", C31 "PlaceOfListingRule"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 745 March 2026
```

## File page 746

```text
FinancialInstrumentAttributes <FinInstrmAttrbts> contains the following elements (see
"FinancialInstrumentAttributes111" on page 1445 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 1447
   DayCountBasis <DayCntBsis> [0..1] ± 1447
   RegistrationForm <RegnForm> [0..1] ± 1448
   PaymentFrequency <PmtFrqcy> [0..1] ± 1448
   PaymentStatus <PmtSts> [0..1] ± 1448
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 1448
   ClassificationType <ClssfctnTp> [0..1] ± 1449
   OptionStyle <OptnStyle> [0..1] ± 1449
   OptionType <OptnTp> [0..1] ± 1449
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 1449
   CouponDate <CpnDt> [0..1] Date 1450
   ExpiryDate <XpryDt> [0..1] Date 1450
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 1450
   MaturityDate <MtrtyDt> [0..1] Date 1450
   IssueDate <IsseDt> [0..1] Date 1450
   NextCallableDate <NxtCllblDt> [0..1] Date 1450
   PutableDate <PutblDt> [0..1] Date 1451
   DatedDate <DtdDt> [0..1] Date 1451
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1451
   PreviousFactor <PrvsFctr> [0..1] Rate 1451
   CurrentFactor <CurFctr> [0..1] Rate 1451
   NextFactor <NxtFctr> [0..1] Rate 1451
   InterestRate <IntrstRate> [0..1] Rate 1451
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 1451
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1452
   IndexRateBasis <IndxRateBsis> [0..1] Rate 1452
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 1452
   PoolNumber <PoolNb> [0..1] ± 1452
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1452
   CallableIndicator <CllblInd> [0..1] Indicator 1453
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 746 March 2026
```

## File page 747

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 1453
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 1453
   ExercisePrice <ExrcPric> [0..1] ± 1453
   SubscriptionPrice <SbcptPric> [0..1] ± 1454
   ConversionPrice <ConvsPric> [0..1] ± 1454
   StrikePrice <StrkPric> [0..1] ± 1454
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 1454
   ContractSize <CtrctSz> [0..1] ± C12 1455
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C10,
C11,
C14,
C15,
C16
1455
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 1456
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
22.4.8 QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [1..1]
Definition: Details related to the account and quantity involved in the transaction.
Impacted by: C14 "DenominationRule", C34 "SafekeepingAccountOrBlockChainAddress1Rule", C36
"SafekeepingAccountOrBlockChainAddress2Rule", C38
"SafekeepingAccountOrBlockChainAddress3Rule", C40 "SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 747 March 2026
```

## File page 748

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following elements (see
"QuantityAndAccount116" on page 1738 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1739
   DenominationChoice <DnmtnChc> [0..1] Text 1739
   AccountOwner <AcctOwnr> [0..1] ± 1740
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1740
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1740
   CashAccount <CshAcct> [0..1] ± 1740
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1741
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 1741
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in an
ICSD account versus an account at the local CSD.
22.4.9 SecuritiesFinancingDetails <SctiesFincgDtls>
Presence: [0..1]
Definition: Details of the closing of the securities financing transaction.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 748 March 2026
```

