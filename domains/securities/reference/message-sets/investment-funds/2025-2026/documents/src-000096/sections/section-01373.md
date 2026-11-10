---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.8 FinancialInstrumentDetails <FinInstrmDtls>", "43.4.5.8.1 Identification <Id>"]
file_pages: [1930]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.8.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1930 to 1930.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1930

```text
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
43.4.5.8.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 1930
Or   SEDOL <SEDOL> [1..1] IdentifierSet 1931
Or   CUSIP <CUSIP> [1..1] IdentifierSet 1931
Or   RIC <RIC> [1..1] IdentifierSet 1931
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 1931
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 1931
Or   CTA <CTA> [1..1] IdentifierSet 1931
Or   QUICK <QUICK> [1..1] IdentifierSet 1931
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 1932
Or   Dutch <Dtch> [1..1] IdentifierSet 1932
Or   Valoren <Vlrn> [1..1] IdentifierSet 1932
Or   Sicovam <SCVM> [1..1] IdentifierSet 1932
Or   Belgian <Belgn> [1..1] IdentifierSet 1932
Or   Common <Cmon> [1..1] IdentifierSet 1932
Or   DTI <DTI> [1..1] IdentifierSet 1932
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  1932
     Identification <Id> [1..1] Text 1933
     IdentificationSource <IdSrc> [1..1] ± 1933
43.4.5.8.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1930 May 2026
```

