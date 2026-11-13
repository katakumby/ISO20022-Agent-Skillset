---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.86 FinancialAdvice1Code"]
file_pages: [5302, 5303]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.86 FinancialAdvice1Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5302 to 5303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5302

```text
CodeName Name Definition
F202 FATCA202 Account pool reporting type is a
recalcitrant account holder without US
indicia.
F203 FATCA203 Account pool reporting type is a dormant
account.
F204 FATCA204 Account pool reporting type is a non-
participating foreign financial institution.
F205 FATCA205 Account pool reporting type is a
recalcitrant account holder that is a US
person.
F206 FATCA206 Account pool reporting type is
recalcitrant account holder that is a
passive non-financial foreign entity
(NFFE).
66.2.2.86  FinancialAdvice1Code
Definition: Specifies if advice has been received from an independent financial advisor.
Type: CodeSet
CodeName Name Definition
RECE Received Advice has been received from an
independent financial advisor.
NREC NotReceived Advice has not been received from an
independent financial advisor.
UKWN Unknown It is not known whether or not advice has
been received from an independent
financial advisor.
66.2.2.87  FinancialInstrumentIdentificationType1Code
Definition: Specifies the financial instrument identification type.
Type: CodeSet
CodeName Name Definition
BELC CodeSRWSecretariaatVoorRoerendeWaarden
OrSVMSecrétariatDesValeursMobilières
National securities identification number
for BE issued by the National Numbering
Association SIX Telekurs Belgium.
BLOM Bloomberg Ticker-like code assigned by Bloomberg
to identify financial instruments.
CCCD OtherNationalSecuritiesIdentificationNumber National Securities Identification Number
issued by the National Numbering
Association for a country for which no
specific financial instrument identification
type code already yet. The first two
letters of the code represents the country
code (for example, EGDC for Egyptian
NSIN). To be used only until the code is
added to the ISO
ExternalFinancialInstrumentIdentification
Type1Code list.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5302 May 2026
```

## File page 5303

```text
CodeName Name Definition
CMED ChicagoMercantileExchangeCME Ticker-like code assigned by the
Chicago Mercantile Exchange to identify
listed-derivatives instruments.
COMM CommonCode National securities identification number
for ICSDs issued by the National
Numbering Association Clearstream and
Euroclear.
CTAC ConsolidatedTapeAssociationCTA Ticker-like code assigned by the
Consolidated Tape Association to
identify financial instruments.
CUSP CommitteeOnUniformSecurityIdentificationProc
eduresCUSIP
National securities identification number
for US and CA issued by the National
Numbering Association Standard & Poor
´s - CUSIP Global Services.
FIGC FinancialInstrumentGlobalIdentifierComposite A Financial Instrument Global Identifier
Composite (FIGC) is a unique, persistent
twelve character string that serves to
identify financial instruments across
asset classes at the composite level, is
associated with one or more FIGI venue
level ID's and a single Share Class level
ID.
FIGG FinancialInstrumentGlobalIdentifierShareClass A Financial Instrument Global Identifier
Share Class (FIGG) is a unique,
persistent twelve character string that
serves to identify financial instruments
across asset classes at the global share
class level, and is associated with one or
more Composite level ID's.
FIGI FinancialInstrumentGlobalIdentifier A Financial Instrument Global Identifier
(FIGI) is a unique, persistent twelve
character string that serves to identify
financial instruments across asset
classes at the venue level. It is
associated with one Composite ID.
ISDU ISDAAndFpMLProductURLInSecurityID URL in Description to identify OTC
derivatives instruments.
ISDX ISDAAndFpMLProductSpecificationXMLInEnco
dedSecurityDesc
XML in Description to identify OTC
derivatives instruments.
LCHD LCHClearnet Ticker-like code assigned by LCH to
identify listed-derivatives instruments.
OCCS OptionsClearingCorpOCC Ticker-like code assigned by the Options
Clearing Corporation to identify financial
instruments.
OPRA OptionsPriceReportingAuthorityOPRA Ticker-like code assigned by the Options
Price Reporting Authority to identify
financial instruments.
RCMD MarkitRedCode Ticker-like code assigned by Markit to
identify listed-derivatives instruments.
RICC ReutersInstrumentCodeRIC Ticker-like code assigned by Thomson
Reuters to identify financial instruments.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5303 May 2026
```

