---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.13 FinancialInstrumentDetails <FinInstrmDtls>", "30.4.7.13.1 Identification <Id>"]
file_pages: [717]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.13.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 717 to 717.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 717

```text
When an ISIN code exists, it is strongly recommended that the ISIN be used.
30.4.7.13.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 717
Or   SEDOL <SEDOL> [1..1] IdentifierSet 717
Or   CUSIP <CUSIP> [1..1] IdentifierSet 718
Or   RIC <RIC> [1..1] IdentifierSet 718
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 718
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 718
Or   CTA <CTA> [1..1] IdentifierSet 718
Or   QUICK <QUICK> [1..1] IdentifierSet 718
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 718
Or   Dutch <Dtch> [1..1] IdentifierSet 719
Or   Valoren <Vlrn> [1..1] IdentifierSet 719
Or   Sicovam <SCVM> [1..1] IdentifierSet 719
Or   Belgian <Belgn> [1..1] IdentifierSet 719
Or   Common <Cmon> [1..1] IdentifierSet 719
Or   DTI <DTI> [1..1] IdentifierSet 719
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  719
     Identification <Id> [1..1] Text 720
     IdentificationSource <IdSrc> [1..1] ± 720
30.4.7.13.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
30.4.7.13.1.2  SEDOL <SEDOL>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 717 May 2026
```

