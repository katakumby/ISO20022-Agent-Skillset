---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.25 EffectiveSettlementDate <FctvSttlmDt>"]
file_pages: [1645, 1646, 1647]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.25 EffectiveSettlementDate <FctvSttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1645 to 1647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1645

```text
EffectiveTransferDate <FctvTrfDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
40.4.15.11.25  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities were exchanged at the International Central Securities
Depository (ICSD) or Central Securities Depository (CSD).
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
40.4.15.11.26  PaymentDetails <PmtDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1645 May 2026
```

## File page 1646

```text
PaymentDetails <PmtDtls> contains the following PaymentInstrument21 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1648
   CreditTransferDetails <CdtTrfDtls> [0..1]  1648
     Debtor <Dbtr> [0..1] ± 1651
     DebtorAccount <DbtrAcct> [0..1]  1651
       Name <Nm> [0..1] Text 1651
       IBAN <IBAN> [0..1] IdentifierSet C28 1651
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1652
       Other <Othr> [0..1] ± 1652
     DebtorAgent <DbtrAgt> [0..1]  1652
       BICFI <BICFI> [0..1] IdentifierSet C9 1653
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1653
       NameAndAddress <NmAndAdr> [0..1] ± 1654
       LEI <LEI> [0..1] IdentifierSet 1654
       ProprietaryIdentification <PrtryId> [0..1] Text 1655
       BranchIdentification <BrnchId> [0..1] ± 1655
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  1655
       Name <Nm> [0..1] Text 1655
       IBAN <IBAN> [0..1] IdentifierSet C28 1655
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1656
       Other <Othr> [0..1] ± 1656
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  1656
       BICFI <BICFI> [0..1] IdentifierSet C9 1657
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1657
       NameAndAddress <NmAndAdr> [0..1] ± 1658
       LEI <LEI> [0..1] IdentifierSet 1658
       ProprietaryIdentification <PrtryId> [0..1] Text 1659
       BranchIdentification <BrnchId> [0..1] ± 1659
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1659
       Name <Nm> [0..1] Text 1659
       IBAN <IBAN> [0..1] IdentifierSet C28 1659
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1646 May 2026
```

## File page 1647

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1660
       Other <Othr> [0..1] ± 1660
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  1660
       BICFI <BICFI> [0..1] IdentifierSet C9 1661
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1661
       NameAndAddress <NmAndAdr> [0..1] ± 1662
       LEI <LEI> [0..1] IdentifierSet 1662
       ProprietaryIdentification <PrtryId> [0..1] Text 1663
       BranchIdentification <BrnchId> [0..1] ± 1663
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1663
       Name <Nm> [0..1] Text 1663
       IBAN <IBAN> [0..1] IdentifierSet C28 1663
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1664
       Other <Othr> [0..1] ± 1664
     CreditorAgent <CdtrAgt> [1..1]  1664
       BICFI <BICFI> [0..1] IdentifierSet C9 1665
       ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1665
       NameAndAddress <NmAndAdr> [0..1] ± 1666
       LEI <LEI> [0..1] IdentifierSet 1666
       ProprietaryIdentification <PrtryId> [0..1] Text 1667
       BranchIdentification <BrnchId> [0..1] ± 1667
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  1667
       Name <Nm> [0..1] Text 1667
       IBAN <IBAN> [0..1] IdentifierSet C28 1667
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1668
       Other <Othr> [0..1] ± 1668
     Creditor <Cdtr> [0..1] ± 1668
     CreditorAccount <CdtrAcct> [1..1]  1669
       Name <Nm> [0..1] Text 1669
       IBAN <IBAN> [0..1] IdentifierSet C28 1669
       BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1670
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1647 May 2026
```

