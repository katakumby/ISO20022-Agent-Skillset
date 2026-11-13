---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.5 FinancialInstrumentDetails <FinInstrmDtls>", "44.4.4.9.5.1 Identification <Id>"]
file_pages: [2151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.5.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2151 to 2151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2151

```text
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
44.4.4.9.5.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 2151
Or   SEDOL <SEDOL> [1..1] IdentifierSet 2152
Or   CUSIP <CUSIP> [1..1] IdentifierSet 2152
Or   RIC <RIC> [1..1] IdentifierSet 2152
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 2152
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 2152
Or   CTA <CTA> [1..1] IdentifierSet 2152
Or   QUICK <QUICK> [1..1] IdentifierSet 2152
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 2153
Or   Dutch <Dtch> [1..1] IdentifierSet 2153
Or   Valoren <Vlrn> [1..1] IdentifierSet 2153
Or   Sicovam <SCVM> [1..1] IdentifierSet 2153
Or   Belgian <Belgn> [1..1] IdentifierSet 2153
Or   Common <Cmon> [1..1] IdentifierSet 2153
Or   DTI <DTI> [1..1] IdentifierSet 2153
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  2153
     Identification <Id> [1..1] Text 2154
     IdentificationSource <IdSrc> [1..1] ± 2154
44.4.4.9.5.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2151 May 2026
```

