---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "41.4.4.12.1 PaymentInstrument <PmtInstrm>", "41.4.4.12.1.1 CreditTransferDetails <CdtTrfDtls>"]
file_pages: [1849, 1850, 1851]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.12.1.1 CreditTransferDetails <CdtTrfDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1849 to 1851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1849

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountIdentification <AcctId> [0..1] Text 1884
     Type <Tp> [0..1] ± 1884
Or}   BlockChainCashWallet <BlckChainCshWllt> [1..1]  1885
     Identification <Id> [1..1] Text 1885
     Type <Tp> [0..1] ± 1885
     Name <Nm> [0..1] Text 1885
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1886
41.4.4.12.1.1  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1849 May 2026
```

## File page 1850

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 1852
   Debtor <Dbtr> [0..1] ± 1852
   DebtorAccount <DbtrAcct> [0..1]  1852
     Identification <Id> [1..1]  1852
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1853
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1853
Or}       Other <Othr> [1..1] ± 1853
     Name <Nm> [0..1] Text 1854
   DebtorAgent <DbtrAgt> [0..1]  1854
     Party <Pty> [1..1]  1854
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1855
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1855
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1855
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1856
     LEI <LEI> [0..1] IdentifierSet 1856
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  1857
     Identification <Id> [1..1]  1857
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1857
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1858
Or}       Other <Othr> [1..1] ± 1858
     Name <Nm> [0..1] Text 1858
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  1858
     Party <Pty> [1..1]  1859
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1859
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1859
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1860
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1861
     LEI <LEI> [0..1] IdentifierSet 1861
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1862
     Identification <Id> [1..1]  1862
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1850 May 2026
```

## File page 1851

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1862
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1863
Or}       Other <Othr> [1..1] ± 1863
     Name <Nm> [0..1] Text 1863
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  1863
     Party <Pty> [1..1]  1864
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1864
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1864
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1865
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1866
     LEI <LEI> [0..1] IdentifierSet 1866
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1867
     Identification <Id> [1..1]  1867
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1867
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1868
Or}       Other <Othr> [1..1] ± 1868
     Name <Nm> [0..1] Text 1868
   CreditorAgent <CdtrAgt> [1..1]  1868
     Party <Pty> [1..1]  1869
{Or       NameAndAddress <NmAndAdr> [1..1] ± 1869
Or       BICFI <BICFI> [1..1] IdentifierSet C6 1869
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1870
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 1871
     LEI <LEI> [0..1] IdentifierSet 1871
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  1872
     Identification <Id> [1..1]  1872
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 1872
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1873
Or}       Other <Othr> [1..1] ± 1873
     Name <Nm> [0..1] Text 1873
   Creditor <Cdtr> [0..1] ± 1873
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1851 May 2026
```

