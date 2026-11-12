---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.12 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "56.4.3.2.12.4 FinancialInstrumentIdentification <FinInstrmId>", "56.4.3.2.12.4.1 ISIN <ISIN>"]
file_pages: [4170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.12.4.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4170 to 4170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4170

```text
FinancialInstrumentIdentification <FinInstrmId> contains one of the following
SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 4170
Or   SEDOL <SEDOL> [1..1] IdentifierSet 4170
Or   CUSIP <CUSIP> [1..1] IdentifierSet 4171
Or   RIC <RIC> [1..1] IdentifierSet 4171
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 4171
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 4171
Or   CTA <CTA> [1..1] IdentifierSet 4171
Or   QUICK <QUICK> [1..1] IdentifierSet 4171
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 4171
Or   Dutch <Dtch> [1..1] IdentifierSet 4172
Or   Valoren <Vlrn> [1..1] IdentifierSet 4172
Or   Sicovam <SCVM> [1..1] IdentifierSet 4172
Or   Belgian <Belgn> [1..1] IdentifierSet 4172
Or   Common <Cmon> [1..1] IdentifierSet 4172
Or   DTI <DTI> [1..1] IdentifierSet 4172
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  4172
     Identification <Id> [1..1] Text 4173
     IdentificationSource <IdSrc> [1..1] ± 4173
56.4.3.2.12.4.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
56.4.3.2.12.4.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4170 May 2026
```

