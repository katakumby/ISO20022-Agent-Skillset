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
file_pages: [1712, 1713, 1714, 1715, 1716]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# Continuation at file page 1712

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1712 to 1716.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1712

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               Other <Othr> [1..1] ± 1820
             Name <Nm> [0..1] Text 1820
Or         ChequeDetails <ChqDtls> [1..1]  1820
           Number <Nb> [0..1] Text 1821
           PayeeIdentification <PyeeId> [1..1] ± 1821
           DraweeIdentification <DrweeId> [0..1]  1821
             Party <Pty> [1..1]  1822
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1822
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1822
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1823
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1824
             LEI <LEI> [0..1] IdentifierSet 1824
           DrawerIdentification <DrwrId> [0..1] ± 1825
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  1825
           Number <Nb> [0..1] Text 1825
           PayeeIdentification <PyeeId> [1..1] ± 1825
           DraweeIdentification <DrweeId> [0..1]  1826
             Party <Pty> [1..1]  1826
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1826
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1827
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1827
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1828
             LEI <LEI> [0..1] IdentifierSet 1828
           DrawerIdentification <DrwrId> [0..1] ± 1829
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 1829
           AccountIdentification <AcctId> [0..1] Text 1829
           Type <Tp> [0..1] ± 1829
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  1830
           Identification <Id> [1..1] Text 1830
           Type <Tp> [0..1] ± 1830
           Name <Nm> [0..1] Text 1830
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1712 May 2026
```

## File page 1713

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1831
     DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  1831
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
1831
         ISIN <ISIN> [0..1] IdentifierSet 1833
         OtherIdentification <OthrId> [0..*]  1833
           Identification <Id> [1..1] Text 1833
           Suffix <Sfx> [0..1] Text 1833
           Type <Tp> [1..1]  1833
{Or             Code <Cd> [1..1] CodeSet 1834
Or}             Proprietary <Prtry> [1..1] Text 1835
         Description <Desc> [0..1] Text 1835
       Quantity <Qty> [1..1]  1836
{Or         Quantity <Qty> [1..1] ± C15 1836
Or}         ProprietaryQuantity <PrtryQty> [1..1]  1836
           Quantity <Qty> [1..1] Quantity 1837
           QuantityType <QtyTp> [1..1] Text 1837
           Issuer <Issr> [1..1] Text 1837
           SchemeName <SchmeNm> [0..1] Text 1837
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1837
     NonStandardSettlementInformation
<NonStdSttlmInf>
[0..1] Text 1837
     StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 1837
     FinancialAdvice <FinAdvc> [0..1] CodeSet 1838
     NegotiatedTrade <NgtdTrad> [0..1] CodeSet 1838
     RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 1838
     Equalisation <Equlstn> [0..1] ± 1839
     CustomerConductClassification
<CstmrCndctClssfctn>
[0..1] ± 1839
     TransactionChannelType <TxChanlTp> [0..1] ± 1839
     SignatureType <SgntrTp> [0..1] ± 1840
     OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C38 1840
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1713 May 2026
```

## File page 1714

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 1840
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 1841
   TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 1841
   BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  1841
     PaymentInstrument <PmtInstrm> [1..1]  1845
{Or       CreditTransferDetails <CdtTrfDtls> [1..1]  1849
         Reference <Ref> [0..1] Text 1852
         Debtor <Dbtr> [0..1] ± 1852
         DebtorAccount <DbtrAcct> [0..1]  1852
           Identification <Id> [1..1]  1852
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1853
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1853
Or}             Other <Othr> [1..1] ± 1853
           Name <Nm> [0..1] Text 1854
         DebtorAgent <DbtrAgt> [0..1]  1854
           Party <Pty> [1..1]  1854
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1855
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1855
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1855
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1856
           LEI <LEI> [0..1] IdentifierSet 1856
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  1857
           Identification <Id> [1..1]  1857
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1857
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1858
Or}             Other <Othr> [1..1] ± 1858
           Name <Nm> [0..1] Text 1858
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  1858
           Party <Pty> [1..1]  1859
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1859
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1859
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1714 May 2026
```

## File page 1715

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1860
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1861
           LEI <LEI> [0..1] IdentifierSet 1861
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1862
           Identification <Id> [1..1]  1862
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1862
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1863
Or}             Other <Othr> [1..1] ± 1863
           Name <Nm> [0..1] Text 1863
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  1863
           Party <Pty> [1..1]  1864
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1864
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1864
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1865
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1866
           LEI <LEI> [0..1] IdentifierSet 1866
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1867
           Identification <Id> [1..1]  1867
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1867
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1868
Or}             Other <Othr> [1..1] ± 1868
           Name <Nm> [0..1] Text 1868
         CreditorAgent <CdtrAgt> [1..1]  1868
           Party <Pty> [1..1]  1869
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1869
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1869
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1870
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1871
           LEI <LEI> [0..1] IdentifierSet 1871
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  1872
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1715 May 2026
```

## File page 1716

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  1872
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1872
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1873
Or}             Other <Othr> [1..1] ± 1873
           Name <Nm> [0..1] Text 1873
         Creditor <Cdtr> [0..1] ± 1873
         CreditorAccount <CdtrAcct> [1..1]  1874
           Identification <Id> [1..1]  1874
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1874
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1875
Or}             Other <Othr> [1..1] ± 1875
           Name <Nm> [0..1] Text 1875
Or       ChequeDetails <ChqDtls> [1..1]  1875
         Number <Nb> [0..1] Text 1876
         PayeeIdentification <PyeeId> [1..1] ± 1876
         DraweeIdentification <DrweeId> [0..1]  1876
           Party <Pty> [1..1]  1877
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1877
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1877
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1878
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1879
           LEI <LEI> [0..1] IdentifierSet 1879
         DrawerIdentification <DrwrId> [0..1] ± 1880
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  1880
         Number <Nb> [0..1] Text 1880
         PayeeIdentification <PyeeId> [1..1] ± 1880
         DraweeIdentification <DrweeId> [0..1]  1881
           Party <Pty> [1..1]  1881
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1881
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1882
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1882
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1716 May 2026
```

