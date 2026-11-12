---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalFinancialInstrumentIdentificationType1Code"]
code_set: "ExternalFinancialInstrumentIdentificationType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalFinancialInstrumentIdentificationType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalFinancialInstrumentIdentificationType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external financial instrument identification type scheme name code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`BELC`-National securities identification number for BE issued by the National Numbering Association SIX Telekurs Belgium.
*`BLOM`-Ticker-like code assigned by Bloomberg to identify financial instruments.
*`CCCD`-National Securities Identification Number issued by the National Numbering Association for a country for which no specific financial instrument identification type code already yet. The first two letters of the code represents the country code (for example, EGDC for Egyptian NSIN). To be used only until the code is added to the ISO ExternalFinancialInstrumentIdentificationType1Code list.
*`CMED`-Ticker-like code assigned by the Chicago Mercantile Exchange to identify listed-derivatives instruments.
*`COMM`-National securities identification number for ICSDs issued by the National Numbering Association Clearstream and Euroclear.
*`CTAC`-Ticker-like code assigned by the Consolidated Tape Association to identify financial instruments.
*`CUSP`-National securities identification number for US and CA issued by the National Numbering Association Standard & Poor´s - CUSIP Global Services.
*`FIGC`-A Financial Instrument Global Identifier Composite (FIGC) is a unique, persistent twelve character string that serves to identify financial instruments across asset classes at the composite level, is associated with one or more FIGI venue level ID’s and a single Share Class level ID.
*`FIGG`-A Financial Instrument Global Identifier Share Class (FIGG) is a unique, persistent twelve character string that serves to identify financial instruments across asset classes at the global share class level, and is associated with one or more Composite level ID’s.
*`FIGI`-A Financial Instrument Global Identifier (FIGI) is a unique, persistent twelve character string that serves to identify financial instruments across asset classes at the venue level. It is associated with one Composite ID.
*`ISDU`-URL in Description to identify OTC derivatives instruments.
*`ISDX`-XML in Description to identify OTC derivatives instruments.
*`LCHD`-Ticker-like code assigned by LCH to identify listed-derivatives instruments.
*`OCCS`-Ticker-like code assigned by the Options Clearing Corporation to identify financial instruments.
*`OPRA`-Ticker-like code assigned by the Options Price Reporting Authority to identify financial instruments.
*`RCMD`-Ticker-like code assigned by Markit to identify listed-derivatives instruments.
*`RICC`-Ticker-like code assigned by Thomson Reuters to identify financial instruments.
*`SEDL`-National securities identification number for GB issued by the National Numbering Association London Stock Exchange.
*`SICC`-National securities identification number for JP issued by the National Numbering Association 6 Stock Exchanges and JASDEC (Securities Identification Ticker-like code Committee)
*`TIKR`-Ticker Code assigned by an exchange to identify financial instruments.
*`VALO`-National securities identification number for CH and LI issued by the National Numbering Association SIX Telekurs Ltd.
*`WKNR`-National securities identification number for DE issued by the National Numbering Association WM Datenservice.
*`CCDC`-National Bond identification number for China issued by CHINA CENTRAL DEPOSITORY & CLEARING CO., Limited.
*`DTID`-Digital Token Identifier, as defined in ISO 24165.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | BELC |
| 2 | BLOM |
| 3 | CCCD |
| 4 | CMED |
| 5 | COMM |
| 6 | CTAC |
| 7 | CUSP |
| 8 | FIGC |
| 9 | FIGG |
| 10 | FIGI |
| 11 | ISDU |
| 12 | ISDX |
| 13 | LCHD |
| 14 | OCCS |
| 15 | OPRA |
| 16 | RCMD |
| 17 | RICC |
| 18 | SEDL |
| 19 | SICC |
| 20 | TIKR |
| 21 | VALO |
| 22 | WKNR |
| 23 | CCDC |
| 24 | DTID |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
