---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.7.1 OwnerIdentification <OwnrId>"]
file_pages: [573]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.7.1 OwnerIdentification <OwnrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 573 to 573.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 573

```text
AccountDetails <AcctDtls> contains the following InvestmentAccount82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..*] ± 573
   AccountIdentification <AcctId> [1..1] Text 574
   AccountName <AcctNm> [0..1] Text 574
   AccountDesignation <AcctDsgnt> [0..1] Text 574
   AccountServicer <AcctSvcr> [0..1] ± 574
   SubAccountDetails <SubAcctDtls> [0..1] ± 574
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 575
   IntermediaryInformation <IntrmyInf> [0..*] ± 575
   SecuritiesForm <SctiesForm> [0..1] CodeSet 575
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 576
   IncomePreference <IncmPref> [0..1] CodeSet 576
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 576
   SafekeepingPlace <SfkpgPlc> [0..1] ± 576
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  577
     TradeTransactionCondition <TradTxCond> [0..*] ± 577
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 578
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 578
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
578
       Depository <Dpstry> [0..1] ± 580
       Party1 <Pty1> [0..1] ± 581
       Party2 <Pty2> [0..1] ± 581
       Party3 <Pty3> [0..1] ± 581
       Party4 <Pty4> [0..1] ± 582
       Party5 <Pty5> [0..1] ± 582
26.4.7.1  OwnerIdentification <OwnrId>
Presence: [0..*]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 573 May 2026
```

