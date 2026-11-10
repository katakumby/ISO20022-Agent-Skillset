---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.26 PaymentDetails <PmtDtls>", "40.4.15.11.26.1 Reference <Ref>"]
file_pages: [1648, 1649, 1650]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.26.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1648 to 1650.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1648

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Other <Othr> [0..1] ± 1670
40.4.15.11.26.1  Reference <Ref>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer was
intended to settle, such as commercial invoices in an accounts' receivable system.
Datatype: "Max35Text" on page 5403
40.4.15.11.26.2  CreditTransferDetails <CdtTrfDtls>
Presence: [0..1]
Definition: Payment instrument between a debtor and a creditor that flows through one or more financial
institutions or systems.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1648 May 2026
```

## File page 1649

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1660
     Other <Othr> [0..1] ± 1660
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1649 May 2026
```

## File page 1650

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     Other <Othr> [0..1] ± 1670
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1650 May 2026
```

