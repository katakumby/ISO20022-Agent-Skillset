---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.7.1 OwnerIdentification <OwnrId>"]
file_pages: [485]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.7.1 OwnerIdentification <OwnrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 485 to 485.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 485

```text
AccountDetails <AcctDtls> contains the following InvestmentAccount82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..*] ± 485
   AccountIdentification <AcctId> [1..1] Text 486
   AccountName <AcctNm> [0..1] Text 486
   AccountDesignation <AcctDsgnt> [0..1] Text 486
   AccountServicer <AcctSvcr> [0..1] ± 486
   SubAccountDetails <SubAcctDtls> [0..1] ± 486
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 487
   IntermediaryInformation <IntrmyInf> [0..*] ± 487
   SecuritiesForm <SctiesForm> [0..1] CodeSet 487
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 488
   IncomePreference <IncmPref> [0..1] CodeSet 488
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 488
   SafekeepingPlace <SfkpgPlc> [0..1] ± 488
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  489
     TradeTransactionCondition <TradTxCond> [0..*] ± 489
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 490
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 490
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
490
       Depository <Dpstry> [0..1] ± 492
       Party1 <Pty1> [0..1] ± 493
       Party2 <Pty2> [0..1] ± 493
       Party3 <Pty3> [0..1] ± 493
       Party4 <Pty4> [0..1] ± 494
       Party5 <Pty5> [0..1] ± 494
24.4.7.1  OwnerIdentification <OwnrId>
Presence: [0..*]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 485 May 2026
```

