---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.49 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "46.4.5.10.49.4 FinancialInstrumentIdentification <FinInstrmId>", "46.4.5.10.49.4.1 ISIN <ISIN>"]
file_pages: [2473]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.49.4.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2473 to 2473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2473

```text
FinancialInstrumentIdentification <FinInstrmId> contains one of the following
SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 2473
Or   SEDOL <SEDOL> [1..1] IdentifierSet 2473
Or   CUSIP <CUSIP> [1..1] IdentifierSet 2474
Or   RIC <RIC> [1..1] IdentifierSet 2474
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 2474
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 2474
Or   CTA <CTA> [1..1] IdentifierSet 2474
Or   QUICK <QUICK> [1..1] IdentifierSet 2474
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 2474
Or   Dutch <Dtch> [1..1] IdentifierSet 2475
Or   Valoren <Vlrn> [1..1] IdentifierSet 2475
Or   Sicovam <SCVM> [1..1] IdentifierSet 2475
Or   Belgian <Belgn> [1..1] IdentifierSet 2475
Or   Common <Cmon> [1..1] IdentifierSet 2475
Or   DTI <DTI> [1..1] IdentifierSet 2475
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  2475
     Identification <Id> [1..1] Text 2476
     IdentificationSource <IdSrc> [1..1] ± 2476
46.4.5.10.49.4.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
46.4.5.10.49.4.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2473 May 2026
```

