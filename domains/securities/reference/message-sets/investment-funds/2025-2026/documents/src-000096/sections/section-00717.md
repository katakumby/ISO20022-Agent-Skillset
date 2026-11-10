---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.6 AllOtherCash <AllOthrCsh>"]
file_pages: [985, 986, 987]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.6 AllOtherCash <AllOthrCsh>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 985 to 987.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 985

```text
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
35.4.14.6  AllOtherCash <AllOthrCsh>
Presence: [0..*]
Definition: Specifies whether all remaining assets in the portfolio not listed for transfer should be
liquidated and transferred as cash.
AllOtherCash <AllOthrCsh> contains the following elements (see "AllOtherCash1" on page 4866 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4866
   Currency <Ccy> [0..1] CodeSet C1 4867
35.4.14.7  CashAll <CshAll>
Presence: [0..*]
Definition: Specifies whether all assets in the portfolio are to be liquidated and transferred as cash.
CashAll <CshAll> contains the following elements (see "CashAll1" on page 4870 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4871
   Currency <Ccy> [0..1] CodeSet C1 4871
35.4.14.8  ResidualCash <RsdlCsh>
Presence: [0..*]
Definition: Specifies how the cash in the account that is awaiting investment is to be dealt with.
ResidualCash <RsdlCsh> contains the following elements (see "ResidualCash2" on page 4854 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4854
   Currency <Ccy> [0..1] CodeSet C1 4855
35.4.14.9  PaymentDetails <PmtDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 985 May 2026
```

## File page 986

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 988
   CreditTransferDetails <CdtTrfDtls> [0..1]  988
     Debtor <Dbtr> [0..1] ± 991
     DebtorAccount <DbtrAcct> [0..1]  991
       Name <Nm> [0..1] Text 991
       IBAN <IBAN> [0..1] IdentifierSet C26 991
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 992
       Other <Othr> [0..1] ± 992
     DebtorAgent <DbtrAgt> [0..1]  992
       BICFI <BICFI> [0..1] IdentifierSet C10 993
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 993
       NameAndAddress <NmAndAdr> [0..1] ± 994
       LEI <LEI> [0..1] IdentifierSet 994
       ProprietaryIdentification <PrtryId> [0..1] Text 995
       BranchIdentification <BrnchId> [0..1] ± 995
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  995
       Name <Nm> [0..1] Text 995
       IBAN <IBAN> [0..1] IdentifierSet C26 995
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 996
       Other <Othr> [0..1] ± 996
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  996
       BICFI <BICFI> [0..1] IdentifierSet C10 997
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 997
       NameAndAddress <NmAndAdr> [0..1] ± 998
       LEI <LEI> [0..1] IdentifierSet 998
       ProprietaryIdentification <PrtryId> [0..1] Text 999
       BranchIdentification <BrnchId> [0..1] ± 999
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  999
       Name <Nm> [0..1] Text 999
       IBAN <IBAN> [0..1] IdentifierSet C26 999
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 986 May 2026
```

## File page 987

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1000
       Other <Othr> [0..1] ± 1000
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  1000
       BICFI <BICFI> [0..1] IdentifierSet C10 1001
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1001
       NameAndAddress <NmAndAdr> [0..1] ± 1002
       LEI <LEI> [0..1] IdentifierSet 1002
       ProprietaryIdentification <PrtryId> [0..1] Text 1003
       BranchIdentification <BrnchId> [0..1] ± 1003
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1003
       Name <Nm> [0..1] Text 1003
       IBAN <IBAN> [0..1] IdentifierSet C26 1003
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1004
       Other <Othr> [0..1] ± 1004
     CreditorAgent <CdtrAgt> [1..1]  1004
       BICFI <BICFI> [0..1] IdentifierSet C10 1005
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1005
       NameAndAddress <NmAndAdr> [0..1] ± 1006
       LEI <LEI> [0..1] IdentifierSet 1006
       ProprietaryIdentification <PrtryId> [0..1] Text 1007
       BranchIdentification <BrnchId> [0..1] ± 1007
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  1007
       Name <Nm> [0..1] Text 1007
       IBAN <IBAN> [0..1] IdentifierSet C26 1007
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1008
       Other <Othr> [0..1] ± 1008
     Creditor <Cdtr> [0..1] ± 1008
     CreditorAccount <CdtrAcct> [1..1]  1009
       Name <Nm> [0..1] Text 1009
       IBAN <IBAN> [0..1] IdentifierSet C26 1009
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1010
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 987 May 2026
```

