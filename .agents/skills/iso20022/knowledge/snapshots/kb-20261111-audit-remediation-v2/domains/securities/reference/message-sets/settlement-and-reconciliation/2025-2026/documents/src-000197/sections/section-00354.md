---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.5.17 CurrencyToBuyOrSell <CcyToBuyOrSell>"]
file_pages: [522, 523, 524, 525, 526, 527]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.5.17 CurrencyToBuyOrSell <CcyToBuyOrSell>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 522 to 527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 522

```text
17.4.5.17  CurrencyToBuyOrSell <CcyToBuyOrSell>
Presence: [0..1]
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds
or to sell the indicated currency in order to obtain the necessary currency to fund the transaction.
CurrencyToBuyOrSell <CcyToBuyOrSell> contains one of the following elements (see
"CurrencyToBuyOrSell1Choice" on page 1568 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 1568
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 1569
17.4.5.18  MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus27Choice"
on page 1924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1924
Or}   Proprietary <Prtry> [1..1] ± 1925
17.4.5.19  AffirmationStatus <AffirmSts>
Presence: [0..1]
Definition: Status of affirmation of a trade.
AffirmationStatus <AffirmSts> contains one of the following elements (see
"AffirmationStatus8Choice" on page 1878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1878
Or}   Proprietary <Prtry> [1..1] ± 1879
17.4.5.20  FXAdditionalDetails <FxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details pertaining to foreign exchange instructions.
Datatype: "Max350Text" on page 2192
17.4.5.21  SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 522 March 2026
```

## File page 523

```text
Definition: Provides additional settlement processing information which cannot be included within the
structured fields of the message.
Datatype: "Max350Text" on page 2192
17.4.6 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C26 "DescriptionPresenceRule", C27 "DescriptionUsageRule", C34 "ISINGuideline", C35
"ISINPresenceRule", C43 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 523 March 2026
```

## File page 524

```text
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
17.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C4 "AdditionalDetailsRule", C49 "PlaceOfListingRule"
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 524 March 2026
```

## File page 525

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
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 525 March 2026
```

## File page 526

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
17.4.8 QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [1..1]
Definition: Details related to the account and quantity involved in the transaction.
Impacted by: C24 "DenominationRule", C54 "SafekeepingAccountOrBlockChainAddress1Rule", C58
"SafekeepingAccountOrBlockChainAddress2Rule", C62
"SafekeepingAccountOrBlockChainAddress3Rule", C64 "SafekeepingPlaceGuideline", C65
"SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 526 March 2026
```

## File page 527

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following QuantityAndAccount117
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± 528
   DenominationChoice <DnmtnChc> [0..1] Text 528
   AccountOwner <AcctOwnr> [0..1] ± 528
   SafekeepingAccount <SfkpgAcct> [0..1] ± 529
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 529
   CashAccount <CshAcct> [0..1] ± 529
   SafekeepingPlace <SfkpgPlc> [0..1] ± C63 530
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 530
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
• SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist between the
account servicer and the account owner, it is recommended to use the place of safekeeping field
following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and NCSD to
NCSD settlement instructions.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 527 March 2026
```

