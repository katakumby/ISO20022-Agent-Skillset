---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.47 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "43.4.5.9.47.4 FinancialInstrumentIdentification <FinInstrmId>", "43.4.5.9.47.4.1 ISIN <ISIN>"]
file_pages: [2050]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.47.4.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2050 to 2050.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2050

```text
FinancialInstrumentIdentification <FinInstrmId> contains one of the following
SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 2050
Or   SEDOL <SEDOL> [1..1] IdentifierSet 2050
Or   CUSIP <CUSIP> [1..1] IdentifierSet 2051
Or   RIC <RIC> [1..1] IdentifierSet 2051
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 2051
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 2051
Or   CTA <CTA> [1..1] IdentifierSet 2051
Or   QUICK <QUICK> [1..1] IdentifierSet 2051
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 2051
Or   Dutch <Dtch> [1..1] IdentifierSet 2052
Or   Valoren <Vlrn> [1..1] IdentifierSet 2052
Or   Sicovam <SCVM> [1..1] IdentifierSet 2052
Or   Belgian <Belgn> [1..1] IdentifierSet 2052
Or   Common <Cmon> [1..1] IdentifierSet 2052
Or   DTI <DTI> [1..1] IdentifierSet 2052
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  2052
     Identification <Id> [1..1] Text 2053
     IdentificationSource <IdSrc> [1..1] ± 2053
43.4.5.9.47.4.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
43.4.5.9.47.4.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2050 May 2026
```

