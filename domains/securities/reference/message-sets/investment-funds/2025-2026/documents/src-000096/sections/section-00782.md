---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.20 RequestedTradeDate <ReqdTradDt>"]
file_pages: [1066, 1067, 1068]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.20 RequestedTradeDate <ReqdTradDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1066 to 1068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1066

```text
Definition: Date for which the instructing party requests the transfer.
Datatype: "ISODate" on page 5388
35.4.14.10.20  RequestedTradeDate <ReqdTradDt>
Presence: [0..1]
Definition: Date to be used as the trade date when securities are settled through an International
Central Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
35.4.14.10.21  RequestedSettlementDate <ReqdSttlmDt>
Presence: [0..1]
Definition: Date at which the securities are to be exchanged at the International Central Securities
Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
35.4.14.10.22  PaymentDetails <PmtDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1066 May 2026
```

## File page 1067

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1069
   CreditTransferDetails <CdtTrfDtls> [0..1]  1069
     Debtor <Dbtr> [0..1] ± 1072
     DebtorAccount <DbtrAcct> [0..1]  1072
       Name <Nm> [0..1] Text 1072
       IBAN <IBAN> [0..1] IdentifierSet C26 1072
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1073
       Other <Othr> [0..1] ± 1073
     DebtorAgent <DbtrAgt> [0..1]  1073
       BICFI <BICFI> [0..1] IdentifierSet C10 1074
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1074
       NameAndAddress <NmAndAdr> [0..1] ± 1075
       LEI <LEI> [0..1] IdentifierSet 1075
       ProprietaryIdentification <PrtryId> [0..1] Text 1076
       BranchIdentification <BrnchId> [0..1] ± 1076
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  1076
       Name <Nm> [0..1] Text 1076
       IBAN <IBAN> [0..1] IdentifierSet C26 1076
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1077
       Other <Othr> [0..1] ± 1077
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  1077
       BICFI <BICFI> [0..1] IdentifierSet C10 1078
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1078
       NameAndAddress <NmAndAdr> [0..1] ± 1079
       LEI <LEI> [0..1] IdentifierSet 1079
       ProprietaryIdentification <PrtryId> [0..1] Text 1080
       BranchIdentification <BrnchId> [0..1] ± 1080
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1080
       Name <Nm> [0..1] Text 1080
       IBAN <IBAN> [0..1] IdentifierSet C26 1080
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1067 May 2026
```

## File page 1068

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1081
       Other <Othr> [0..1] ± 1081
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  1081
       BICFI <BICFI> [0..1] IdentifierSet C10 1082
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1082
       NameAndAddress <NmAndAdr> [0..1] ± 1083
       LEI <LEI> [0..1] IdentifierSet 1083
       ProprietaryIdentification <PrtryId> [0..1] Text 1084
       BranchIdentification <BrnchId> [0..1] ± 1084
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1084
       Name <Nm> [0..1] Text 1084
       IBAN <IBAN> [0..1] IdentifierSet C26 1084
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1085
       Other <Othr> [0..1] ± 1085
     CreditorAgent <CdtrAgt> [1..1]  1085
       BICFI <BICFI> [0..1] IdentifierSet C10 1086
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1086
       NameAndAddress <NmAndAdr> [0..1] ± 1087
       LEI <LEI> [0..1] IdentifierSet 1087
       ProprietaryIdentification <PrtryId> [0..1] Text 1088
       BranchIdentification <BrnchId> [0..1] ± 1088
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  1088
       Name <Nm> [0..1] Text 1088
       IBAN <IBAN> [0..1] IdentifierSet C26 1088
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1089
       Other <Othr> [0..1] ± 1089
     Creditor <Cdtr> [0..1] ± 1089
     CreditorAccount <CdtrAcct> [1..1]  1090
       Name <Nm> [0..1] Text 1090
       IBAN <IBAN> [0..1] IdentifierSet C26 1090
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1091
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1068 May 2026
```

