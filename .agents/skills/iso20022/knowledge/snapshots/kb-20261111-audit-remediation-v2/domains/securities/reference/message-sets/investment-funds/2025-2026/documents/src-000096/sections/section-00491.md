---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.8.14 SettlementPartiesDetails <SttlmPtiesDtls>", "28.4.8.14.4 ReceivingSideDetails <RcvgSdDtls>", "28.4.8.14.4.5 Party4 <Pty4>"]
file_pages: [670, 671, 672]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.8.14.4.5 Party4 <Pty4>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 670 to 672.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 670

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
28.4.8.14.4.5  Party4 <Pty4>
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
28.4.8.14.4.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the party 4.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 670 May 2026
```

## File page 671

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
28.4.9 SettlementDetails <SttlmDtls>
Presence: [0..1]
Definition: Information related to the delivering side of the transfer.
Impacted by: C29 "PhysicalTransferDetails1Rule", C30 "PhysicalTransferDetails2Rule"
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 671 May 2026
```

## File page 672

```text
SettlementDetails <SttlmDtls> contains the following DeliverInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Transferor <Trfr> [0..1] ± 673
   TransferorRegisteredAccount <TrfrRegdAcct> [0..1]  673
     Identification <Id> [0..1] Text 674
     AccountName <AcctNm> [0..1] Text 674
     Designation <Dsgnt> [0..1] Text 674
     Servicer <Svcr> [0..1] ± 674
     SubAccountDetails <SubAcctDtls> [0..1] ± 674
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 675
   IntermediaryInformation <IntrmyInf> [0..*] ± 675
   SecuritiesForm <SctiesForm> [0..1] CodeSet 675
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 676
   IncomePreference <IncmPref> [0..1] CodeSet 676
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 676
   RequestedTradeDate <ReqdTradDt> [0..1] Date 676
   RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 677
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 677
   StampDuty <StmpDty> [0..1] CodeSet 677
   NetAmount <NetAmt> [0..1] Amount C1, C10 677
   Fees <Fees> [0..*] ± C18 678
   IndividualTax <IndvTax> [0..*] ± 679
   ForeignExchangeDetails <FXDtls> [0..*] ± 679
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  680
     TradeTransactionCondition <TradTxCond> [0..*] ± 681
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 681
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 682
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
682
       Depository <Dpstry> [0..1] ± 683
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 672 May 2026
```

