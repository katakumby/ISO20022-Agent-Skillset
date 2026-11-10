---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.9 Conversion <Convs>", "36.4.15.11.9.1 TargetSecurity <TrgtScty>", "36.4.15.11.9.1.1 Identification <Id>", "36.4.15.11.9.1.1.16 OtherProprietaryIdentification <OthrPrtryId>", "36.4.15.11.9.1.1.16.1 Identification <Id>"]
file_pages: [1230, 1231, 1232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.9.1.1.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1230 to 1232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1230

```text
36.4.15.11.9.1.1.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
36.4.15.11.9.1.1.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
36.4.15.11.9.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
36.4.15.11.9.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
36.4.15.11.9.2  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the conversion.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
36.4.15.11.10  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1230 May 2026
```

## File page 1231

```text
UnitsDetails <UnitsDtls> contains the following Unit14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  1233
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1233
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1233
   OrderDate <OrdrDt> [0..1] Date 1233
   AcquisitionDate <AcqstnDt> [0..1] Date 1233
   CertificateNumber <CertNb> [0..*] Text 1233
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1233
   Reference <Ref> [0..1] Text 1234
   PriceDetails <PricDtls> [0..1] ± 1234
   TransactionOverhead <TxOvrhd> [0..1]  C36,
C53
1234
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1236
     TotalFees <TtlFees> [0..1] Amount C1, C18 1237
     TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1237
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1237
     IndividualFee <IndvFee> [0..*]  C6 1238
       Type <Tp> [1..1]  1238
{Or         Code <Cd> [1..1] CodeSet 1239
Or}         Proprietary <Prtry> [1..1] ± 1240
       Basis <Bsis> [0..1]  1240
{Or         Code <Cd> [1..1] CodeSet 1240
Or}         Proprietary <Prtry> [1..1] ± 1241
       StandardAmount <StdAmt> [0..1] Amount C1, C18 1241
       StandardRate <StdRate> [0..1] Rate 1241
       DiscountDetails <DscntDtls> [0..1]  C24 1242
         Amount <Amt> [0..1] Amount C1, C18 1242
         Rate <Rate> [0..1] Rate 1243
         Basis <Bsis> [0..1]  1243
{Or           Code <Cd> [1..1] CodeSet 1243
Or}           Proprietary <Prtry> [1..1] ± 1243
       AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1244
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1231 May 2026
```

## File page 1232

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AppliedRate <ApldRate> [0..1] Rate 1244
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 1244
       RecipientIdentification <RcptId> [0..1] ± 1244
       InformativeIndicator <InftvInd> [1..1] Indicator 1245
     IndividualTax <IndvTax> [0..*] ± 1245
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  1245
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C21,
C22,
C33,
C34,
C37
1246
         ISIN <ISIN> [0..1] IdentifierSet 1248
         OtherIdentification <OthrId> [0..*]  1248
           Identification <Id> [1..1] Text 1248
           Suffix <Sfx> [0..1] Text 1248
           Type <Tp> [1..1]  1248
{Or             Code <Cd> [1..1] CodeSet 1249
Or}             Proprietary <Prtry> [1..1] Text 1250
         Description <Desc> [0..1] Text 1250
       Quantity <Qty> [1..1]  1251
{Or         Quantity <Qty> [1..1] ± C23 1251
Or}         ProprietaryQuantity <PrtryQty> [1..1]  1251
           Quantity <Qty> [1..1] Quantity 1252
           QuantityType <QtyTp> [1..1] Text 1252
           Issuer <Issr> [1..1] Text 1252
           SchemeName <SchmeNm> [0..1] Text 1252
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1252
   OtherAmount <OthrAmt> [0..*]  1252
     Type <Tp> [1..1]  1253
{Or       Code <Cd> [1..1] CodeSet 1253
Or}       ProprietaryCode <PrtryCd> [1..1] ± 1253
     Amount <Amt> [1..1] Amount C1, C18 1253
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1232 May 2026
```

