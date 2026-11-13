---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.7.14 SettlementPartiesDetails <SttlmPtiesDtls>", "26.4.7.14.4 DeliveringSideDetails <DlvrgSdDtls>", "26.4.7.14.4.5 Party4 <Pty4>"]
file_pages: [582, 583, 584]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.7.14.4.5 Party4 <Pty4>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 582 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 582

```text
Party3 <Pty3> contains the following elements (see "PartyIdentificationAndAccount194" on page 5009
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5010
   LEI <LEI> [0..1] IdentifierSet 5010
   AlternateIdentification <AltrnId> [0..1] ± 5010
   SafekeepingAccount <SfkpgAcct> [0..1] ± 5010
   ProcessingDate <PrcgDt> [0..1] ± 5011
   ProcessingIdentification <PrcgId> [0..1] Text 5011
   AdditionalInformation <AddtlInf> [0..1] ± C4 5011
26.4.7.14.4.5  Party4 <Pty4>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the party 3.
Party4 <Pty4> contains the following elements (see "PartyIdentificationAndAccount194" on page 5009
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5010
   LEI <LEI> [0..1] IdentifierSet 5010
   AlternateIdentification <AltrnId> [0..1] ± 5010
   SafekeepingAccount <SfkpgAcct> [0..1] ± 5010
   ProcessingDate <PrcgDt> [0..1] ± 5011
   ProcessingIdentification <PrcgId> [0..1] Text 5011
   AdditionalInformation <AddtlInf> [0..1] ± C4 5011
26.4.7.14.4.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the party 4.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 582 May 2026
```

## File page 583

```text
Party5 <Pty5> contains the following elements (see "PartyIdentificationAndAccount194" on page 5009
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5010
   LEI <LEI> [0..1] IdentifierSet 5010
   AlternateIdentification <AltrnId> [0..1] ± 5010
   SafekeepingAccount <SfkpgAcct> [0..1] ± 5010
   ProcessingDate <PrcgDt> [0..1] ± 5011
   ProcessingIdentification <PrcgId> [0..1] Text 5011
   AdditionalInformation <AddtlInf> [0..1] ± C4 5011
26.4.8 SettlementDetails <SttlmDtls>
Presence: [0..1]
Definition: Information related to the receiving side of the transfer.
Impacted by: C30 "PhysicalTransferDetails1Rule", C31 "PhysicalTransferDetails2Rule"
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 583 May 2026
```

## File page 584

```text
SettlementDetails <SttlmDtls> contains the following ReceiveInformation23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Transferee <Trfee> [0..1] ± 585
   TransfereeRegisteredAccount <TrfeeRegdAcct> [0..1]  585
     Identification <Id> [0..1] Text 586
     AccountName <AcctNm> [0..1] Text 586
     Designation <Dsgnt> [0..1] Text 586
     Servicer <Svcr> [0..1] ± 586
     SubAccountDetails <SubAcctDtls> [0..1] ± 586
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 587
   IntermediaryInformation <IntrmyInf> [0..*] ± 587
   SecuritiesForm <SctiesForm> [0..1] CodeSet 587
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 588
   IncomePreference <IncmPref> [0..1] CodeSet 588
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 588
   RequestedTradeDate <ReqdTradDt> [0..1] Date 588
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 589
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 589
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 589
   StampDuty <StmpDty> [0..1] CodeSet 589
   NetAmount <NetAmt> [0..1] Amount C1, C10 590
   Fees <Fees> [0..*] ± C19 590
   IndividualTax <IndvTax> [0..*] ± 591
   ForeignExchangeDetails <FXDtls> [0..*] ± 592
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  593
     TradeTransactionCondition <TradTxCond> [0..*] ± 594
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 594
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 594
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
594
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 584 May 2026
```

