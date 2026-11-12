---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.17 PhysicalDeliveryIndicator <PhysDlvryInd>"]
file_pages: [1786, 1787, 1788, 1789]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.17 PhysicalDeliveryIndicator <PhysDlvryInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1786 to 1789.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1786

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
41.4.4.8.17  PhysicalDeliveryIndicator <PhysDlvryInd>
Presence: [1..1]
Definition: Indicates whether the financial instrument is to be physically delivered.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
41.4.4.8.18  PhysicalDeliveryDetails <PhysDlvryDtls>
Presence: [0..1]
Definition: Information related to the physical delivery of the securities.
PhysicalDeliveryDetails <PhysDlvryDtls> contains the following elements (see
"DeliveryParameters3" on page 5096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Address <Adr> [1..1] ± 5096
   IssuedCertificateNumber <IssdCertNb> [0..1] Text 5097
41.4.4.8.19  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1786 May 2026
```

## File page 1787

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction167 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  1790
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  1794
       Reference <Ref> [0..1] Text 1797
       Debtor <Dbtr> [0..1] ± 1797
       DebtorAccount <DbtrAcct> [0..1]  1797
         Identification <Id> [1..1]  1797
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1798
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1798
Or}           Other <Othr> [1..1] ± 1798
         Name <Nm> [0..1] Text 1799
       DebtorAgent <DbtrAgt> [0..1]  1799
         Party <Pty> [1..1]  1799
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1800
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1800
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1800
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1801
         LEI <LEI> [0..1] IdentifierSet 1801
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  1802
         Identification <Id> [1..1]  1802
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1802
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1803
Or}           Other <Othr> [1..1] ± 1803
         Name <Nm> [0..1] Text 1803
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  1803
         Party <Pty> [1..1]  1804
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1804
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1804
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1805
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1806
         LEI <LEI> [0..1] IdentifierSet 1806
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1787 May 2026
```

## File page 1788

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1807
         Identification <Id> [1..1]  1807
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1807
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1808
Or}           Other <Othr> [1..1] ± 1808
         Name <Nm> [0..1] Text 1808
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  1808
         Party <Pty> [1..1]  1809
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1809
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1809
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1810
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1811
         LEI <LEI> [0..1] IdentifierSet 1811
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1812
         Identification <Id> [1..1]  1812
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1812
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1813
Or}           Other <Othr> [1..1] ± 1813
         Name <Nm> [0..1] Text 1813
       CreditorAgent <CdtrAgt> [1..1]  1813
         Party <Pty> [1..1]  1814
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1814
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1814
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1815
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1816
         LEI <LEI> [0..1] IdentifierSet 1816
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  1817
         Identification <Id> [1..1]  1817
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1817
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1818
Or}           Other <Othr> [1..1] ± 1818
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1788 May 2026
```

## File page 1789

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [0..1] Text 1818
       Creditor <Cdtr> [0..1] ± 1818
       CreditorAccount <CdtrAcct> [1..1]  1819
         Identification <Id> [1..1]  1819
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 1819
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1820
Or}           Other <Othr> [1..1] ± 1820
         Name <Nm> [0..1] Text 1820
Or     ChequeDetails <ChqDtls> [1..1]  1820
       Number <Nb> [0..1] Text 1821
       PayeeIdentification <PyeeId> [1..1] ± 1821
       DraweeIdentification <DrweeId> [0..1]  1821
         Party <Pty> [1..1]  1822
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1822
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1822
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1823
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1824
         LEI <LEI> [0..1] IdentifierSet 1824
       DrawerIdentification <DrwrId> [0..1] ± 1825
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  1825
       Number <Nb> [0..1] Text 1825
       PayeeIdentification <PyeeId> [1..1] ± 1825
       DraweeIdentification <DrweeId> [0..1]  1826
         Party <Pty> [1..1]  1826
{Or           NameAndAddress <NmAndAdr> [1..1] ± 1826
Or           BICFI <BICFI> [1..1] IdentifierSet C6 1827
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1827
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 1828
         LEI <LEI> [0..1] IdentifierSet 1828
       DrawerIdentification <DrwrId> [0..1] ± 1829
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 1829
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1789 May 2026
```

