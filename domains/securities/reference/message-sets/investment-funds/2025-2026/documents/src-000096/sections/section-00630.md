---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.11 SettlementDate <SttlmDt>"]
file_pages: [860, 861, 862]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.11 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 860 to 862.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 860

```text
34.4.4.11  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date at which the securities are to be exchanged or were exchanged at the International
Central Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
34.4.4.12  SendOutDate <SndOutDt>
Presence: [0..1]
Definition: Date on which the document, for example, the application form, was sent.
Datatype: "ISODate" on page 5388
34.4.4.13  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
34.4.4.14  TotalUnitsNumber <TtlUnitsNb>
Presence: [0..1]
Definition: Number of units to be transferred.
Datatype: "DecimalNumber" on page 5400
34.4.4.15  AveragePrice <AvrgPric>
Presence: [0..1]
Definition: Weighted average price of the units in the account. The average price may also be known as
the average acquisition price.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
34.4.4.16  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units to be transferred.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 860 May 2026
```

## File page 861

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  863
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 863
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 863
   OrderDate <OrdrDt> [0..1] Date 863
   AcquisitionDate <AcqstnDt> [0..1] Date 863
   CertificateNumber <CertNb> [0..*] Text 863
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 863
   Reference <Ref> [0..1] Text 864
   PriceDetails <PricDtls> [0..1] ± 864
   TransactionOverhead <TxOvrhd> [0..1]  C22,
C27
864
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 866
     TotalFees <TtlFees> [0..1] Amount C1, C10 867
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 867
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 867
     IndividualFee <IndvFee> [0..*]  C4 868
       Type <Tp> [1..1]  868
{Or         Code <Cd> [1..1] CodeSet 869
Or}         Proprietary <Prtry> [1..1] ± 870
       Basis <Bsis> [0..1]  870
{Or         Code <Cd> [1..1] CodeSet 870
Or}         Proprietary <Prtry> [1..1] ± 871
       StandardAmount <StdAmt> [0..1] Amount C1, C10 871
       StandardRate <StdRate> [0..1] Rate 871
       DiscountDetails <DscntDtls> [0..1]  C14 872
         Amount <Amt> [0..1] Amount C1, C10 872
         Rate <Rate> [0..1] Rate 873
         Basis <Bsis> [0..1]  873
{Or           Code <Cd> [1..1] CodeSet 873
Or}           Proprietary <Prtry> [1..1] ± 873
       AppliedAmount <ApldAmt> [0..1] Amount C1, C10 874
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 861 May 2026
```

## File page 862

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 874
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 874
       RecipientIdentification <RcptId> [0..1] ± 874
       InformativeIndicator <InftvInd> [1..1] Indicator 875
     IndividualTax <IndvTax> [0..*] ± 875
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  875
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C20,
C21,
C23
876
         ISIN <ISIN> [0..1] IdentifierSet 878
         OtherIdentification <OthrId> [0..*]  878
           Identification <Id> [1..1] Text 878
           Suffix <Sfx> [0..1] Text 878
           Type <Tp> [1..1]  878
{Or             Code <Cd> [1..1] CodeSet 879
Or}             Proprietary <Prtry> [1..1] Text 880
         Description <Desc> [0..1] Text 880
       Quantity <Qty> [1..1]  881
{Or         Quantity <Qty> [1..1] ± C13 881
Or}         ProprietaryQuantity <PrtryQty> [1..1]  881
           Quantity <Qty> [1..1] Quantity 882
           QuantityType <QtyTp> [1..1] Text 882
           Issuer <Issr> [1..1] Text 882
           SchemeName <SchmeNm> [0..1] Text 882
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 882
   OtherAmount <OthrAmt> [0..*]  882
     Type <Tp> [1..1]  883
{Or       Code <Cd> [1..1] CodeSet 883
Or}       ProprietaryCode <PrtryCd> [1..1] ± 883
     Amount <Amt> [1..1] Amount C1, C10 883
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 862 May 2026
```

