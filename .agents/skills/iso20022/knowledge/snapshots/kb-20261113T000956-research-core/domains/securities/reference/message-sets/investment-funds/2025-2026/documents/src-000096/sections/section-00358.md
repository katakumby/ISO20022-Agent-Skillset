---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.7.14 SettlementPartiesDetails <SttlmPtiesDtls>", "24.4.7.14.4 DeliveringSideDetails <DlvrgSdDtls>", "24.4.7.14.4.5 Party4 <Pty4>"]
file_pages: [494, 495, 496]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.7.14.4.5 Party4 <Pty4>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 494 to 496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 494

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
24.4.7.14.4.5  Party4 <Pty4>
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
24.4.7.14.4.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the party 4.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 494 May 2026
```

## File page 495

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
24.4.8 SettlementDetails <SttlmDtls>
Presence: [0..1]
Definition: Information related to the receiving side of the transfer.
Impacted by: C29 "PhysicalTransferDetails1Rule", C30 "PhysicalTransferDetails2Rule"
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 495 May 2026
```

## File page 496

```text
SettlementDetails <SttlmDtls> contains the following ReceiveInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Transferee <Trfee> [0..1] ± 497
   TransfereeRegisteredAccount <TrfeeRegdAcct> [0..1]  497
     Identification <Id> [0..1] Text 498
     AccountName <AcctNm> [0..1] Text 498
     Designation <Dsgnt> [0..1] Text 498
     Servicer <Svcr> [0..1] ± 498
     SubAccountDetails <SubAcctDtls> [0..1] ± 498
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 499
   IntermediaryInformation <IntrmyInf> [0..*] ± 499
   SecuritiesForm <SctiesForm> [0..1] CodeSet 499
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 500
   IncomePreference <IncmPref> [0..1] CodeSet 500
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 500
   RequestedTradeDate <ReqdTradDt> [0..1] Date 500
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 501
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 501
   StampDuty <StmpDty> [0..1] CodeSet 501
   NetAmount <NetAmt> [0..1] Amount C1, C10 501
   Fees <Fees> [0..*] ± C18 502
   IndividualTax <IndvTax> [0..*] ± 503
   ForeignExchangeDetails <FXDtls> [0..*] ± 503
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  504
     TradeTransactionCondition <TradTxCond> [0..*] ± 505
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 505
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 506
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
506
       Depository <Dpstry> [0..1] ± 507
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 496 May 2026
```

