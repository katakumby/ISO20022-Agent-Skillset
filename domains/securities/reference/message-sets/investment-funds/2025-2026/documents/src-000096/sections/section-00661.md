---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.4 CashSettlementDetails <CshSttlmDtls>", "34.4.4.19.4.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [900, 901, 902]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.4.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 900 to 902.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 900

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Other <Othr> [0..1] ± 922
Or}   ChequeDetails <ChqDtls> [1..1]  922
     Number <Nb> [0..1] Text 923
     PayeeIdentification <PyeeId> [0..1] ± 923
     DraweeIdentification <DrweeId> [0..1]  923
       Party <Pty> [1..1]  924
{Or         NameAndAddress <NmAndAdr> [1..1] ± 924
Or         BICFI <BICFI> [1..1] IdentifierSet C6 924
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 925
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 926
       LEI <LEI> [0..1] IdentifierSet 926
     DrawerIdentification <DrwrId> [0..1] ± 927
34.4.4.19.4.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor that flows through one or more financial
institutions or systems.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 900 May 2026
```

## File page 901

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [0..1] ± 903
   DebtorAccount <DbtrAcct> [0..1]  903
     Name <Nm> [0..1] Text 903
     IBAN <IBAN> [0..1] IdentifierSet C17 903
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 904
     Other <Othr> [0..1] ± 904
   DebtorAgent <DbtrAgt> [0..1]  904
     BICFI <BICFI> [0..1] IdentifierSet C6 905
     ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 905
     NameAndAddress <NmAndAdr> [0..1] ± 906
     LEI <LEI> [0..1] IdentifierSet 906
     ProprietaryIdentification <PrtryId> [0..1] Text 907
     BranchIdentification <BrnchId> [0..1] ± 907
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  907
     Name <Nm> [0..1] Text 907
     IBAN <IBAN> [0..1] IdentifierSet C17 907
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 908
     Other <Othr> [0..1] ± 908
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  908
     BICFI <BICFI> [0..1] IdentifierSet C6 909
     ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 909
     NameAndAddress <NmAndAdr> [0..1] ± 910
     LEI <LEI> [0..1] IdentifierSet 910
     ProprietaryIdentification <PrtryId> [0..1] Text 911
     BranchIdentification <BrnchId> [0..1] ± 911
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  911
     Name <Nm> [0..1] Text 911
     IBAN <IBAN> [0..1] IdentifierSet C17 911
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 912
     Other <Othr> [0..1] ± 912
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 901 May 2026
```

## File page 902

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  912
     BICFI <BICFI> [0..1] IdentifierSet C6 913
     ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 913
     NameAndAddress <NmAndAdr> [0..1] ± 914
     LEI <LEI> [0..1] IdentifierSet 914
     ProprietaryIdentification <PrtryId> [0..1] Text 915
     BranchIdentification <BrnchId> [0..1] ± 915
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  915
     Name <Nm> [0..1] Text 915
     IBAN <IBAN> [0..1] IdentifierSet C17 915
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 916
     Other <Othr> [0..1] ± 916
   CreditorAgent <CdtrAgt> [1..1]  916
     BICFI <BICFI> [0..1] IdentifierSet C6 917
     ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 917
     NameAndAddress <NmAndAdr> [0..1] ± 918
     LEI <LEI> [0..1] IdentifierSet 918
     ProprietaryIdentification <PrtryId> [0..1] Text 919
     BranchIdentification <BrnchId> [0..1] ± 919
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  919
     Name <Nm> [0..1] Text 919
     IBAN <IBAN> [0..1] IdentifierSet C17 919
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 920
     Other <Othr> [0..1] ± 920
   Creditor <Cdtr> [0..1] ± 920
   CreditorAccount <CdtrAcct> [1..1]  921
     Name <Nm> [0..1] Text 921
     IBAN <IBAN> [0..1] IdentifierSet C17 921
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 922
     Other <Othr> [0..1] ± 922
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 902 May 2026
```

