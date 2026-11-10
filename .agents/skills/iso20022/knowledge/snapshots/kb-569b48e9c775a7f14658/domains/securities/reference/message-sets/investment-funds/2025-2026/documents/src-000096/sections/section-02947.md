---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>", "56.4.3.1.3 StatusInitiator <StsInitr>"]
file_pages: [4135, 4136, 4137, 4138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.1.3 StatusInitiator <StsInitr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4135 to 4138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4135

```text
Definition: Status of all the orders in the order message is partially settled.
PartiallySettled <PrtlySttld> contains the following elements (see "PartiallySettledStatus10" on
page 5185 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5185
{Or     Code <Cd> [1..1] CodeSet 5185
Or}     Proprietary <Prtry> [1..1] ± 5186
   AdditionalInformation <AddtlInf> [0..1] Text 5186
56.4.3.1.3  StatusInitiator <StsInitr>
Presence: [0..1]
Definition: Party that initiates the status of the order.
StatusInitiator <StsInitr> contains the following elements (see "PartyIdentification139" on page 5043
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
56.4.3.2  IndividualOrderDetailsReport <IndvOrdrDtlsRpt>
Presence: [1..*]
Definition: Status report details of an individual order.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4135 May 2026
```

## File page 4136

```text
IndividualOrderDetailsReport <IndvOrdrDtlsRpt> contains the following
IndividualOrderStatusAndReason9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 4139
   OrderReference <OrdrRef> [1..1] Text 4139
   ClientReference <ClntRef> [0..1] Text 4139
   DealReference <DealRef> [0..1] Text 4139
   NonceIdentification <NonceId> [0..1] Text 4140
   CancellationReference <CxlRef> [0..1] Text 4140
   OrderStatus <OrdrSts> [1..1]  4140
{Or     Status <Sts> [1..1] CodeSet 4140
Or     Cancelled <Canc> [1..1] ± C3, C5 4141
Or     ConditionallyAccepted <CondlyAccptd> [1..1] ± 4142
Or     Rejected <Rjctd> [1..10]  C18 4142
       Reason <Rsn> [0..1]  4143
{Or         Code <Cd> [1..1] CodeSet 4143
Or}         Proprietary <Prtry> [1..1] ± 4145
       AdditionalInformation <AddtlInf> [0..1] Text 4146
Or     Suspended <Sspd> [1..1] ± 4146
Or     InRepair <InRpr> [1..1] ± 4146
Or}     PartiallySettled <PrtlySttld> [1..1] ± 4147
   RepairedFee <RprdFee> [0..10]  C6, C12 4147
     Type <Tp> [0..1]  4148
{Or       Code <Cd> [1..1] CodeSet 4148
Or}       Proprietary <Prtry> [1..1] ± 4150
     RepairedStandardAmount <RprdStdAmt> [0..1] Amount C1, C8 4150
     RepairedStandardRate <RprdStdRate> [0..1] Rate 4150
     RepairedDiscountAmount <RprdDscntAmt> [0..1] Amount C1, C8 4150
     RepairedDiscountRate <RprdDscntRate> [0..1] Rate 4151
     RepairedRequestedAmount <RprdReqdAmt> [0..1] Amount C1, C8 4151
     RepairedRequestedRate <RprdReqdRate> [0..1] Rate 4151
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 4152
     NewCommercialAgreementReferenceIndicator
<NewComrclAgrmtRefInd>
[0..1] Indicator 4152
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4136 May 2026
```

## File page 4137

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4157
     FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C13 4157
       Identification <Id> [1..1]  4159
{Or         ISIN <ISIN> [1..1] IdentifierSet 4159
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4160
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4160
Or         RIC <RIC> [1..1] IdentifierSet 4160
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4160
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4160
Or         CTA <CTA> [1..1] IdentifierSet 4160
Or         QUICK <QUICK> [1..1] IdentifierSet 4160
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4161
Or         Dutch <Dtch> [1..1] IdentifierSet 4161
Or         Valoren <Vlrn> [1..1] IdentifierSet 4161
Or         Sicovam <SCVM> [1..1] IdentifierSet 4161
Or         Belgian <Belgn> [1..1] IdentifierSet 4161
Or         Common <Cmon> [1..1] IdentifierSet 4161
Or         DTI <DTI> [1..1] IdentifierSet 4161
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  4161
           Identification <Id> [1..1] Text 4162
           IdentificationSource <IdSrc> [1..1] ± 4162
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4137 May 2026
```

## File page 4138

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       ISIN <ISIN> [1..1] IdentifierSet 4170
Or       SEDOL <SEDOL> [1..1] IdentifierSet 4170
Or       CUSIP <CUSIP> [1..1] IdentifierSet 4171
Or       RIC <RIC> [1..1] IdentifierSet 4171
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 4171
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4138 May 2026
```

