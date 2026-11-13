---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.11 ProductType <PdctTp>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.11 ProductType <PdctTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
15.4.5.8.11  ProductType <PdctTp>
Presence: [0..1]
Definition: Classification of the financial instrument. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 00060.
ProductType <PdctTp> contains one of the following ProductStructure1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 316
Or}   Proprietary <Prtry> [1..1] ± 316
15.4.5.8.11.1  Code <Cd>
Presence: [1..1]
Definition: Product structure expressed as a code.
Datatype: "ProductStructure1Code" on page 5344
CodeName Name Definition
BOND Bond Product is a bond.
NUMM NonUCITSMoneyMarketFund Product is a money market fund that is
not an Undertaking for Collective
Investment in Transferable Securities
(UCITS).
UCMM UCITSMoneyMarketFund Product is an Undertaking for Collective
Investment in Transferable Securities
(UCITS) money market fund.
EXTC ExchangeTradedCommodity Product is an exchange traded
commodity.
UCIT UCITS Product is an Undertaking for Collective
Investment in Transferable Securities
(UCITS).
SSEC StructuredSecurity Product is a structured security.
SFUN StructuredFund Product is a structured fund.
NUCI NonUCITS Product is a not an Undertaking for
Collective Investment in Transferable
Securities (UCITS).
15.4.5.8.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Product structure expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 316 May 2026
```

