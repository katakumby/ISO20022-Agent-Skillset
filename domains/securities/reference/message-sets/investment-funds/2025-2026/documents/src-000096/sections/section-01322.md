---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.10 RequestedNAVCurrency <ReqdNAVCcy>"]
file_pages: [1841, 1842, 1843, 1844]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.10 RequestedNAVCurrency <ReqdNAVCcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1841 to 1844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1841

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
41.4.4.10  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C4 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
41.4.4.11  TotalSettlementAmount <TtlSttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the multiple order.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
41.4.4.12  BulkCashSettlementDetails <BlkCshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1841 May 2026
```

## File page 1842

```text
BulkCashSettlementDetails <BlkCshSttlmDtls> contains the following PaymentTransaction167
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  1845
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  1849
       Reference <Ref> [0..1] Text 1852
       Debtor <Dbtr> [0..1] ± 1852
       DebtorAccount <DbtrAcct> [0..1]  1852
         Identification <Id> [1..1]  1852
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1853
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1853
Or}           Other <Othr> [1..1] ± 1853
         Name <Nm> [0..1] Text 1854
       DebtorAgent <DbtrAgt> [0..1]  1854
         Party <Pty> [1..1]  1854
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1855
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1855
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1855
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1856
         LEI <LEI> [0..1] IdentifierSet 1856
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  1857
         Identification <Id> [1..1]  1857
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1857
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1858
Or}           Other <Othr> [1..1] ± 1858
         Name <Nm> [0..1] Text 1858
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  1858
         Party <Pty> [1..1]  1859
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1859
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1859
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1860
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1861
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1842 May 2026
```

## File page 1843

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         LEI <LEI> [0..1] IdentifierSet 1861
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1862
         Identification <Id> [1..1]  1862
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1862
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1863
Or}           Other <Othr> [1..1] ± 1863
         Name <Nm> [0..1] Text 1863
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  1863
         Party <Pty> [1..1]  1864
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1864
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1864
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1865
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1866
         LEI <LEI> [0..1] IdentifierSet 1866
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1867
         Identification <Id> [1..1]  1867
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1867
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1868
Or}           Other <Othr> [1..1] ± 1868
         Name <Nm> [0..1] Text 1868
       CreditorAgent <CdtrAgt> [1..1]  1868
         Party <Pty> [1..1]  1869
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1869
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1869
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1870
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1871
         LEI <LEI> [0..1] IdentifierSet 1871
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  1872
         Identification <Id> [1..1]  1872
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1872
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1873
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1843 May 2026
```

## File page 1844

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Other <Othr> [1..1] ± 1873
         Name <Nm> [0..1] Text 1873
       Creditor <Cdtr> [0..1] ± 1873
       CreditorAccount <CdtrAcct> [1..1]  1874
         Identification <Id> [1..1]  1874
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1874
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1875
Or}           Other <Othr> [1..1] ± 1875
         Name <Nm> [0..1] Text 1875
Or     ChequeDetails <ChqDtls> [1..1]  1875
       Number <Nb> [0..1] Text 1876
       PayeeIdentification <PyeeId> [1..1] ± 1876
       DraweeIdentification <DrweeId> [0..1]  1876
         Party <Pty> [1..1]  1877
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1877
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1877
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1878
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1879
         LEI <LEI> [0..1] IdentifierSet 1879
       DrawerIdentification <DrwrId> [0..1] ± 1880
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  1880
       Number <Nb> [0..1] Text 1880
       PayeeIdentification <PyeeId> [1..1] ± 1880
       DraweeIdentification <DrweeId> [0..1]  1881
         Party <Pty> [1..1]  1881
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1881
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1882
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1882
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1883
         LEI <LEI> [0..1] IdentifierSet 1883
       DrawerIdentification <DrwrId> [0..1] ± 1884
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1844 May 2026
```

