---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.2 Linkages <Lnkgs>", "19.4.4.17 FXAdditionalDetails <FxAddtlDtls>"]
file_pages: [621, 622, 623, 624, 625]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.4.17 FXAdditionalDetails <FxAddtlDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 621 to 625.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 621

```text
19.4.4.17  FXAdditionalDetails <FxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details pertaining to foreign exchange instructions.
Datatype: "Max350Text" on page 2192
19.4.4.18  SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
Presence: [0..1]
Definition: Provides additional settlement processing information which cannot be included within the
structured fields of the message.
Datatype: "Max350Text" on page 2192
19.4.5 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C18 "DescriptionPresenceRule", C19 "DescriptionUsageRule", C25 "ISINGuideline", C26
"ISINPresenceRule", C31 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 621 March 2026
```

## File page 622

```text
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
19.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [0..1]
Definition: Elements characterising a financial instrument.
Impacted by: C4 "AdditionalDetailsRule", C38 "PlaceOfListingRule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 622 March 2026
```

## File page 623

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
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 623 March 2026
```

## File page 624

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
19.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [1..1]
Definition: Details related to the account and quantity involved in the transaction.
Impacted by: C16 "DenominationRule", C33 "PartialSettlementGuideline", C42
"SafekeepingAccountOrBlockChainAddress1Rule", C46
"SafekeepingAccountOrBlockChainAddress2Rule", C50
"SafekeepingAccountOrBlockChainAddress3Rule", C52 "SafekeepingPlaceGuideline", C53
"SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 624 March 2026
```

## File page 625

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following QuantityAndAccount115
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettledQuantity <SttldQty> [1..1] ± 626
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C20 626
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C20 627
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 627
   RemainingToBeSettledAmount <RmngToBeSttldAmt> [0..1] ± 628
   DenominationChoice <DnmtnChc> [0..1] Text 628
   AccountOwner <AcctOwnr> [0..1] ± 628
   SafekeepingAccount <SfkpgAcct> [0..1] ± 628
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 629
   CashAccount <CshAcct> [0..1] ± 629
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 629
   SafekeepingPlace <SfkpgPlc> [0..1] ± C51 630
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• PartialSettlementGuideline
Partial settlement information only applies to markets where partial settlement is allowed.
The SettledQuantity field provides the quantity of securities effectively settled.
The other quantities (PreviouslySettledQuantity and/or RemainingToBeSettledQuantity) may be
provided, but this is not mandatory.
For more details, see the relevant market practice document on www.smpg.info.
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
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 625 March 2026
```

