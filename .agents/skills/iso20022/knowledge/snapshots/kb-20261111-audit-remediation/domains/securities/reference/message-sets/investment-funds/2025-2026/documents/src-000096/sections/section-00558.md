---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.8 AccountDetails <AcctDtls>", "30.4.8.14 SettlementPartiesDetails <SttlmPtiesDtls>", "30.4.8.14.4 ReceivingSideDetails <RcvgSdDtls>", "30.4.8.14.4.5 Party4 <Pty4>"]
file_pages: [758, 759, 760]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.8.14.4.5 Party4 <Pty4>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 758 to 760.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 758

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
30.4.8.14.4.5  Party4 <Pty4>
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
30.4.8.14.4.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the party 4.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 758 May 2026
```

## File page 759

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
30.4.9 SettlementDetails <SttlmDtls>
Presence: [0..1]
Definition: Information related to the delivering side of the transfer.
Impacted by: C30 "PhysicalTransferDetails1Rule", C31 "PhysicalTransferDetails2Rule"
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 759 May 2026
```

## File page 760

```text
SettlementDetails <SttlmDtls> contains the following DeliverInformation23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Transferor <Trfr> [0..1] ± 761
   TransferorRegisteredAccount <TrfrRegdAcct> [0..1]  761
     Identification <Id> [0..1] Text 762
     AccountName <AcctNm> [0..1] Text 762
     Designation <Dsgnt> [0..1] Text 762
     Servicer <Svcr> [0..1] ± 762
     SubAccountDetails <SubAcctDtls> [0..1] ± 762
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 763
   IntermediaryInformation <IntrmyInf> [0..*] ± 763
   SecuritiesForm <SctiesForm> [0..1] CodeSet 763
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 764
   IncomePreference <IncmPref> [0..1] CodeSet 764
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 764
   RequestedTradeDate <ReqdTradDt> [0..1] Date 764
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 765
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 765
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 765
   StampDuty <StmpDty> [0..1] CodeSet 765
   NetAmount <NetAmt> [0..1] Amount C1, C10 766
   Fees <Fees> [0..*] ± C19 766
   IndividualTax <IndvTax> [0..*] ± 767
   ForeignExchangeDetails <FXDtls> [0..*] ± 768
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  769
     TradeTransactionCondition <TradTxCond> [0..*] ± 770
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 770
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 770
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
770
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 760 May 2026
```

