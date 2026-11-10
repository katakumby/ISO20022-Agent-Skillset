---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.7 FinancialInstrumentDetails <FinInstrmDtls>", "41.4.4.7.9 SeriesIdentification <SrsId>", "41.4.4.7.9.1 SeriesDate <SrsDt>"]
file_pages: [1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.7.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1726 to 1735.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1726

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
41.4.4.7.9.1  SeriesDate <SrsDt>
Presence: [0..1]
Definition: Issue date of the fund series. It is typically applicable to a redemption order, subscription
order confirmation or redemption order confirmation, but may be specified in the subscription order, if
known.
SeriesDate <SrsDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
41.4.4.7.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
41.4.4.8  IndividualOrderDetails <IndvOrdrDtls>
Presence: [1..*]
Definition: Instruction from an investor to sell investment fund units back to the fund.
Impacted by: C26 "OrderOriginatorEligibility3Rule", C29 "PhysicalDeliveryDetails1Rule", C30
"PhysicalDeliveryDetails2Rule"
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1726 May 2026
```

## File page 1727

```text
IndividualOrderDetails <IndvOrdrDtls> contains the following RedemptionOrder17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [1..1] Text 1736
   ClientReference <ClntRef> [0..1] Text 1736
   NonceIdentification <NonceId> [0..1] Text 1736
   InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 1736
     AccountIdentification <AcctId> [1..1] Text 1737
     AccountName <AcctNm> [0..1] Text 1737
     AccountDesignation <AcctDsgnt> [0..1] Text 1737
     OwnerIdentification <OwnrId> [0..*] ± 1737
     AccountServicer <AcctSvcr> [0..1] ± 1738
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 1738
     SubAccountDetails <SubAcctDtls> [0..1] ± 1738
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1739
   OrderType <OrdrTp> [0..10] ± 1739
   BeneficiaryDetails <BnfcryDtls> [0..*] ± C28 1739
   AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg> [1..1]  1740
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1740
Or     GrossAmount <GrssAmt> [1..1] Amount C4, C9 1741
Or     NetAmount <NetAmt> [1..1] Amount C4, C9 1741
Or     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1741
Or}     HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 1742
   Rounding <Rndg> [0..1] CodeSet 1742
   SettlementAmount <SttlmAmt> [0..1] Amount C3, C10 1742
   CashSettlementDate <CshSttlmDt> [0..1] Date 1742
   SettlementMethod <SttlmMtd> [0..1] CodeSet 1742
   ForeignExchangeDetails <FXDtls> [0..1]  1743
     UnitCurrency <UnitCcy> [1..1] CodeSet C3 1743
     QuotedCurrency <QtdCcy> [1..1] CodeSet C3 1744
     ExchangeRate <XchgRate> [1..1] Rate 1744
     QuotationDate <QtnDt> [0..1] DateTime 1744
     QuotingInstitution <QtgInstn> [0..1] ± 1745
   IncomePreference <IncmPref> [0..1] CodeSet 1745
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1727 May 2026
```

## File page 1728

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1745
   TransactionOverhead <TxOvrhd> [0..1]  C19 1745
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1748
     IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
1748
       Type <Tp> [1..1]  1749
{Or         Code <Cd> [1..1] CodeSet 1749
Or}         Proprietary <Prtry> [1..1] ± 1750
       Basis <Bsis> [0..1]  1750
{Or         Code <Cd> [1..1] CodeSet 1751
Or}         Proprietary <Prtry> [1..1] ± 1751
       StandardAmount <StdAmt> [0..1] Amount C3, C10 1751
       StandardRate <StdRate> [0..1] Rate 1752
       DiscountDetails <DscntDtls> [0..1]  C16 1752
         Amount <Amt> [0..1] Amount C3, C10 1752
         Rate <Rate> [0..1] Rate 1753
         Basis <Bsis> [0..1]  1753
{Or           Code <Cd> [1..1] CodeSet 1753
Or}           Proprietary <Prtry> [1..1] ± 1754
       RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 1754
       RequestedRate <ReqdRate> [0..1] Rate 1754
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 1755
       RecipientIdentification <RcptId> [0..1] ± 1755
     IndividualTax <IndvTax> [0..*]  1755
       Type <Tp> [1..1]  1756
{Or         Code <Cd> [1..1] CodeSet 1756
Or}         Proprietary <Prtry> [1..1] ± 1758
       Tax <Tax> [0..1]  1758
{Or         Amount <Amt> [1..1] Amount C3, C10 1758
Or}         Rate <Rate> [1..1] Rate 1759
       Country <Ctry> [0..1] CodeSet C8 1759
       ExemptionIndicator <XmptnInd> [1..1] Indicator 1759
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1728 May 2026
```

## File page 1729

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ExemptionReason <XmptnRsn> [0..1]  1759
{Or         Code <Cd> [1..1] CodeSet 1759
Or}         Proprietary <Prtry> [1..1] ± 1762
       RecipientIdentification <RcptId> [0..1] ± 1762
       TaxCalculationDetails <TaxClctnDtls> [0..1]  1763
         Basis <Bsis> [1..1]  1763
{Or           Code <Cd> [1..1] CodeSet 1763
Or}           Proprietary <Prtry> [1..1] ± 1763
     DigitalNetworkFee <DgtlNtwkFee> [0..*]  1764
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
1764
         ISIN <ISIN> [0..1] IdentifierSet 1766
         OtherIdentification <OthrId> [0..*]  1766
           Identification <Id> [1..1] Text 1766
           Suffix <Sfx> [0..1] Text 1766
           Type <Tp> [1..1]  1766
{Or             Code <Cd> [1..1] CodeSet 1767
Or}             Proprietary <Prtry> [1..1] Text 1768
         Description <Desc> [0..1] Text 1768
       Quantity <Qty> [1..1]  1769
{Or         Quantity <Qty> [1..1] ± C15 1769
Or}         ProprietaryQuantity <PrtryQty> [1..1]  1769
           Quantity <Qty> [1..1] Quantity 1770
           QuantityType <QtyTp> [1..1] Text 1770
           Issuer <Issr> [1..1] Text 1770
           SchemeName <SchmeNm> [0..1] Text 1770
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1770
   SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  1770
     SettlementDate <SttlmDt> [0..1] Date 1772
     SettlementPlace <SttlmPlc> [1..1]  1772
       Party <Pty> [1..1]  1773
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1729 May 2026
```

## File page 1730

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1773
Or         ProprietaryIdentification <PrtryId> [1..1] ± 1773
Or         NameAndAddress <NmAndAdr> [1..1] ± 1774
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1774
       LEI <LEI> [0..1] IdentifierSet 1774
     SafekeepingPlace <SfkpgPlc> [0..1] ± 1774
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1775
     TradeTransactionCondition <TradTxCond> [0..*] ± 1775
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1775
     ReceivingSideDetails <RcvgSdDtls> [1..1]  C31,
C32
1776
       ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  1777
         PartyIdentification <PtyId> [1..1] ± 1777
         AccountIdentification <AcctId> [0..1] Text 1777
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1777
       ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  1778
         PartyIdentification <PtyId> [1..1] ± 1778
         AccountIdentification <AcctId> [0..1] Text 1778
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1778
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  1779
         PartyIdentification <PtyId> [1..1] ± 1779
         AccountIdentification <AcctId> [0..1] Text 1779
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1779
       ReceivingAgentDetails <RcvgAgtDtls> [1..1]  1780
         PartyIdentification <PtyId> [1..1] ± 1780
         AccountIdentification <AcctId> [0..1] Text 1780
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1780
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C12
1781
       DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  1782
         PartyIdentification <PtyId> [1..1] ± 1782
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1730 May 2026
```

## File page 1731

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AccountIdentification <AcctId> [0..1] Text 1782
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1783
       DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  1783
         PartyIdentification <PtyId> [1..1] ± 1783
         AccountIdentification <AcctId> [0..1] Text 1783
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1783
       DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  1784
         PartyIdentification <PtyId> [1..1] ± 1784
         AccountIdentification <AcctId> [0..1] Text 1784
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1784
       DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  1785
         PartyIdentification <PtyId> [1..1] ± 1785
         AccountIdentification <AcctId> [0..1] Text 1785
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 1785
   PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 1786
   PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 1786
   CashSettlementDetails <CshSttlmDtls> [0..1]  1786
     PaymentInstrument <PmtInstrm> [1..1]  1790
{Or       CreditTransferDetails <CdtTrfDtls> [1..1]  1794
         Reference <Ref> [0..1] Text 1797
         Debtor <Dbtr> [0..1] ± 1797
         DebtorAccount <DbtrAcct> [0..1]  1797
           Identification <Id> [1..1]  1797
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1798
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1798
Or}             Other <Othr> [1..1] ± 1798
           Name <Nm> [0..1] Text 1799
         DebtorAgent <DbtrAgt> [0..1]  1799
           Party <Pty> [1..1]  1799
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1800
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1731 May 2026
```

## File page 1732

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1800
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1800
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1801
           LEI <LEI> [0..1] IdentifierSet 1801
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  1802
           Identification <Id> [1..1]  1802
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1802
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1803
Or}             Other <Othr> [1..1] ± 1803
           Name <Nm> [0..1] Text 1803
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  1803
           Party <Pty> [1..1]  1804
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1804
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1804
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1805
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1806
           LEI <LEI> [0..1] IdentifierSet 1806
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1807
           Identification <Id> [1..1]  1807
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1807
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1808
Or}             Other <Othr> [1..1] ± 1808
           Name <Nm> [0..1] Text 1808
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  1808
           Party <Pty> [1..1]  1809
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1809
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1809
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1810
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1811
           LEI <LEI> [0..1] IdentifierSet 1811
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1732 May 2026
```

## File page 1733

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1812
           Identification <Id> [1..1]  1812
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1812
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1813
Or}             Other <Othr> [1..1] ± 1813
           Name <Nm> [0..1] Text 1813
         CreditorAgent <CdtrAgt> [1..1]  1813
           Party <Pty> [1..1]  1814
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1814
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1814
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1815
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1816
           LEI <LEI> [0..1] IdentifierSet 1816
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  1817
           Identification <Id> [1..1]  1817
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1817
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1818
Or}             Other <Othr> [1..1] ± 1818
           Name <Nm> [0..1] Text 1818
         Creditor <Cdtr> [0..1] ± 1818
         CreditorAccount <CdtrAcct> [1..1]  1819
           Identification <Id> [1..1]  1819
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 1819
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1820
Or}             Other <Othr> [1..1] ± 1820
           Name <Nm> [0..1] Text 1820
Or       ChequeDetails <ChqDtls> [1..1]  1820
         Number <Nb> [0..1] Text 1821
         PayeeIdentification <PyeeId> [1..1] ± 1821
         DraweeIdentification <DrweeId> [0..1]  1821
           Party <Pty> [1..1]  1822
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1733 May 2026
```

## File page 1734

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1822
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1822
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1823
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1824
           LEI <LEI> [0..1] IdentifierSet 1824
         DrawerIdentification <DrwrId> [0..1] ± 1825
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  1825
         Number <Nb> [0..1] Text 1825
         PayeeIdentification <PyeeId> [1..1] ± 1825
         DraweeIdentification <DrweeId> [0..1]  1826
           Party <Pty> [1..1]  1826
{Or             NameAndAddress <NmAndAdr> [1..1] ± 1826
Or             BICFI <BICFI> [1..1] IdentifierSet C6 1827
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1827
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1828
           LEI <LEI> [0..1] IdentifierSet 1828
         DrawerIdentification <DrwrId> [0..1] ± 1829
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 1829
         AccountIdentification <AcctId> [0..1] Text 1829
         Type <Tp> [0..1] ± 1829
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  1830
         Identification <Id> [1..1] Text 1830
         Type <Tp> [0..1] ± 1830
         Name <Nm> [0..1] Text 1830
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
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1734 May 2026
```

## File page 1735

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 1833
         Suffix <Sfx> [0..1] Text 1833
         Type <Tp> [1..1]  1833
{Or           Code <Cd> [1..1] CodeSet 1834
Or}           Proprietary <Prtry> [1..1] Text 1835
       Description <Desc> [0..1] Text 1835
     Quantity <Qty> [1..1]  1836
{Or       Quantity <Qty> [1..1] ± C15 1836
Or}       ProprietaryQuantity <PrtryQty> [1..1]  1836
         Quantity <Qty> [1..1] Quantity 1837
         QuantityType <QtyTp> [1..1] Text 1837
         Issuer <Issr> [1..1] Text 1837
         SchemeName <SchmeNm> [0..1] Text 1837
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1837
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 1837
   StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 1837
   FinancialAdvice <FinAdvc> [0..1] CodeSet 1838
   NegotiatedTrade <NgtdTrad> [0..1] CodeSet 1838
   RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 1838
   Equalisation <Equlstn> [0..1] ± 1839
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 1839
   TransactionChannelType <TxChanlTp> [0..1] ± 1839
   SignatureType <SgntrTp> [0..1] ± 1840
   OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C38 1840
Constraints
• OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or one or more occurrences of
RelatedPartyDetails/OrderOriginatorEligibility may be present, but not both.
• PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'false'
 Or    /PhysicalDeliveryIndicator is equal to value '0'
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1735 May 2026
```

