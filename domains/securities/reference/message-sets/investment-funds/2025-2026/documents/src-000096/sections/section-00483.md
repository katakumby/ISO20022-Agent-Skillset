---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.8.1 OwnerIdentification <OwnrId>"]
file_pages: [661]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.8.1 OwnerIdentification <OwnrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 661 to 661.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 661

```text
AccountDetails <AcctDtls> contains the following InvestmentAccount83 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..*] ± 661
   AccountIdentification <AcctId> [1..1] Text 662
   AccountName <AcctNm> [0..1] Text 662
   AccountDesignation <AcctDsgnt> [0..1] Text 662
   AccountServicer <AcctSvcr> [0..1] ± 662
   SubAccountDetails <SubAcctDtls> [0..1] ± 662
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 663
   IntermediaryInformation <IntrmyInf> [0..*] ± 663
   SecuritiesForm <SctiesForm> [0..1] CodeSet 663
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 664
   IncomePreference <IncmPref> [0..1] CodeSet 664
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 664
   SafekeepingPlace <SfkpgPlc> [0..1] ± 664
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  665
     TradeTransactionCondition <TradTxCond> [0..*] ± 665
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 666
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 666
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
666
       Depository <Dpstry> [0..1] ± 668
       Party1 <Pty1> [0..1] ± 669
       Party2 <Pty2> [0..1] ± 669
       Party3 <Pty3> [0..1] ± 669
       Party4 <Pty4> [0..1] ± 670
       Party5 <Pty5> [0..1] ± 670
28.4.8.1  OwnerIdentification <OwnrId>
Presence: [0..*]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 661 May 2026
```

