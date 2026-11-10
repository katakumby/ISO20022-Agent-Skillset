---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.6 FinancialInstrumentDetails <FinInstrmDtls>", "52.4.5.10.6.1 Identification <Id>"]
file_pages: [3307]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.6.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3307 to 3307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3307

```text
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
52.4.5.10.6.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 3307
Or   SEDOL <SEDOL> [1..1] IdentifierSet 3308
Or   CUSIP <CUSIP> [1..1] IdentifierSet 3308
Or   RIC <RIC> [1..1] IdentifierSet 3308
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 3308
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 3308
Or   CTA <CTA> [1..1] IdentifierSet 3308
Or   QUICK <QUICK> [1..1] IdentifierSet 3308
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 3309
Or   Dutch <Dtch> [1..1] IdentifierSet 3309
Or   Valoren <Vlrn> [1..1] IdentifierSet 3309
Or   Sicovam <SCVM> [1..1] IdentifierSet 3309
Or   Belgian <Belgn> [1..1] IdentifierSet 3309
Or   Common <Cmon> [1..1] IdentifierSet 3309
Or   DTI <DTI> [1..1] IdentifierSet 3309
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  3309
     Identification <Id> [1..1] Text 3310
     IdentificationSource <IdSrc> [1..1] ± 3310
52.4.5.10.6.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3307 May 2026
```

