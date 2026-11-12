---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>"]
file_pages: [893, 894, 895]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19 PaymentDetails <PmtDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 893 to 895.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 893

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
34.4.4.19  PaymentDetails <PmtDtls>
Presence: [0..*]
Definition: Details of a payment that will result from or resulting from the liquation of an asset and
transfer of cash or for the transfer of cash that was not invested.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 893 May 2026
```

## File page 894

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 896
   Amount <Amt> [1..1] Amount C1 896
   PaymentDate <PmtDt> [0..1] Date 897
   CashSettlementDetails <CshSttlmDtls> [0..1]  897
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  900
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
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 894 May 2026
```

## File page 895

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  911
         Name <Nm> [0..1] Text 911
         IBAN <IBAN> [0..1] IdentifierSet C17 911
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 912
         Other <Othr> [0..1] ± 912
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
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 895 May 2026
```

