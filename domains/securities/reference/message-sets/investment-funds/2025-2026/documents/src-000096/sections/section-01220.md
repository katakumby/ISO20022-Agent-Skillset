---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [1696, 1697, 1698]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# Continuation at file page 1696

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1696 to 1698.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1696

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C38 1840
     RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 1840
     RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 1841
     TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 1841
     BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  1841
       PaymentInstrument <PmtInstrm> [1..1]  1845
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  1849
           Reference <Ref> [0..1] Text 1852
           Debtor <Dbtr> [0..1] ± 1852
           DebtorAccount <DbtrAcct> [0..1]  1852
             Identification <Id> [1..1]  1852
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1853
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1853
Or}               Other <Othr> [1..1] ± 1853
             Name <Nm> [0..1] Text 1854
           DebtorAgent <DbtrAgt> [0..1]  1854
             Party <Pty> [1..1]  1854
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1855
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1855
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1855
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1856
             LEI <LEI> [0..1] IdentifierSet 1856
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  1857
             Identification <Id> [1..1]  1857
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1857
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1858
Or}               Other <Othr> [1..1] ± 1858
             Name <Nm> [0..1] Text 1858
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  1858
             Party <Pty> [1..1]  1859
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1859
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1696 May 2026
```

## File page 1697

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1859
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1860
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1861
             LEI <LEI> [0..1] IdentifierSet 1861
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1862
             Identification <Id> [1..1]  1862
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1862
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1863
Or}               Other <Othr> [1..1] ± 1863
             Name <Nm> [0..1] Text 1863
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  1863
             Party <Pty> [1..1]  1864
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1864
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1864
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1865
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1866
             LEI <LEI> [0..1] IdentifierSet 1866
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1867
             Identification <Id> [1..1]  1867
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1867
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1868
Or}               Other <Othr> [1..1] ± 1868
             Name <Nm> [0..1] Text 1868
           CreditorAgent <CdtrAgt> [1..1]  1868
             Party <Pty> [1..1]  1869
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1869
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1869
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1870
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1871
             LEI <LEI> [0..1] IdentifierSet 1871
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  1872
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1697 May 2026
```

## File page 1698

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Identification <Id> [1..1]  1872
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1872
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1873
Or}               Other <Othr> [1..1] ± 1873
             Name <Nm> [0..1] Text 1873
           Creditor <Cdtr> [0..1] ± 1873
           CreditorAccount <CdtrAcct> [1..1]  1874
             Identification <Id> [1..1]  1874
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1874
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1875
Or}               Other <Othr> [1..1] ± 1875
             Name <Nm> [0..1] Text 1875
Or         ChequeDetails <ChqDtls> [1..1]  1875
           Number <Nb> [0..1] Text 1876
           PayeeIdentification <PyeeId> [1..1] ± 1876
           DraweeIdentification <DrweeId> [0..1]  1876
             Party <Pty> [1..1]  1877
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1877
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1877
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1878
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1879
             LEI <LEI> [0..1] IdentifierSet 1879
           DrawerIdentification <DrwrId> [0..1] ± 1880
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  1880
           Number <Nb> [0..1] Text 1880
           PayeeIdentification <PyeeId> [1..1] ± 1880
           DraweeIdentification <DrweeId> [0..1]  1881
             Party <Pty> [1..1]  1881
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1881
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1882
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 1882
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1698 May 2026
```

