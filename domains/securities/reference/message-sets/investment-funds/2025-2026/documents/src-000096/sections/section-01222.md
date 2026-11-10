---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks"]
file_pages: [1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1702 to 1711.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1702

```text
C31 ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present.
If ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
C32 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C33 RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences
of IndividualOrderDetails/SettlementAmount, if present.
C34 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C35 SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualOrderDetails/
SettlementAmount, if present, must be the same in all occurrences of IndividualOrderDetails.
C36 StandardFeeAmountCalculation
If StandardAmount, RequestedAmount and DiscountDetails/Amount are all present, then
StandardAmount minus DiscountDetails/Amount must equal RequestedAmount.
C37 StandardFeeRateCalculation
If StandardRate, RequestedRate and DiscountDetails/Rate are all present, then StandardRate
minus DiscountDetails/Rate must equal RequestedRate.
C38 WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
41.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
41.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
41.4.2 PoolReference <PoolRef>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1702 May 2026
```

## File page 1703

```text
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
41.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
41.4.4 BulkOrderDetails <BlkOrdrDtls>
Presence: [1..1]
Definition: General information related to the orders.
Impacted by: C7 "BulkCashSettlementDetailsRule", C33 "RequestedSettlementCurrencyRule", C35
"SettlementCurrencyRule"
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1703 May 2026
```

## File page 1704

```text
BulkOrderDetails <BlkOrdrDtls> contains the following RedemptionBulkOrder08 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 1717
   PlaceOfTrade <PlcOfTrad> [0..1] ± 1717
   OrderDateTime <OrdrDtTm> [0..1] DateTime 1718
   ExpiryDateTime <XpryDtTm> [0..1] ± 1718
   RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 1718
   CancellationRight <CxlRght> [0..1] ± 1718
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C21 1719
     Identification <Id> [1..1]  1721
{Or       ISIN <ISIN> [1..1] IdentifierSet 1721
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1722
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1722
Or       RIC <RIC> [1..1] IdentifierSet 1722
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1722
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1722
Or       CTA <CTA> [1..1] IdentifierSet 1722
Or       QUICK <QUICK> [1..1] IdentifierSet 1722
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1723
Or       Dutch <Dtch> [1..1] IdentifierSet 1723
Or       Valoren <Vlrn> [1..1] IdentifierSet 1723
Or       Sicovam <SCVM> [1..1] IdentifierSet 1723
Or       Belgian <Belgn> [1..1] IdentifierSet 1723
Or       Common <Cmon> [1..1] IdentifierSet 1723
Or       DTI <DTI> [1..1] IdentifierSet 1723
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1723
         Identification <Id> [1..1] Text 1724
         IdentificationSource <IdSrc> [1..1] ± 1724
     Name <Nm> [0..1] Text 1724
     ShortName <ShrtNm> [0..1] Text 1724
     SupplementaryIdentification <SplmtryId> [0..1] Text 1724
     ClassType <ClssTp> [0..1] Text 1724
     SecuritiesForm <SctiesForm> [0..1] CodeSet 1725
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1704 May 2026
```

## File page 1705

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1725
     ProductGroup <PdctGrp> [0..1] Text 1725
     SeriesIdentification <SrsId> [0..1]  C34 1725
       SeriesDate <SrsDt> [0..1] ± 1726
       SeriesName <SrsNm> [0..1] Text 1726
   IndividualOrderDetails <IndvOrdrDtls> [1..*]  C26,
C29,
C30
1726
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
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1740
Or       GrossAmount <GrssAmt> [1..1] Amount C4, C9 1741
Or       NetAmount <NetAmt> [1..1] Amount C4, C9 1741
Or       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1741
Or}       HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 1742
     Rounding <Rndg> [0..1] CodeSet 1742
     SettlementAmount <SttlmAmt> [0..1] Amount C3, C10 1742
     CashSettlementDate <CshSttlmDt> [0..1] Date 1742
     SettlementMethod <SttlmMtd> [0..1] CodeSet 1742
     ForeignExchangeDetails <FXDtls> [0..1]  1743
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1705 May 2026
```

## File page 1706

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       UnitCurrency <UnitCcy> [1..1] CodeSet C3 1743
       QuotedCurrency <QtdCcy> [1..1] CodeSet C3 1744
       ExchangeRate <XchgRate> [1..1] Rate 1744
       QuotationDate <QtnDt> [0..1] DateTime 1744
       QuotingInstitution <QtgInstn> [0..1] ± 1745
     IncomePreference <IncmPref> [0..1] CodeSet 1745
     Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1745
     TransactionOverhead <TxOvrhd> [0..1]  C19 1745
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 1748
       IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
1748
         Type <Tp> [1..1]  1749
{Or           Code <Cd> [1..1] CodeSet 1749
Or}           Proprietary <Prtry> [1..1] ± 1750
         Basis <Bsis> [0..1]  1750
{Or           Code <Cd> [1..1] CodeSet 1751
Or}           Proprietary <Prtry> [1..1] ± 1751
         StandardAmount <StdAmt> [0..1] Amount C3, C10 1751
         StandardRate <StdRate> [0..1] Rate 1752
         DiscountDetails <DscntDtls> [0..1]  C16 1752
           Amount <Amt> [0..1] Amount C3, C10 1752
           Rate <Rate> [0..1] Rate 1753
           Basis <Bsis> [0..1]  1753
{Or             Code <Cd> [1..1] CodeSet 1753
Or}             Proprietary <Prtry> [1..1] ± 1754
         RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 1754
         RequestedRate <ReqdRate> [0..1] Rate 1754
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 1755
         RecipientIdentification <RcptId> [0..1] ± 1755
       IndividualTax <IndvTax> [0..*]  1755
         Type <Tp> [1..1]  1756
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1706 May 2026
```

## File page 1707

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 1756
Or}           Proprietary <Prtry> [1..1] ± 1758
         Tax <Tax> [0..1]  1758
{Or           Amount <Amt> [1..1] Amount C3, C10 1758
Or}           Rate <Rate> [1..1] Rate 1759
         Country <Ctry> [0..1] CodeSet C8 1759
         ExemptionIndicator <XmptnInd> [1..1] Indicator 1759
         ExemptionReason <XmptnRsn> [0..1]  1759
{Or           Code <Cd> [1..1] CodeSet 1759
Or}           Proprietary <Prtry> [1..1] ± 1762
         RecipientIdentification <RcptId> [0..1] ± 1762
         TaxCalculationDetails <TaxClctnDtls> [0..1]  1763
           Basis <Bsis> [1..1]  1763
{Or             Code <Cd> [1..1] CodeSet 1763
Or}             Proprietary <Prtry> [1..1] ± 1763
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
{Or               Code <Cd> [1..1] CodeSet 1767
Or}               Proprietary <Prtry> [1..1] Text 1768
           Description <Desc> [0..1] Text 1768
         Quantity <Qty> [1..1]  1769
{Or           Quantity <Qty> [1..1] ± C15 1769
Or}           ProprietaryQuantity <PrtryQty> [1..1]  1769
             Quantity <Qty> [1..1] Quantity 1770
             QuantityType <QtyTp> [1..1] Text 1770
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1707 May 2026
```

## File page 1708

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Issuer <Issr> [1..1] Text 1770
             SchemeName <SchmeNm> [0..1] Text 1770
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1770
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  1770
       SettlementDate <SttlmDt> [0..1] Date 1772
       SettlementPlace <SttlmPlc> [1..1]  1772
         Party <Pty> [1..1]  1773
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1773
Or           ProprietaryIdentification <PrtryId> [1..1] ± 1773
Or           NameAndAddress <NmAndAdr> [1..1] ± 1774
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1774
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
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1708 May 2026
```

## File page 1709

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  1794
           Reference <Ref> [0..1] Text 1797
           Debtor <Dbtr> [0..1] ± 1797
           DebtorAccount <DbtrAcct> [0..1]  1797
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1709 May 2026
```

## File page 1710

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Identification <Id> [1..1]  1797
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1798
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1798
Or}               Other <Othr> [1..1] ± 1798
             Name <Nm> [0..1] Text 1799
           DebtorAgent <DbtrAgt> [0..1]  1799
             Party <Pty> [1..1]  1799
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1800
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1800
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1800
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1801
             LEI <LEI> [0..1] IdentifierSet 1801
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  1802
             Identification <Id> [1..1]  1802
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1802
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1803
Or}               Other <Othr> [1..1] ± 1803
             Name <Nm> [0..1] Text 1803
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  1803
             Party <Pty> [1..1]  1804
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1804
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1804
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1805
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1806
             LEI <LEI> [0..1] IdentifierSet 1806
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1807
             Identification <Id> [1..1]  1807
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1807
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1808
Or}               Other <Othr> [1..1] ± 1808
             Name <Nm> [0..1] Text 1808
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1710 May 2026
```

## File page 1711

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  1808
             Party <Pty> [1..1]  1809
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1809
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1809
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1810
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1811
             LEI <LEI> [0..1] IdentifierSet 1811
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1812
             Identification <Id> [1..1]  1812
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1812
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1813
Or}               Other <Othr> [1..1] ± 1813
             Name <Nm> [0..1] Text 1813
           CreditorAgent <CdtrAgt> [1..1]  1813
             Party <Pty> [1..1]  1814
{Or               NameAndAddress <NmAndAdr> [1..1] ± 1814
Or               BICFI <BICFI> [1..1] IdentifierSet C6 1814
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 1815
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 1816
             LEI <LEI> [0..1] IdentifierSet 1816
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  1817
             Identification <Id> [1..1]  1817
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1817
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1818
Or}               Other <Othr> [1..1] ± 1818
             Name <Nm> [0..1] Text 1818
           Creditor <Cdtr> [0..1] ± 1818
           CreditorAccount <CdtrAcct> [1..1]  1819
             Identification <Id> [1..1]  1819
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 1819
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1820
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1711 May 2026
```

