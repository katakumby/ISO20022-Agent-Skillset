---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks"]
file_pages: [4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C14", "C15", "C16", "C17", "C18", "C19", "C20"], "until_heading": "56.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 4119, "topic": "56.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02939.md"}]
---

# 56.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4119 to 4126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 4119, C14–C20 before **56.4 Message Building Blocks** continue [56.3 Constraints](section-02939.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 4119

```text
C14 MessageNameAndReferenceGuideline
If Reference/RelatedReference/MessageName or Reference/OtherReference/MessageName is
present, it must contain 502 or must start with setr.001, setr.004, setr.007, setr.010, setr.013,
setr.019 or setr.018 and Reference/RelatedReference/Reference must contain the message
reference of a message in this list.
This constraint is defined at the MessageDefinition level.
C15 OrderDataElementRule
One of the elements (InvestmentAccountDetails, FinancialInstrumentDetails, UnitsNumber,
NetAmount, GrossAmount, HoldingsRedemptionRate, SettlementAmount, UnitCurrency,
QuotedCurrency) must be present.
C16 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C17 OtherReferenceGuideline
Reference/OtherReference should be used to reference an order instruction sent in a
proprietary way or used for a system reference. If Reference/OtherReference is present,
Reference/OtherReference/MessageName must contain 'fax' or 'phone' or 'email', etc.
This constraint is defined at the MessageDefinition level.
C18 RejectedElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
C19 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C20 SwitchOrderDataElementRule
One of the elements (SettlementAmount, SettlementMethod, AdditionalAmount, UnitCurrency,
QuotedCurrency) must be present.
56.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
56.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4119 May 2026
```

## File page 4120

```text
56.4.2 Reference <Ref>
Presence: [0..1]
Definition: Reference to the message or communication that was previously received.
Reference <Ref> contains one of the following elements (see "References64Choice" on page 4551 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RelatedReference <RltdRef> [1..2] ± 4551
Or}   OtherReference <OthrRef> [1..2] ± 4551
56.4.3 StatusReport <StsRpt>
Presence: [1..1]
Definition: Status of the order.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4120 May 2026
```

## File page 4121

```text
StatusReport <StsRpt> contains one of the following Status40Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrderDetailsReport <OrdrDtlsRpt> [1..1]  4127
     MasterReference <MstrRef> [0..1] Text 4128
     OrderStatus <OrdrSts> [1..1]  4128
{Or       Status <Sts> [1..1] CodeSet 4129
Or       Cancelled <Canc> [1..1] ± C3, C5 4130
Or       ConditionallyAccepted <CondlyAccptd> [1..1] ± 4130
Or       Rejected <Rjctd> [1..10]  C18 4131
         Reason <Rsn> [0..1]  4131
{Or           Code <Cd> [1..1] CodeSet 4131
Or}           Proprietary <Prtry> [1..1] ± 4134
         AdditionalInformation <AddtlInf> [0..1] Text 4134
Or       Suspended <Sspd> [1..1] ± 4134
Or}       PartiallySettled <PrtlySttld> [1..1] ± 4134
     StatusInitiator <StsInitr> [0..1] ± 4135
Or   IndividualOrderDetailsReport <IndvOrdrDtlsRpt> [1..*]  4135
     MasterReference <MstrRef> [0..1] Text 4139
     OrderReference <OrdrRef> [1..1] Text 4139
     ClientReference <ClntRef> [0..1] Text 4139
     DealReference <DealRef> [0..1] Text 4139
     NonceIdentification <NonceId> [0..1] Text 4140
     CancellationReference <CxlRef> [0..1] Text 4140
     OrderStatus <OrdrSts> [1..1]  4140
{Or       Status <Sts> [1..1] CodeSet 4140
Or       Cancelled <Canc> [1..1] ± C3, C5 4141
Or       ConditionallyAccepted <CondlyAccptd> [1..1] ± 4142
Or       Rejected <Rjctd> [1..10]  C18 4142
         Reason <Rsn> [0..1]  4143
{Or           Code <Cd> [1..1] CodeSet 4143
Or}           Proprietary <Prtry> [1..1] ± 4145
         AdditionalInformation <AddtlInf> [0..1] Text 4146
Or       Suspended <Sspd> [1..1] ± 4146
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4121 May 2026
```

## File page 4122

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       InRepair <InRpr> [1..1] ± 4146
Or}       PartiallySettled <PrtlySttld> [1..1] ± 4147
     RepairedFee <RprdFee> [0..10]  C6, C12 4147
       Type <Tp> [0..1]  4148
{Or         Code <Cd> [1..1] CodeSet 4148
Or}         Proprietary <Prtry> [1..1] ± 4150
       RepairedStandardAmount <RprdStdAmt> [0..1] Amount C1, C8 4150
       RepairedStandardRate <RprdStdRate> [0..1] Rate 4150
       RepairedDiscountAmount <RprdDscntAmt> [0..1] Amount C1, C8 4150
       RepairedDiscountRate <RprdDscntRate> [0..1] Rate 4151
       RepairedRequestedAmount <RprdReqdAmt> [0..1] Amount C1, C8 4151
       RepairedRequestedRate <RprdReqdRate> [0..1] Rate 4151
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 4152
       NewCommercialAgreementReferenceIndicator
<NewComrclAgrmtRefInd>
[0..1] Indicator 4152
     StatusInitiator <StsInitr> [0..1] ± 4152
     OrderData <OrdrData> [0..1]  C15 4152
       InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C16 4154
         AccountIdentification <AcctId> [1..1] Text 4155
         AccountName <AcctNm> [0..1] Text 4155
         AccountDesignation <AcctDsgnt> [0..1] Text 4155
         OwnerIdentification <OwnrId> [0..*] ± 4155
         AccountServicer <AcctSvcr> [0..1] ± 4156
         OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4156
         SubAccountDetails <SubAcctDtls> [0..1] ± 4156
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 4157
       FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C13 4157
         Identification <Id> [1..1]  4159
{Or           ISIN <ISIN> [1..1] IdentifierSet 4159
Or           SEDOL <SEDOL> [1..1] IdentifierSet 4160
Or           CUSIP <CUSIP> [1..1] IdentifierSet 4160
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4122 May 2026
```

## File page 4123

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           RIC <RIC> [1..1] IdentifierSet 4160
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 4160
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 4160
Or           CTA <CTA> [1..1] IdentifierSet 4160
Or           QUICK <QUICK> [1..1] IdentifierSet 4160
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 4161
Or           Dutch <Dtch> [1..1] IdentifierSet 4161
Or           Valoren <Vlrn> [1..1] IdentifierSet 4161
Or           Sicovam <SCVM> [1..1] IdentifierSet 4161
Or           Belgian <Belgn> [1..1] IdentifierSet 4161
Or           Common <Cmon> [1..1] IdentifierSet 4161
Or           DTI <DTI> [1..1] IdentifierSet 4161
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  4161
             Identification <Id> [1..1] Text 4162
             IdentificationSource <IdSrc> [1..1] ± 4162
         Name <Nm> [0..1] Text 4162
         ShortName <ShrtNm> [0..1] Text 4162
         SupplementaryIdentification <SplmtryId> [0..1] Text 4162
         ClassType <ClssTp> [0..1] Text 4162
         SecuritiesForm <SctiesForm> [0..1] CodeSet 4163
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4163
         ProductGroup <PdctGrp> [0..1] Text 4163
         SeriesIdentification <SrsId> [0..1]  C19 4163
           SeriesDate <SrsDt> [0..1] ± 4164
           SeriesName <SrsNm> [0..1] Text 4164
       UnitsNumber <UnitsNb> [0..1] Quantity 4164
       DigitalTokenUnit <DgtlTknUnit> [0..1] Quantity 4164
       NetAmount <NetAmt> [0..1] Amount C2, C9 4164
       GrossAmount <GrssAmt> [0..1] Amount C2, C9 4165
       HoldingsRedemptionRate <HldgsRedRate> [0..1] Rate 4165
       SettlementAmount <SttlmAmt> [0..1] Amount C1, C8 4165
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4123 May 2026
```

## File page 4124

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       UnitCurrency <UnitCcy> [0..1] CodeSet C1 4166
       QuotedCurrency <QtdCcy> [0..1] CodeSet C1 4166
     NewDetails <NewDtls> [0..1]  C10 4167
       ExpectedTradeDateTime <XpctdTradDtTm> [0..1] ± 4167
       ExpectedCashSettlementDate <XpctdCshSttlmDt> [0..1] Date 4167
     GatingOrHoldBackDetails <GtgOrHldBckDtls> [0..1]  4167
       Type <Tp> [1..1] CodeSet 4168
       Amount <Amt> [0..1] Amount C1, C8 4169
       ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 4169
       FinancialInstrumentIdentification <FinInstrmId> [0..1]  4169
{Or         ISIN <ISIN> [1..1] IdentifierSet 4170
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4170
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4171
Or         RIC <RIC> [1..1] IdentifierSet 4171
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4171
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4171
Or         CTA <CTA> [1..1] IdentifierSet 4171
Or         QUICK <QUICK> [1..1] IdentifierSet 4171
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4171
Or         Dutch <Dtch> [1..1] IdentifierSet 4172
Or         Valoren <Vlrn> [1..1] IdentifierSet 4172
Or         Sicovam <SCVM> [1..1] IdentifierSet 4172
Or         Belgian <Belgn> [1..1] IdentifierSet 4172
Or         Common <Cmon> [1..1] IdentifierSet 4172
Or         DTI <DTI> [1..1] IdentifierSet 4172
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  4172
           Identification <Id> [1..1] Text 4173
           IdentificationSource <IdSrc> [1..1] ± 4173
       FinancialInstrumentName <FinInstrmNm> [0..1] Text 4173
       RedemptionCompletion <RedCmpltn> [0..1] CodeSet 4173
Or}   SwitchOrderDetailsReport <SwtchOrdrDtlsRpt> [1..*]  4173
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4124 May 2026
```

## File page 4125

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     MasterReference <MstrRef> [0..1] Text 4176
     OrderReference <OrdrRef> [1..1] Text 4176
     ClientReference <ClntRef> [0..1] Text 4176
     DealReference <DealRef> [0..1] Text 4177
     NonceIdentification <NonceId> [0..1] Text 4177
     CancellationReference <CxlRef> [0..1] Text 4177
     OrderStatus <OrdrSts> [1..1]  4177
{Or       Status <Sts> [1..1] CodeSet 4177
Or       Cancelled <Canc> [1..1] ± C3, C5 4178
Or       ConditionallyAccepted <CondlyAccptd> [1..1] ± 4179
Or       Rejected <Rjctd> [1..10]  C18 4179
         Reason <Rsn> [0..1]  4179
{Or           Code <Cd> [1..1] CodeSet 4180
Or}           Proprietary <Prtry> [1..1] ± 4182
         AdditionalInformation <AddtlInf> [0..1] Text 4183
Or       Suspended <Sspd> [1..1] ± 4183
Or       InRepair <InRpr> [1..1] ± 4183
Or}       PartiallySettled <PrtlySttld> [1..1] ± 4183
     LegInformation <LegInf> [0..*]  4184
       LegIdentification <LegId> [1..1]  4186
{Or         RedemptionLegIdentification <RedLegId> [1..1] Text 4187
Or}         SubscriptionLegIdentification <SbcptLegId> [1..1] Text 4187
       LegRejectionReason <LegRjctnRsn> [0..1] Text 4187
       RepairedFee <RprdFee> [0..10]  C6, C12 4187
         Type <Tp> [0..1]  4188
{Or           Code <Cd> [1..1] CodeSet 4188
Or}           Proprietary <Prtry> [1..1] ± 4190
         RepairedStandardAmount <RprdStdAmt> [0..1] Amount C1, C8 4190
         RepairedStandardRate <RprdStdRate> [0..1] Rate 4190
         RepairedDiscountAmount <RprdDscntAmt> [0..1] Amount C1, C8 4190
         RepairedDiscountRate <RprdDscntRate> [0..1] Rate 4191
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4125 May 2026
```

## File page 4126

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RepairedRequestedAmount <RprdReqdAmt> [0..1] Amount C1, C8 4191
         RepairedRequestedRate <RprdReqdRate> [0..1] Rate 4191
         CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 4192
         NewCommercialAgreementReferenceIndicator
<NewComrclAgrmtRefInd>
[0..1] Indicator 4192
       InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C16 4192
         AccountIdentification <AcctId> [1..1] Text 4193
         AccountName <AcctNm> [0..1] Text 4193
         AccountDesignation <AcctDsgnt> [0..1] Text 4193
         OwnerIdentification <OwnrId> [0..*] ± 4193
         AccountServicer <AcctSvcr> [0..1] ± 4193
         OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4194
         SubAccountDetails <SubAcctDtls> [0..1] ± 4194
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 4194
       FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C13 4195
         Identification <Id> [1..1]  4197
{Or           ISIN <ISIN> [1..1] IdentifierSet 4197
Or           SEDOL <SEDOL> [1..1] IdentifierSet 4198
Or           CUSIP <CUSIP> [1..1] IdentifierSet 4198
Or           RIC <RIC> [1..1] IdentifierSet 4198
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 4198
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 4198
Or           CTA <CTA> [1..1] IdentifierSet 4198
Or           QUICK <QUICK> [1..1] IdentifierSet 4198
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 4199
Or           Dutch <Dtch> [1..1] IdentifierSet 4199
Or           Valoren <Vlrn> [1..1] IdentifierSet 4199
Or           Sicovam <SCVM> [1..1] IdentifierSet 4199
Or           Belgian <Belgn> [1..1] IdentifierSet 4199
Or           Common <Cmon> [1..1] IdentifierSet 4199
Or           DTI <DTI> [1..1] IdentifierSet 4199
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4126 May 2026
```

