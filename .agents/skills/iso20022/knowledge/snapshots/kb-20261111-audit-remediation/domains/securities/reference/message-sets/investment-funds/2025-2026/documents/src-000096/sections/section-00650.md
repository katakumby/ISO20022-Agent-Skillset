---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.17 Conversion <Convs>"]
file_pages: [884, 885]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.17 Conversion <Convs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 884 to 885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 884

```text
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
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
34.4.4.17  Conversion <Convs>
Presence: [0..1]
Definition: Information about the source security following a conversion.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 884 May 2026
```

## File page 885

```text
Conversion <Convs> contains the following Conversion4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SourceSecurity <SrcScty> [1..1]  C19 886
     Identification <Id> [1..1]  887
{Or       ISIN <ISIN> [1..1] IdentifierSet 887
Or       SEDOL <SEDOL> [1..1] IdentifierSet 888
Or       CUSIP <CUSIP> [1..1] IdentifierSet 888
Or       RIC <RIC> [1..1] IdentifierSet 888
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 888
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 888
Or       CTA <CTA> [1..1] IdentifierSet 888
Or       QUICK <QUICK> [1..1] IdentifierSet 888
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 889
Or       Dutch <Dtch> [1..1] IdentifierSet 889
Or       Valoren <Vlrn> [1..1] IdentifierSet 889
Or       Sicovam <SCVM> [1..1] IdentifierSet 889
Or       Belgian <Belgn> [1..1] IdentifierSet 889
Or       Common <Cmon> [1..1] IdentifierSet 889
Or       DTI <DTI> [1..1] IdentifierSet 889
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  889
         Identification <Id> [1..1] Text 890
         IdentificationSource <IdSrc> [1..1] ± 890
     Name <Nm> [0..1] Text 890
     ShortName <ShrtNm> [0..1] Text 890
   TotalUnitsNumber <TtlUnitsNb> [0..1] Quantity 890
   UnitsDetails <UnitsDtls> [0..*]  890
     Units <Units> [1..1]  891
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 891
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 891
     OrderDate <OrdrDt> [0..1] Date 891
     AcquisitionDate <AcqstnDt> [0..1] Date 891
     CertificateNumber <CertNb> [0..*] Text 892
     Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 892
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 885 May 2026
```

