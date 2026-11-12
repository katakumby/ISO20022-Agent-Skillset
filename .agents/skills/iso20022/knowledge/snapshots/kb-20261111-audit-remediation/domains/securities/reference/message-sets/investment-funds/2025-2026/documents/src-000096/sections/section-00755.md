---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.8 Conversion <Convs>", "35.4.14.10.8.1 TargetSecurity <TrgtScty>", "35.4.14.10.8.1.1 Identification <Id>", "35.4.14.10.8.1.1.16 OtherProprietaryIdentification <OthrPrtryId>", "35.4.14.10.8.1.1.16.1 Identification <Id>"]
file_pages: [1035, 1036, 1037]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.8.1.1.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1035 to 1037.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1035

```text
35.4.14.10.8.1.1.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
35.4.14.10.8.1.1.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
35.4.14.10.8.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
35.4.14.10.8.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
35.4.14.10.8.2  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the conversion.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
35.4.14.10.9  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1035 May 2026
```

## File page 1036

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  1038
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1038
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1038
   OrderDate <OrdrDt> [0..1] Date 1038
   AcquisitionDate <AcqstnDt> [0..1] Date 1038
   CertificateNumber <CertNb> [0..*] Text 1038
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1038
   Reference <Ref> [0..1] Text 1039
   PriceDetails <PricDtls> [0..1] ± 1039
   TransactionOverhead <TxOvrhd> [0..1]  C34,
C46
1039
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1041
     TotalFees <TtlFees> [0..1] Amount C1, C18 1042
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1042
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1042
     IndividualFee <IndvFee> [0..*]  C6 1043
       Type <Tp> [1..1]  1043
{Or         Code <Cd> [1..1] CodeSet 1044
Or}         Proprietary <Prtry> [1..1] ± 1045
       Basis <Bsis> [0..1]  1045
{Or         Code <Cd> [1..1] CodeSet 1045
Or}         Proprietary <Prtry> [1..1] ± 1046
       StandardAmount <StdAmt> [0..1] Amount C1, C18 1046
       StandardRate <StdRate> [0..1] Rate 1046
       DiscountDetails <DscntDtls> [0..1]  C23 1047
         Amount <Amt> [0..1] Amount C1, C18 1047
         Rate <Rate> [0..1] Rate 1048
         Basis <Bsis> [0..1]  1048
{Or           Code <Cd> [1..1] CodeSet 1048
Or}           Proprietary <Prtry> [1..1] ± 1048
       AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1049
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1036 May 2026
```

## File page 1037

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 1049
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 1049
       RecipientIdentification <RcptId> [0..1] ± 1049
       InformativeIndicator <InftvInd> [1..1] Indicator 1050
     IndividualTax <IndvTax> [0..*] ± 1050
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  1050
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C20,
C21,
C31,
C32,
C35
1051
         ISIN <ISIN> [0..1] IdentifierSet 1053
         OtherIdentification <OthrId> [0..*]  1053
           Identification <Id> [1..1] Text 1053
           Suffix <Sfx> [0..1] Text 1053
           Type <Tp> [1..1]  1053
{Or             Code <Cd> [1..1] CodeSet 1054
Or}             Proprietary <Prtry> [1..1] Text 1055
         Description <Desc> [0..1] Text 1055
       Quantity <Qty> [1..1]  1056
{Or         Quantity <Qty> [1..1] ± C22 1056
Or}         ProprietaryQuantity <PrtryQty> [1..1]  1056
           Quantity <Qty> [1..1] Quantity 1057
           QuantityType <QtyTp> [1..1] Text 1057
           Issuer <Issr> [1..1] Text 1057
           SchemeName <SchmeNm> [0..1] Text 1057
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1057
   OtherAmount <OthrAmt> [0..*]  1057
     Type <Tp> [1..1]  1058
{Or       Code <Cd> [1..1] CodeSet 1058
Or}       ProprietaryCode <PrtryCd> [1..1] ± 1058
     Amount <Amt> [1..1] Amount C1, C18 1058
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1037 May 2026
```

