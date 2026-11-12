---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.12 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "56.4.3.2.12.4 FinancialInstrumentIdentification <FinInstrmId>", "56.4.3.2.12.4.16 OtherProprietaryIdentification <OthrPrtryId>", "56.4.3.2.12.4.16.1 Identification <Id>"]
file_pages: [4173, 4174, 4175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.12.4.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4173 to 4175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4173

```text
56.4.3.2.12.4.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
56.4.3.2.12.4.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
56.4.3.2.12.5  FinancialInstrumentName <FinInstrmNm>
Presence: [0..1]
Definition: New name of the security.
Datatype: "Max350Text" on page 5403
56.4.3.2.12.6  RedemptionCompletion <RedCmpltn>
Presence: [0..1]
Definition: Specifies whether or not additional redemption order instructions are required in order for the
redemption to be completed.
Datatype: "RedemptionCompletion1Code" on page 5346
CodeName Name Definition
RED0 RedemptionNo It is not necessary to send more
redemption order instructions to the
executing party to complete the
redemption, the executing will generate
redemption confirmations automatically.
RED1 RedemptionYes Additional redemption order instructions
must be sent to the executing party order
to have the rest of the redemption
executed.
56.4.3.3  SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>
Presence: [1..*]
Definition: Status report details of a switch order.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4173 May 2026
```

## File page 4174

```text
SwitchOrderDetailsReport <SwtchOrdrDtlsRpt> contains the following
SwitchOrderStatusAndReason3 elements
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
{Or     Status <Sts> [1..1] CodeSet 4177
Or     Cancelled <Canc> [1..1] ± C3, C5 4178
Or     ConditionallyAccepted <CondlyAccptd> [1..1] ± 4179
Or     Rejected <Rjctd> [1..10]  C18 4179
       Reason <Rsn> [0..1]  4179
{Or         Code <Cd> [1..1] CodeSet 4180
Or}         Proprietary <Prtry> [1..1] ± 4182
       AdditionalInformation <AddtlInf> [0..1] Text 4183
Or     Suspended <Sspd> [1..1] ± 4183
Or     InRepair <InRpr> [1..1] ± 4183
Or}     PartiallySettled <PrtlySttld> [1..1] ± 4183
   LegInformation <LegInf> [0..*]  4184
     LegIdentification <LegId> [1..1]  4186
{Or       RedemptionLegIdentification <RedLegId> [1..1] Text 4187
Or}       SubscriptionLegIdentification <SbcptLegId> [1..1] Text 4187
     LegRejectionReason <LegRjctnRsn> [0..1] Text 4187
     RepairedFee <RprdFee> [0..10]  C6, C12 4187
       Type <Tp> [0..1]  4188
{Or         Code <Cd> [1..1] CodeSet 4188
Or}         Proprietary <Prtry> [1..1] ± 4190
       RepairedStandardAmount <RprdStdAmt> [0..1] Amount C1, C8 4190
       RepairedStandardRate <RprdStdRate> [0..1] Rate 4190
       RepairedDiscountAmount <RprdDscntAmt> [0..1] Amount C1, C8 4190
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4174 May 2026
```

## File page 4175

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       RepairedDiscountRate <RprdDscntRate> [0..1] Rate 4191
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
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4194
     FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C13 4195
       Identification <Id> [1..1]  4197
{Or         ISIN <ISIN> [1..1] IdentifierSet 4197
Or         SEDOL <SEDOL> [1..1] IdentifierSet 4198
Or         CUSIP <CUSIP> [1..1] IdentifierSet 4198
Or         RIC <RIC> [1..1] IdentifierSet 4198
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4198
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4198
Or         CTA <CTA> [1..1] IdentifierSet 4198
Or         QUICK <QUICK> [1..1] IdentifierSet 4198
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4199
Or         Dutch <Dtch> [1..1] IdentifierSet 4199
Or         Valoren <Vlrn> [1..1] IdentifierSet 4199
Or         Sicovam <SCVM> [1..1] IdentifierSet 4199
Or         Belgian <Belgn> [1..1] IdentifierSet 4199
Or         Common <Cmon> [1..1] IdentifierSet 4199
Or         DTI <DTI> [1..1] IdentifierSet 4199
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4175 May 2026
```

