---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.8 AccountDetails <AcctDtls>", "30.4.8.1 OwnerIdentification <OwnrId>"]
file_pages: [749]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.8.1 OwnerIdentification <OwnrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 749 to 749.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 749

```text
AccountDetails <AcctDtls> contains the following InvestmentAccount83 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [0..*] ± 749
   AccountIdentification <AcctId> [1..1] Text 750
   AccountName <AcctNm> [0..1] Text 750
   AccountDesignation <AcctDsgnt> [0..1] Text 750
   AccountServicer <AcctSvcr> [0..1] ± 750
   SubAccountDetails <SubAcctDtls> [0..1] ± 750
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 751
   IntermediaryInformation <IntrmyInf> [0..*] ± 751
   SecuritiesForm <SctiesForm> [0..1] CodeSet 751
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 752
   IncomePreference <IncmPref> [0..1] CodeSet 752
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 752
   SafekeepingPlace <SfkpgPlc> [0..1] ± 752
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  753
     TradeTransactionCondition <TradTxCond> [0..*] ± 753
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 754
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 754
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
754
       Depository <Dpstry> [0..1] ± 756
       Party1 <Pty1> [0..1] ± 757
       Party2 <Pty2> [0..1] ± 757
       Party3 <Pty3> [0..1] ± 757
       Party4 <Pty4> [0..1] ± 758
       Party5 <Pty5> [0..1] ± 758
30.4.8.1  OwnerIdentification <OwnrId>
Presence: [0..*]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 749 May 2026
```

