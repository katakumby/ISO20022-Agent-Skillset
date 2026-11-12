---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.19 CashSettlementDetails <CshSttlmDtls>", "41.4.4.8.19.1 PaymentInstrument <PmtInstrm>", "41.4.4.8.19.1.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [1794, 1795, 1796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.19.1.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1794 to 1796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1794

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountIdentification <AcctId> [0..1] Text 1829
     Type <Tp> [0..1] ± 1829
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  1830
     Identification <Id> [1..1] Text 1830
     Type <Tp> [0..1] ± 1830
     Name <Nm> [0..1] Text 1830
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1831
41.4.4.8.19.1.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1794 May 2026
```

## File page 1795

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1797
   Debtor <Dbtr> [0..1] ± 1797
   DebtorAccount <DbtrAcct> [0..1]  1797
     Identification <Id> [1..1]  1797
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1798
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1798
Or}       Other <Othr> [1..1] ± 1798
     Name <Nm> [0..1] Text 1799
   DebtorAgent <DbtrAgt> [0..1]  1799
     Party <Pty> [1..1]  1799
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1800
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1800
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1800
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1801
     LEI <LEI> [0..1] IdentifierSet 1801
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  1802
     Identification <Id> [1..1]  1802
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1802
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1803
Or}       Other <Othr> [1..1] ± 1803
     Name <Nm> [0..1] Text 1803
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  1803
     Party <Pty> [1..1]  1804
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1804
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1804
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1805
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1806
     LEI <LEI> [0..1] IdentifierSet 1806
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1807
     Identification <Id> [1..1]  1807
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1795 May 2026
```

## File page 1796

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1807
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1808
Or}       Other <Othr> [1..1] ± 1808
     Name <Nm> [0..1] Text 1808
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  1808
     Party <Pty> [1..1]  1809
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1809
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1809
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1810
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1811
     LEI <LEI> [0..1] IdentifierSet 1811
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1812
     Identification <Id> [1..1]  1812
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1812
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1813
Or}       Other <Othr> [1..1] ± 1813
     Name <Nm> [0..1] Text 1813
   CreditorAgent <CdtrAgt> [1..1]  1813
     Party <Pty> [1..1]  1814
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1814
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1814
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1815
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1816
     LEI <LEI> [0..1] IdentifierSet 1816
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  1817
     Identification <Id> [1..1]  1817
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1817
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1818
Or}       Other <Othr> [1..1] ± 1818
     Name <Nm> [0..1] Text 1818
   Creditor <Cdtr> [0..1] ± 1818
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1796 May 2026
```

